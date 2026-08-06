# CHECKLIST TEST BÁO CÁO DEMO VOIP (IUH)

Dành cho sinh viên mang theo khi thực hành hoặc báo cáo giảng viên.

## 📋 BẢNG THÔNG TIN HỆ THỐNG VOIP

- **IP Tổng đài (Ubuntu 22.04)**: `192.168.1.100` (Card NAT) / `10.45.80.XXX` (Card Bridged điện thoại)
- **Extension 101**: Giám đốc (Win 7 - Máy 1) - Pass: `123456`
- **Extension 102**: Phòng Kinh Doanh (Win 7 - Máy 2) - Pass: `123456`
- **Extension 103**: Điện thoại Di động (App Sipnetic/Linphone) - Pass: `123456`
- **Ext 600**: Số Gọi Nhóm (Ring Group)
- **Ext 100**: Số Tổng đài IVR (Lời chào tự động)

---

## 🚀 CHECKLIST 6 YÊU CẦU DEMO

- [ ] **Yêu cầu 1: Gọi nhóm (Ring Group)**
  - Thao tác: Từ bất kỳ máy nào (101/102/103), bấm gọi `600`.
  - Đánh giá: Cả máy Win7 (`101`, `102`) và Điện thoại (`103`) đồng thời đổ chuông. Máy nào nhấc trước sẽ đàm thoại.

- [ ] **Yêu cầu 2: Gọi di động**
  - Thao tác: Bấm gọi `103` từ Win7 (101 hoặc 102).
  - Đánh giá: App Sipnetic/Linphone trên điện thoại di động reo chuông nổi màn hình cuộc gọi, nhấc máy đàm thoại 2 chiều rõ tiếng.

- [ ] **Yêu cầu 3: Nhắn tin (SIP Messaging)**
  - Thao tác: Mở tab Message trên MicroSIP (101) gửi tin nhắn tới `103`.
  - Đánh giá: App trên điện thoại di động (`103`) nhận tin nhắn hiển thị đúng nội dung.

- [ ] **Yêu cầu 4: Chặn cuộc gọi (Blacklist / Phân quyền)**
  - Thao tác: 
    + **Lượt 1**: Từ Giám đốc (`101`) gọi Nhân viên (`102` hoặc `103`) -> Cuộc gọi thành công.
    + **Lượt 2**: Từ Nhân viên (`102` hoặc `103`) gọi Giám đốc (`101`) -> Cuộc gọi bị **CHẶN** lập tức (phát thông báo `ss-noservice`).
  - Đánh giá: Phân quyền cuộc gọi đúng 100% theo yêu cầu đề bài.

- [ ] **Yêu cầu 5: Gửi Gmail cuộc gọi nhỡ (Voicemail to Email)**
  - Thao tác: Gọi số `100` (Tổng đài IVR) -> Bấm phím `1` chuyển sang Giám đốc (`101`). Máy 101 KHÔNG nghe máy. Sau 20s tự chuyển sang Hòm thư thoại (Voicemail). Nói 1 đoạn rồi cúp máy.
  - Đánh giá: Asterisk tự động gửi Email báo cuộc gọi nhỡ + file ghi âm `.wav` về Gmail đã cấu hình.

- [ ] **Yêu cầu 6: Gọi tổng đài IVR (Lời chào tự động)**
  - Thao tác: Bấm gọi số `100`.
  - Đánh giá: Nghe lời chào tự động. Bấm phím `1` chuyển đến Giám đốc (`101`), bấm phím `2` chuyển đến Phòng KD (`102`).

