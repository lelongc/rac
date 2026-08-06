# CHECKLIST TEST BÁO CÁO DEMO VOIP (IUH)

Dành cho sinh viên mang theo khi thực hành hoặc báo cáo giảng viên.

## 📋 BẢNG THÔNG TIN HỆ THỐNG VOIP

- **IP Tổng đài (Ubuntu 22.04)**: `192.168.1.100` (Cần đổi theo IP thực tế)
- **Extension 101**: Giám đốc (Win 7 - Máy 1) - Pass: `123456`
- **Extension 102**: Phòng Kinh Doanh (Win 7 - Máy 2) - Pass: `123456`
- **Extension 103**: Điện thoại Di động - Pass: `123456`
- **Ext 600**: Số Gọi Nhóm (Ring Group)
- **Ext 100**: Số Tổng đài IVR (Lời chào tự động)

---

## 🚀 CHECKLIST 6 YÊU CẦU DEMO

- [ ] **Yêu cầu 1: Gọi nhóm (Ring Group)**
  - Thao tác: Bấm gọi `600` từ máy 101.
  - Đánh giá: Máy 102 và 103 cùng đổ chuông.

- [ ] **Yêu cầu 2: Gọi di động**
  - Thao tác: Bấm gọi `103` từ Win7.
  - Đánh giá: App Zoiper trên điện thoại di động reo chuông và đàm thoại rõ tiếng.

- [ ] **Yêu cầu 3: Nhắn tin (SIP Messaging)**
  - Thao tác: Mở tab Message trên MicroSIP gửi tin nhắn tới `103`.
  - Đánh giá: App Zoiper nhận tin nhắn hiển thị đúng nội dung.

- [ ] **Yêu cầu 4: Chặn cuộc gọi (Blacklist)**
  - Thao tác: Lấy máy 102 gọi 101.
  - Đánh giá: Cuộc gọi bị chặn ngắt kết nối lập tức (báo busy/noservice). Giám đốc (101) gọi 102 vẫn bình thường.

- [ ] **Yêu cầu 5: Gửi về Gmail cuộc gọi nhỡ**
  - Thao tác: Gọi 101 không ai bắt máy -> Để lại nhắn thoại qua Voicemail.
  - Đánh giá: Asterisk tự động gửi mail báo cuộc gọi nhỡ + file đính kèm `.wav` về Gmail.

- [ ] **Yêu cầu 6: Gọi tổng đài IVR**
  - Thao tác: Gọi `100`.
  - Đánh giá: Phản hồi lời chào tự động. Bấm phím 1 chuyển đến Giám đốc (101), bấm phím 2 chuyển đến Phòng KD (102).
