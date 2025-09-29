# HƯỚNG DẪN CHI TIẾT THI LAB3-4 - XỬ LÝ ẢNH & VIDEO

## LAB 3: CƠ BẢN VỀ XỬ LÝ ẢNH

### 1. Các không gian màu (Color Spaces)

#### RGB (Red, Green, Blue):

- **Mô hình cộng**: Ánh sáng màu được cộng lại
- **Phạm vi**: Mỗi kênh 0-255 (8-bit)
- **Ứng dụng**: Màn hình, camera số
- **Công thức chuyển đổi**:

```
Gray = 0.299*R + 0.587*G + 0.114*B
```

#### HSV/HSB (Hue, Saturation, Value/Brightness):

- **Hue (Sắc độ)**: 0-360° (0-180 trong OpenCV)
- **Saturation (Độ bão hòa)**: 0-100% (0-255)
- **Value (Độ sáng)**: 0-100% (0-255)
- **Ứng dụng**: Chỉnh sửa màu sắc trực quan

#### YUV/YCrCb (Luminance + Chrominance):

- **Y (Luminance)**: Độ sáng, quan trọng cho mắt người
- **U/Cb, V/Cr**: Thông tin màu sắc
- **Ưu điểm**: Nén hiệu quả (có thể giảm chroma)
- **Ứng dụng**: Video compression, broadcast

### 2. Các thao tác cơ bản với ảnh

#### Histogram:

- **Định nghĩa**: Phân bố cường độ pixel
- **Ứng dụng**: Phân tích chất lượng ảnh
- **Histogram Equalization**: Cân bằng độ tương phản

#### Point Operations:

```python
# Negative
new_pixel = 255 - old_pixel

# Thresholding
new_pixel = 255 if old_pixel > threshold else 0

# Contrast Stretching
new_pixel = (old_pixel - min_val) * 255 / (max_val - min_val)

# Gamma Correction
new_pixel = 255 * (old_pixel/255)^gamma
```

#### Geometric Transforms:

- **Translation**: Dịch chuyển ảnh
- **Rotation**: Xoay ảnh
- **Scaling**: Phóng to/thu nhỏ
- **Shearing**: Nghiêng ảnh
- **Affine Transform**: Kết hợp các phép biến đổi

### 3. Filtering và Enhancement

#### Spatial Filtering:

- **Mean Filter**: Làm mờ (blur)
- **Gaussian Filter**: Làm mờ tự nhiên
- **Median Filter**: Loại bỏ nhiễu muối tiêu
- **Laplacian**: Phát hiện cạnh
- **Sobel**: Phát hiện cạnh có hướng

#### Frequency Domain:

- **FFT**: Fast Fourier Transform
- **Low-pass**: Làm mờ ảnh
- **High-pass**: Tăng cường cạnh
- **Band-pass**: Lọc dải tần

## LAB 4: VIDEO VÀ XỬ LÝ NÂNG CAO

### 1. Video Fundamentals

#### Video Properties:

- **Frame Rate**: fps (frames per second)
  - Cinema: 24 fps
  - TV PAL: 25 fps
  - TV NTSC: 29.97 fps
  - Gaming: 60+ fps
- **Resolution**: Kích thước frame
- **Color Depth**: Bits per pixel
- **Compression**: Lossy vs Lossless

#### Video Standards:

- **NTSC**: 525 lines, ~29.97 fps, 3.579545 MHz subcarrier
- **PAL**: 625 lines, 25 fps, 4.43361875 MHz subcarrier
- **Progressive vs Interlaced**: Quét tuần tự vs xen kẽ

### 2. Video Processing

#### Temporal Operations:

- **Frame Differencing**: Phát hiện chuyển động
- **Background Subtraction**: Tách đối tượng
- **Optical Flow**: Theo dõi chuyển động pixel
- **Motion Estimation**: Ước lượng vector chuyển động

#### Keyframe Detection:

```python
# Histogram difference method
def frame_difference(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
```

### 3. Interlaced Video

#### Interlacing:

- **Field 1**: Dòng chẵn (0, 2, 4, ...)
- **Field 2**: Dòng lẻ (1, 3, 5, ...)
- **Deinterlacing**: Khôi phục progressive từ interlaced

#### Chroma Subsampling:

- **4:4:4**: Full chroma (không giảm)
- **4:2:2**: Giảm chroma ngang 1/2
- **4:2:0**: Giảm chroma ngang và dọc 1/2

### 4. Image/Video Compression

#### Lossy vs Lossless:

- **Lossless**: PNG, GIF, FLAC
- **Lossy**: JPEG, MP4, MP3

#### Quality Metrics:

- **MSE**: Mean Square Error
- **PSNR**: Peak Signal-to-Noise Ratio

```
PSNR = 20 * log10(MAX_VAL) - 10 * log10(MSE)
```

#### JPEG Compression:

- **DCT**: Discrete Cosine Transform
- **Quantization**: Giảm độ chính xác
- **Huffman Coding**: Mã hóa entropy

## CÁC CÔNG THỨC QUAN TRỌNG

### 1. Chuyển đổi Color Space

```python
# RGB to Grayscale
Gray = 0.299*R + 0.587*G + 0.114*B

# RGB to YUV
Y  = 0.299*R + 0.587*G + 0.114*B
U  = -0.169*R - 0.331*G + 0.5*B + 128
V  = 0.5*R - 0.419*G - 0.081*B + 128
```

### 2. Image Quality Metrics

```python
# Mean Square Error
MSE = sum((I1 - I2)^2) / (M * N)

# Peak Signal-to-Noise Ratio
PSNR = 10 * log10((MAX_PIXEL_VALUE)^2 / MSE)
```

### 3. Geometric Transforms

```python
# Translation Matrix
T = [[1, 0, tx],
     [0, 1, ty]]

# Rotation Matrix
R = [[cos(θ), -sin(θ)],
     [sin(θ),  cos(θ)]]

# Scaling Matrix
S = [[sx, 0 ],
     [0,  sy]]
```

### 4. Convolution Kernels

```python
# Gaussian Blur (3x3)
gaussian = [[1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]] / 16

# Edge Detection (Sobel X)
sobel_x = [[-1, 0, 1],
           [-2, 0, 2],
           [-1, 0, 1]]

# Sharpening
sharpen = [[ 0, -1,  0],
           [-1,  5, -1],
           [ 0, -1,  0]]
```

## THÔNG SỐ CHUẨN

### Video Resolutions:

- **QCIF**: 176×144
- **CIF**: 352×288
- **VGA**: 640×480
- **SVGA**: 800×600
- **HD**: 1280×720
- **Full HD**: 1920×1080
- **4K UHD**: 3840×2160

### Image Formats:

| Format | Type         | Best Use               | Compression |
| ------ | ------------ | ---------------------- | ----------- |
| PNG    | Lossless     | Graphics, transparency | LZ77        |
| JPEG   | Lossy        | Photos                 | DCT         |
| GIF    | Indexed      | Simple animations      | LZW         |
| BMP    | Uncompressed | Raw data               | None        |
| TIFF   | Flexible     | Professional           | Various     |

### Video Codecs:

- **H.264/AVC**: Phổ biến, tương thích tốt
- **H.265/HEVC**: Nén tốt hơn H.264
- **VP9**: Google, mã nguồn mở
- **AV1**: Thế hệ mới, miễn phí royalty

## KỸ THUẬT XỬ LÝ NÂNG CAO

### 1. Morphological Operations:

- **Erosion**: Thu nhỏ đối tượng
- **Dilation**: Mở rộng đối tượng
- **Opening**: Erosion + Dilation
- **Closing**: Dilation + Erosion

### 2. Feature Detection:

- **Corner Detection**: Harris, FAST
- **Edge Detection**: Canny, Laplacian
- **Blob Detection**: LoG, DoH
- **Keypoint Matching**: SIFT, SURF, ORB

### 3. Image Segmentation:

- **Thresholding**: Global, Adaptive, Otsu
- **Region Growing**: Mở rộng vùng
- **Watershed**: Phân chia lưu vực
- **Graph Cut**: Cắt đồ thị

### 4. Motion Analysis:

- **Optical Flow**: Lucas-Kanade, Horn-Schunck
- **Background Modeling**: GMM, MOG
- **Object Tracking**: Kalman Filter, Particle Filter

## TROUBLESHOOTING COMMON ISSUES

### OpenCV Issues:

```python
# Check OpenCV installation
import cv2
print(cv2.__version__)

# Color conversion BGR vs RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
```

### PIL/Pillow Issues:

```python
# Convert between PIL and NumPy
pil_img = Image.fromarray(numpy_array)
numpy_array = np.array(pil_img)
```

### Performance Tips:

- Use appropriate data types (uint8 for images)
- Vectorize operations with NumPy
- Use GPU acceleration if available
- Optimize memory usage for large images

## EXAM PREPARATION CHECKLIST

### ✅ Theory Knowledge:

- [ ] Color space conversions
- [ ] Image enhancement techniques
- [ ] Video standards (NTSC/PAL)
- [ ] Compression principles
- [ ] Quality metrics (PSNR, MSE)

### ✅ Practical Skills:

- [ ] OpenCV basic operations
- [ ] PIL/Pillow image manipulation
- [ ] Matplotlib visualization
- [ ] Video file processing
- [ ] Filter implementation

### ✅ Code Templates:

- [ ] Image I/O operations
- [ ] Color space conversions
- [ ] Geometric transformations
- [ ] Filtering operations
- [ ] Video processing loops

---

**Lưu ý quan trọng cho thi:**

1. **Import libraries** đúng thứ tự
2. **Check file paths** trước khi chạy code
3. **Handle exceptions** cho file I/O
4. **Verify image dimensions** và data types
5. **Test với sample data** trước khi nộp
