# Thiết kế và bố trí thông tin

Trang giới thiệu cũ giữ bố cục, nội dung, màu sắc và hiệu ứng theo `f-forum@5b9d1cbd13262122a313e2896db6019764f3bfcd`. Phiên bản này chỉ nối hành động đến các route mới và thay liên kết email quản trị bằng địa chỉ công khai cấu hình riêng; nếu không cấu hình thì không hiển thị hành động email. Không nhập mã xác thực, dữ liệu, tên miền hay định danh riêng của hệ thống cũ.

## Các màn hình

| Route | Thứ tự thông tin | Chi tiết tương tác |
| --- | --- | --- |
| `/home` | Chỉ dấu trang → lời mời tạo web và composer → tác vụ nhanh → dải dự án → giới thiệu → thư viện/thảo luận | Tác vụ nhanh điền một bản nháp và có hai câu làm rõ. Gửi từ Home chỉ chuyển bản nháp; Work space mới quyết định có gọi AI không. |
| `/explore` | Tên khu → dock chọn kho, tìm, lọc → danh sách tuyến tính hoặc sân khấu tách đôi | Bên trái chọn mẫu; bên phải giữ nội dung và xem thử. Mẫu có mã, ảnh minh họa và metadata dùng nhãn khác nhau. |
| `/workspace` | Thông tin phiên và xuất → lịch sử, nội dung, kiểm tra | Màn hình lớn có 3 vùng. Màn hình hẹp chuyển vùng bằng nút. Lưu trữ có thể khôi phục; xóa phải xác nhận. Preview có kích thước desktop/mobile và toàn màn hình, sử dụng iframe sandbox. |
| `/community` | Tìm, viết bài, lọc 4 chủ đề → danh sách → nội dung và phản hồi | Bài mẫu luôn ghi rõ. Không có DM. Đăng công khai yêu cầu đăng nhập. Báo cáo có lý do và không công khai người báo cáo. |
| `/settings` | Danh sách 5 mục → nội dung mục đã chọn | Giải thích mục nào chỉ lưu trên thiết bị; chuyển chủ đề, Diff và cỡ chữ có tác động thật. |
| `/admin` | Chặn truy cập khi chưa xác nhận quyền → hàng đợi báo cáo | Làm việc ở một route riêng; API xác minh UUID từ phiên, không dựa vào trình duyệt để phân quyền. |

## Nguồn và chuyển thể

Đường dẫn dưới đây tính từ gốc `SOURCEOFKNOWLEDGFORAI`. Giấy phép và nguồn upstream xem thêm `NOTICE.md` của kho.

- **Navbar & prompt**: bố trí logo, links và cụm tài khoản lấy cấu trúc navbar của [`LunaNavbar`](../../sources/pinui/blocx/luna-hero/LunaNavbar.tsx), kết hợp hover bừng sáng của [`Inner-Glow Hover Links`](../../sources/codefronts/navigation/css-liquid-glass-navbars/inner-glow-hover-links.md). Composer dùng CSS registry [`Prompt Composer`](../../sources/pinui/registry/prompt-composer/) và chuyển thể khu quick actions thành các tác vụ có thật. Không mang theo nút voice demo hoặc model giả.
- **Dấu hiệu nhận diện**: chuyển thể hình vuông và hai phần cung từ mục logo của [`Velia`](../../sources/motionsites/prompts/editorial/velia.md). Đổi tỉ lệ, vị trí các mảnh và màu theo F‑FORUM. Chuyển động chỉ chạy khi tạo bản xem. Không lấy ảnh hay video CDN từ prompt.
- **Sân khấu Home**: phối cảnh theo brief [`Isometric Motion Grid`](../../sources/threeui/items/three-js/isometric-motion-grid.md). Hình khối xây từ mẫu đẳng cự [`#202`](../../sources/lucianlabs/demos/animation/202-iso-data-blocks.html); khung code tham chiếu [`Classic Mac System 7 Window Chrome`](../../sources/codefronts/design-styles/css-retro-designs/classic-mac-system-7-window-chrome.md). Đây là SVG/CSS, không tải mã ThreeUI Pro và không cần WebGL.
- **Nhịp cuộn**: chuyển thể nhịp xuất hiện ngắn của hành trình editorial `Velia`. Không thay đổi hành vi cuộn gốc; luôn có nội dung nếu observer vắng mặt. Chuyển route có fallback khi trình duyệt không hỗ trợ View Transition API. Chế độ giảm chuyển động tắt hiệu ứng.
- **Explore**: tách đôi theo nhóm layout [`Split Screen`](../../sources/codefronts/layouts/css-split-screen/); ảnh và demo chọn từ kho GitHub. Những mẫu chạy trực tiếp lấy từ registry PinUI (`Chips`, `Task Card`) và lucianLabs (`#001`, `#202`), không thay số liệu minh họa thành tuyên bố về sản phẩm. Tham chiếu giới hạn quyền sử dụng không được đóng gói dưới dạng source.
- **Work space**: lịch sử phiên tham chiếu [`Session List`](../../sources/pinui/registry/session-list/); bố cục công cụ tham chiếu nhóm [`Sidebar Layouts`](../../sources/codefronts/layouts/css-sidebar-layouts/) và luồng ba vùng trong đặc tả v2.

Nền trung tính giữ chữ dễ đọc. Tím dành cho hành động hiện tại và điểm bắt đầu; xanh lá dành cho kết quả đã kiểm tra hoặc trạng thái hoạt động thật. Gradient tập trung ở sân khấu Home. Ưu tiên thuật ngữ trực tiếp: «Bản nháp», «Xem thử», «Tạo từ mẫu cục bộ»; không dùng số tiến độ giả hoặc nhãn «đã kiểm thử» nếu chỉ đối chiếu metadata.
