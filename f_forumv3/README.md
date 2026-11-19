# F‑FORUM v3

F‑FORUM giữ trang giới thiệu hiện tại tại `/`. Phần mới cho người chưa biết code, thành viên CLB và nhóm nhỏ bắt đầu từ `/home`: viết yêu cầu, xem thử một website tĩnh, đọc thay đổi và tải mã nguồn. Ứng dụng này không dùng máy chủ hoặc dữ liệu của F‑FORUM cũ.

## Chạy thử

```sh
cd f_forumv3
npm ci
npm run dev
```

Mở `/home` để vào ứng dụng mới. Phiên khách xem được kho mẫu, thử Prompt Blueprint, tạo và sửa phiên cục bộ, xem bản HTML/CSS và xuất ZIP mà không gọi AI. Phiên đã đăng nhập có thể dùng AI khi cấu hình máy chủ hoàn tất; tài khoản vận hành được chỉ định ở máy chủ và mở trang riêng `/admin`.

```sh
npm test
npm run build
```

- [Bố trí giao diện và nguồn mẫu](docs/DESIGN.md)
- [Triển khai, dữ liệu và điều kiện phát hành](docs/DEPLOYMENT.md)
- [Nhật ký thay đổi](CHANGELOG.md)

## Phạm vi hiện tại

| Mục | Có trong bản này | Chưa có |
| --- | --- | --- |
| Landing | Mã trang cũ, CTA nối sang Studio | Không sửa hoặc thay bản phát hành cũ |
| Home | 8 tác vụ nhanh, Prompt Blueprint, dự án gần đây, điểm tin | Không gửi prompt khi chỉ chọn mẫu |
| Explore | 8 nhóm, tìm và lọc tag, mẫu xem được, nguồn/quyền sử dụng, lưu và gắn vào dự án | Không đồng bộ toàn kho; không sao chép mã ThreeUI Pro |
| Work space | 3 cột, lịch sử cục bộ, AI qua máy chủ nếu đã bật, bản xem HTML/CSS, kiểm tra DOM, Diff và ZIP | Không chạy JS tùy ý, shell, build full-stack hoặc Unit test; không PiP riêng và không Git push |
| Cộng đồng | Feed, 4 nhóm, bài đăng và phản hồi, báo cáo, ẩn/hiện bài qua admin khi kết nối Supabase | Chưa có upvote, lời giải được chấp nhận, hồ sơ bàn giao có quyền riêng hoặc gắn preview công khai |
| Cài đặt | 5 mục, giao diện sáng/tối, lựa chọn Diff và xuất/xóa dữ liệu trên thiết bị | Chưa có BYOK, đồng bộ đa thiết bị, tự xóa tài khoản hoặc connector GitHub |
