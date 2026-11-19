# Triển khai dự án mới trên Vercel

1. Trong tài khoản/team Vercel **mới**, tạo project `fforum` nếu tên còn khả dụng. Không chỉnh, chuyển hoặc xóa project cũ. Dùng nhánh hiện tại khi thử nghiệm, đặt **Root Directory** là `f_forumv3`, framework Vite, Node.js 22. Vercel gọi `npm run build`, phục vụ `dist/` và function `api/studio.js`.
2. Tạo một dự án Supabase mới, chạy `supabase/schema.sql` một lần trong DB trống. Bật email OTP/magic link. Cấu hình Site URL và danh sách redirect chính xác cho `/home` ở môi trường triển khai; không dùng wildcard cho mọi host production. Cấu hình email rate limits và SMTP. Chỉ mở sign-up công khai khi đã có kiểm soát chống spam.
3. Cấu hình các biến trong `.env.example`. `SUPABASE_ANON_KEY` chỉ là khóa công khai dành cho client; service role và khóa AI ở server. `AI_BASE_URL` là base HTTPS của API tương thích OpenAI, không gồm `/chat/completions`. `AI_MODEL` do người triển khai quyết định. Mỗi môi trường dùng khóa riêng, ngân sách riêng. Không dùng khóa từng được dán trong chat.
4. Tạo tài khoản quản trị riêng bằng quy trình quản lý của Supabase. Lấy UUID đã xác minh đưa vào `ADMIN_USER_IDS` phía server. Không cấp admin từ email hiển thị hay `user_metadata`. Kiểm tra `/admin` bằng hai tài khoản trước khi phát hành.
5. Dùng repo `f_forumv3` riêng khi đã có quyền tạo và cấu hình đích. Mã/tài liệu hiện ở thư mục `f_forumv3/` của nhánh Arena. Không đồng bộ sang project cũ. Mọi chỉnh sửa UX sau này cập nhật `docs/DESIGN.md` cùng mã; sửa phạm vi hoặc cấu hình cập nhật README, nhật ký và tài liệu vận hành trong cùng thay đổi.

## Hạn mức và dữ liệu

- Khách không gọi AI; tạo từ mẫu không tính lượt. Tài khoản đã xác minh được tối đa **15 lượt AI/ngày theo UTC**. Giữ chỗ trong PostgreSQL qua thao tác nguyên tử trước khi gọi nhà cung cấp; hệ thống thử hoàn chỗ nếu upstream lỗi hoặc từ chối đầu ra. Tài khoản quản trị bỏ giới hạn theo tài khoản; vẫn cần trần ngân sách nhà cung cấp, giới hạn đầu vào/đầu ra và giám sát chi phí. Nếu tiến trình chết khi đang gọi, có thể cần đối soát lượt giữ chỗ.
- Dự án, lịch sử và tài nguyên lưu theo trình duyệt, **không** phải vault hay đồng bộ theo tài khoản: người khác dùng chung hồ sơ trình duyệt có thể thấy dữ liệu. Đăng xuất không xóa tệp cục bộ. Không nhập dữ liệu học sinh, email riêng hoặc khóa. Khi gọi AI, gửi yêu cầu, phiên bản HTML trước và ngữ cảnh đã chọn; không gửi email hay token đăng nhập đến nhà cung cấp AI.
- Bản xem chỉ HTML/CSS tĩnh. Đầu ra AI được lọc trước khi hiển thị, không có scripts/mạng/form trong bản xem, iframe không có quyền same-origin. ZIP chỉ chứa mã đầu ra và README, không có biến môi trường hoặc tệp cấu hình máy chủ. Bộ lọc nhận diện một số dạng bí mật phổ biến; không thay thế kiểm tra thủ công hoặc dịch vụ secret scanning.
- Cộng đồng lưu bài và phản hồi công khai. Bài ẩn không được API public trả về; không trộn bài mẫu vào feed thật. Trước khi mời học sinh hoặc mở đăng ký đại trà, bổ sung chặn người dùng, báo cáo phản hồi, xử lý/xóa dữ liệu tài khoản, quy trình tiếp nhận khiếu nại và nhân sự kiểm duyệt. Cần kiểm thử đa tài khoản, kiểm tra đồng thời hạn mức, đặt ngưỡng ngân sách, chống spam đăng ký và xác minh dữ liệu trên môi trường Vercel/Supabase thực.

## Kiểm tra

`npm test` kiểm tra nguồn mẫu, cấu hình API không lộ bí mật khi offline, lọc HTML/CSS và bản mẫu cục bộ. `npm run build` kiểm tra bundle. Smoke test Chromium được chạy cho landing, Blueprint → Work space, preview trong iframe, Checks, ZIP, khôi phục, mẫu, cổng admin, màn hình hẹp và giao diện tối. Chưa thử gọi AI thật, gửi email hoặc viết vào DB production.
