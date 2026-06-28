# HƯỚNG DẪN CHI TIẾT THI GIỮA KÌ - ĐA PHƯƠNG TIỆN

## LAB 1: CƠ BẢN VỀ ĐA PHƯƠNG TIỆN

### 1. Các định dạng file phổ biến

#### Hình ảnh:

- **JPEG/JPG**: Nén có mất dữ liệu, phù hợp ảnh màu
- **PNG**: Nén không mất dữ liệu, hỗ trợ trong suốt
- **GIF**: Hỗ trợ animation, 256 màu
- **BMP**: Không nén, dung lượng lớn
- **TIFF**: Chất lượng cao, dùng in ấn

#### Video:

- **MP4**: Phổ biến nhất, tương thích tốt
- **AVI**: Định dạng cũ, dung lượng lớn
- **MOV**: Apple QuickTime
- **WMV**: Windows Media Video
- **FLV**: Flash Video

#### Audio:

- **MP3**: Nén có mất dữ liệu, phổ biến
- **WAV**: Không nén, chất lượng cao
- **AAC**: Nén tốt hơn MP3
- **FLAC**: Nén không mất dữ liệu
- **OGG**: Mã nguồn mở

### 2. Tính toán dung lượng file

#### Công thức tính dung lượng ảnh:

```
Dung lượng = Chiều rộng × Chiều cao × Số bit/pixel ÷ 8
```

**Ví dụ**: Ảnh 1920×1080, 24-bit:

```
1920 × 1080 × 24 ÷ 8 = 6,220,800 bytes ≈ 6.2 MB
```

#### Công thức tính dung lượng video:

```
Dung lượng = Bitrate × Thời gian ÷ 8
```

**Ví dụ**: Video 5 phút, bitrate 2 Mbps:

```
2,000,000 × 300 ÷ 8 = 75,000,000 bytes = 75 MB
```

#### Công thức tính dung lượng audio:

```
Dung lượng = Sample rate × Bit depth × Channels × Thời gian ÷ 8
```

**Ví dụ**: Audio 3 phút, 44.1kHz, 16-bit, stereo:

```
44,100 × 16 × 2 × 180 ÷ 8 = 31,752,000 bytes ≈ 31.75 MB
```

### 3. Chuyển đổi đơn vị

#### Đơn vị dung lượng:

- 1 KB = 1,024 bytes
- 1 MB = 1,024 KB = 1,048,576 bytes
- 1 GB = 1,024 MB = 1,073,741,824 bytes

#### Đơn vị tần số:

- 1 kHz = 1,000 Hz
- 1 MHz = 1,000 kHz = 1,000,000 Hz

### 4. Thông số kỹ thuật quan trọng

#### Hình ảnh:

- **Resolution**: 72 DPI (web), 300 DPI (in)
- **Color depth**: 1-bit (đen trắng), 8-bit (256 màu), 24-bit (16 triệu màu)
- **Aspect ratio**: 4:3, 16:9, 16:10

#### Video:

- **Frame rate**: 24 fps (phim), 30 fps (TV), 60 fps (gaming)
- **Resolution**: HD (1280×720), Full HD (1920×1080), 4K (3840×2160)
- **Bitrate**: 1-5 Mbps (HD), 5-25 Mbps (4K)

#### Audio:

- **Sample rate**: 44.1 kHz (CD), 48 kHz (video), 96 kHz (studio)
- **Bit depth**: 16-bit (CD), 24-bit (studio), 32-bit (professional)

## LAB 2: XỬ LÝ VÀ CHỈNH SỬA ĐA PHƯƠNG TIỆN

### 1. Các thao tác cơ bản với hình ảnh

#### Resize (Thay đổi kích thước):

- **Maintain aspect ratio**: Giữ tỷ lệ khung hình
- **Interpolation methods**:
  - Nearest neighbor (nhanh, chất lượng thấp)
  - Bilinear (cân bằng)
  - Bicubic (chậm, chất lượng cao)

#### Crop (Cắt ảnh):

- Xác định vùng cần giữ lại
- Loại bỏ phần không cần thiết
- Thay đổi composition

#### Color adjustment:

- **Brightness**: Độ sáng (+/- 100)
- **Contrast**: Độ tương phản (+/- 100)
- **Saturation**: Độ bão hòa màu sắc
- **Hue**: Sắc độ màu

### 2. Filters và Effects

#### Blur filters:

- **Gaussian Blur**: Làm mờ tự nhiên
- **Motion Blur**: Mô phỏng chuyển động
- **Radial Blur**: Làm mờ xoay tròn

#### Sharpen filters:

- **Unsharp Mask**: Tăng độ sắc nét
- **Smart Sharpen**: Tự động tối ưu

#### Noise filters:

- **Add Noise**: Thêm nhiễu
- **Reduce Noise**: Giảm nhiễu

### 3. Layers và Blending modes

#### Layer types:

- **Background**: Lớp nền
- **Normal**: Lớp thường
- **Adjustment**: Lớp điều chỉnh
- **Text**: Lớp text

#### Blending modes:

- **Normal**: Bình thường
- **Multiply**: Nhân
- **Screen**: Sàng lọc
- **Overlay**: Phủ lên
- **Soft Light**: Ánh sáng mềm
- **Hard Light**: Ánh sáng cứng

### 4. Video editing cơ bản

#### Timeline operations:

- **Cut**: Cắt clip
- **Split**: Tách clip
- **Trim**: Cắt đầu/cuối
- **Extend**: Kéo dài

#### Transitions:

- **Cut**: Chuyển cảnh đột ngột
- **Fade**: Mờ dần
- **Dissolve**: Hoà tan
- **Wipe**: Quét

#### Color correction:

- **White Balance**: Cân bằng trắng
- **Exposure**: Độ phơi sáng
- **Highlights/Shadows**: Vùng sáng/tối
- **Color Grading**: Điều màu

### 5. Audio editing

#### Basic operations:

- **Cut/Copy/Paste**: Cắt/Copy/Dán
- **Fade In/Out**: Mờ dần vào/ra
- **Normalize**: Chuẩn hoá âm lượng
- **Amplify**: Khuếch đại

#### Effects:

- **Reverb**: Tiếng vọng
- **Echo**: Tiếng dội
- **EQ**: Chỉnh âm
- **Compressor**: Nén dynamic

### 6. Export settings

#### Image export:

- **JPEG**: Quality 80-90% cho web
- **PNG**: Lossless cho graphics
- **TIFF**: Uncompressed cho print

#### Video export:

- **H.264**: Tương thích tốt
- **Bitrate**: 2-10 Mbps tuỳ quality
- **Resolution**: Match source hoặc downscale

#### Audio export:

- **MP3**: 128-320 kbps
- **WAV**: 44.1kHz/16-bit minimum
- **AAC**: Tối ưu cho video
