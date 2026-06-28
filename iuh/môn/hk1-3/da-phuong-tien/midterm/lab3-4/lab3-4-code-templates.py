# -*- coding: utf-8 -*-
"""
CODE TEMPLATES HOÀN CHỈNH CHO THI LAB3-4
Author: Lê Thành Long
Date: 2025

MỤC LỤC NHANH THEO ĐỀ BÀI THI:
====================================

📋 DẠNG ĐỀ: "Đọc ảnh và hiển thị thông tin"
   → Copy: Section 2A + 2B (Đọc/Ghi ảnh)
   
📋 DẠNG ĐỀ: "Chuyển đổi RGB sang Grayscale/HSV/YUV" 
   → Copy: Section 3 (Color Space Conversions)
   
📋 DẠNG ĐỀ: "Điều chỉnh độ sáng, tương phản, gamma"
   → Copy: Section 4 (Image Enhancement)
   
📋 DẠNG ĐỀ: "Xoay, lật, resize, dịch chuyển ảnh"
   → Copy: Section 5 (Geometric Transforms)
   
📋 DẠNG ĐỀ: "Làm mờ, phát hiện cạnh, lọc nhiễu"
   → Copy: Section 6 (Filtering & Convolution)
   
📋 DẠNG ĐỀ: "Đọc video, trích xuất frame, keyframes"
   → Copy: Section 7 (Video Processing)
   
📋 DẠNG ĐỀ: "Tính MSE, PSNR, so sánh chất lượng"
   → Copy: Section 8 (Quality Metrics)
   
📋 DẠNG ĐỀ: "Chroma subsampling 4:4:4, 4:2:2, 4:2:0"
   → Copy: Section 7C (chroma_subsample function)
   
📋 DẠNG ĐỀ: "Interlacing/Deinterlacing video"
   → Copy: Section 7B (simulate_interlacing function)
   
📋 DẠNG ĐỀ: "Bài tổng hợp xử lý ảnh hoàn chỉnh"
   → Copy: Section 10A (complete_image_processing_example)
   
📋 DẠNG ĐỀ: "Bài tổng hợp xử lý video hoàn chỉnh"  
   → Copy: Section 10B (complete_video_processing_example)

IMPORTS CẦN THIẾT CHO MỌI BÀI:
=============================
Section 1: Setup & Imports (Copy vào đầu mọi file)

TÌM NHANH THEO TỪ KHÓA:
======================
- "đọc ảnh" → Section 2A: read_image_*
- "lưu ảnh" → Section 2B: save_image_*  
- "grayscale" → Section 3: rgb_to_grayscale
- "RGB to HSV" → Section 3: rgb_to_hsv
- "RGB to YUV" → Section 3: rgb_to_yuv
- "brightness" → Section 4: adjust_brightness_contrast
- "contrast" → Section 4: adjust_brightness_contrast
- "histogram" → Section 4: histogram_equalization
- "gamma" → Section 4: gamma_correction
- "threshold" → Section 4: apply_threshold
- "xoay" → Section 5: rotate_image
- "lật" → Section 5: flip_image
- "resize" → Section 5: resize_image
- "dịch chuyển" → Section 5: translate_image
- "blur" → Section 6: apply_gaussian_blur
- "canny" → Section 6: detect_edges_canny
- "sobel" → Section 6: apply_sobel_filter
- "video properties" → Section 2C: read_video_properties
- "keyframe" → Section 7A: extract_keyframes
- "interlace" → Section 7B: simulate_interlacing
- "chroma" → Section 7C: chroma_subsample
- "MSE" → Section 8: calculate_mse
- "PSNR" → Section 8: calculate_psnr
"""

# =============================================================================
# SECTION 1: SETUP & IMPORTS - COPY VÀO ĐẦU MỌI BÀI
# =============================================================================

# Standard imports for all image/video processing
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# PIL/Pillow for image processing
try:
    from PIL import Image, ImageOps, ImageEnhance, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    print("PIL/Pillow not available")
    PIL_AVAILABLE = False

# OpenCV for computer vision
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    print("OpenCV not available")
    CV2_AVAILABLE = False

# Helper function to check file exists
def check_file_exists(filepath):
    """Use this to validate file paths"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return True

# Helper function to create output directory
def ensure_output_dir(dirname="outputs"):
    """Use this to create output folder"""
    Path(dirname).mkdir(exist_ok=True)
    return dirname

# =============================================================================
# SECTION 2A: ĐỌC ẢNH - DÙNG KHI ĐỀ YÊU CẦU "Đọc ảnh và hiển thị thông tin"
# =============================================================================

def read_image_pil(filepath):
    """🎯 Đọc ảnh bằng PIL - trả về PIL Image
    📝 Dùng khi: Đề yêu cầu đọc ảnh PNG/JPEG/TIFF
    """
    check_file_exists(filepath)
    return Image.open(filepath)

def read_image_cv2_rgb(filepath):
    """🎯 Đọc ảnh bằng OpenCV và chuyển sang RGB  
    📝 Dùng khi: Cần OpenCV functions nhưng muốn RGB color order
    """
    check_file_exists(filepath)
    img_bgr = cv2.imread(filepath)
    if img_bgr is None:
        raise ValueError(f"Cannot read image: {filepath}")
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

def read_image_as_array(filepath):
    """🎯 Đọc ảnh thành numpy array
    📝 Dùng khi: Cần xử lý ảnh bằng NumPy operations
    """
    if PIL_AVAILABLE:
        pil_img = Image.open(filepath)
        return np.array(pil_img)
    elif CV2_AVAILABLE:
        return read_image_cv2_rgb(filepath)
    else:
        raise RuntimeError("No image library available")

def get_image_info(filepath):
    """🎯 Lấy thông tin chi tiết ảnh
    📝 Dùng khi: Đề yêu cầu hiển thị kích thước, format, channels
    """
    img = read_image_pil(filepath)
    array = np.array(img)
    
    info = {
        'filename': os.path.basename(filepath),
        'format': img.format,
        'mode': img.mode,
        'size': img.size,  # (width, height)
        'width': img.size[0],
        'height': img.size[1],
        'channels': 1 if array.ndim == 2 else array.shape[2],
        'dtype': str(array.dtype),
        'file_size_bytes': os.path.getsize(filepath)
    }
    
    return info, img, array

# =============================================================================
# SECTION 2B: GHI ẢNH - DÙNG KHI CẦN LƯU KẾT QUẢ
# =============================================================================

def save_image_pil(image, filepath, quality=95):
    """🎯 Lưu ảnh bằng PIL với quality setting
    📝 Dùng khi: Cần control JPEG quality hoặc lưu PNG
    """
    if isinstance(image, np.ndarray):
        if image.dtype != np.uint8:
            image = np.clip(image, 0, 255).astype(np.uint8)
        image = Image.fromarray(image)
    
    ensure_output_dir(os.path.dirname(filepath))
    
    if filepath.lower().endswith('.jpg') or filepath.lower().endswith('.jpeg'):
        image.save(filepath, 'JPEG', quality=quality)
    else:
        image.save(filepath)

def save_image_cv2(image_rgb, filepath):
    """🎯 Lưu ảnh bằng OpenCV
    📝 Dùng khi: Working với OpenCV functions
    """
    if isinstance(image_rgb, Image.Image):
        image_rgb = np.array(image_rgb)
    
    ensure_output_dir(os.path.dirname(filepath))
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(filepath, image_bgr)

# =============================================================================
# SECTION 2C: VIDEO OPERATIONS - DÙNG KHI ĐỀ VỀ VIDEO
# =============================================================================

def read_video_properties(video_path):
    """🎯 Đọc thông tin video chi tiết
    📝 Dùng khi: Đề yêu cầu hiển thị fps, resolution, duration, codec
    """
    check_file_exists(video_path)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video: {video_path}")
    
    properties = {
        'filename': os.path.basename(video_path),
        'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': cap.get(cv2.CAP_PROP_FPS),
        'frame_count': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        'duration_seconds': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / cap.get(cv2.CAP_PROP_FPS),
        'codec_fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
        'file_size_bytes': os.path.getsize(video_path)
    }
    
    cap.release()
    return properties

def extract_frames_from_video(video_path, max_frames=10, save_frames=True, output_dir="frames"):
    """🎯 Trích xuất frames từ video
    📝 Dùng khi: Đề yêu cầu lấy frame từ video để xử lý
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0
    
    if save_frames:
        ensure_output_dir(output_dir)
    
    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame_rgb)
        
        if save_frames:
            frame_path = f"{output_dir}/frame_{frame_count:04d}.jpg"
            cv2.imwrite(frame_path, frame)
        
        frame_count += 1
    
    cap.release()
    return frames

# =============================================================================
# SECTION 3: COLOR SPACE CONVERSIONS - DÙNG KHI ĐỀ YÊU CẦU CHUYỂN ĐỔI MÀU
# =============================================================================

def rgb_to_grayscale(rgb_image):
    """🎯 Chuyển RGB sang grayscale bằng công thức chuẩn
    📝 Dùng khi: Đề yêu cầu "chuyển ảnh màu sang xám"
    🔢 Công thức: Gray = 0.299*R + 0.587*G + 0.114*B
    """
    if isinstance(rgb_image, Image.Image):
        return rgb_image.convert('L')
    else:
        # Numpy array
        if rgb_image.ndim == 3:
            return np.dot(rgb_image[...,:3], [0.299, 0.587, 0.114])
        else:
            return rgb_image

def rgb_to_hsv(rgb_image):
    """🎯 Chuyển RGB sang HSV
    📝 Dùng khi: Đề yêu cầu "chuyển RGB sang HSV" hoặc "tách Hue/Saturation/Value"
    """
    if CV2_AVAILABLE:
        if isinstance(rgb_image, Image.Image):
            rgb_image = np.array(rgb_image)
        bgr = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        return hsv
    else:
        raise RuntimeError("OpenCV required for HSV conversion")

def rgb_to_yuv(rgb_image):
    """🎯 Chuyển RGB sang YUV
    📝 Dùng khi: Đề yêu cầu "chuyển RGB sang YUV" hoặc "tách Luminance/Chrominance"
    🔢 Công thức manual: Y=0.299R+0.587G+0.114B, U=-0.169R-0.331G+0.5B+128, V=0.5R-0.419G-0.081B+128
    """
    if CV2_AVAILABLE:
        if isinstance(rgb_image, Image.Image):
            rgb_image = np.array(rgb_image)
        bgr = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        yuv = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV)
        return yuv
    else:
        # Manual conversion
        if isinstance(rgb_image, Image.Image):
            rgb_image = np.array(rgb_image)
        
        rgb = rgb_image.astype(np.float32)
        yuv = np.zeros_like(rgb)
        
        yuv[:,:,0] = 0.299 * rgb[:,:,0] + 0.587 * rgb[:,:,1] + 0.114 * rgb[:,:,2]  # Y
        yuv[:,:,1] = -0.169 * rgb[:,:,0] - 0.331 * rgb[:,:,1] + 0.5 * rgb[:,:,2] + 128  # U
        yuv[:,:,2] = 0.5 * rgb[:,:,0] - 0.419 * rgb[:,:,1] - 0.081 * rgb[:,:,2] + 128   # V
        
        return np.clip(yuv, 0, 255).astype(np.uint8)

def split_color_channels(rgb_image):
    """🎯 Tách các kênh màu riêng biệt
    📝 Dùng khi: Đề yêu cầu "tách kênh R, G, B" hoặc "hiển thị từng kênh màu"
    """
    if isinstance(rgb_image, Image.Image):
        return rgb_image.split()  # Returns R, G, B channels
    else:
        if rgb_image.ndim == 3:
            return rgb_image[:,:,0], rgb_image[:,:,1], rgb_image[:,:,2]
        else:
            return rgb_image, rgb_image, rgb_image

# =============================================================================
# SECTION 4: IMAGE ENHANCEMENT - DÙNG KHI ĐỀ YÊU CẦU CHỈNH SỬA ẢNH
# =============================================================================

def adjust_brightness_contrast(image, brightness=0, contrast=1.0):
    """🎯 Điều chỉnh độ sáng và tương phản
    📝 Dùng khi: Đề yêu cầu "điều chỉnh brightness/contrast" 
    🔢 brightness: -100 to +100, contrast: 0.5 to 2.0
    """
    if isinstance(image, Image.Image):
        # PIL method
        if brightness != 0:
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(1.0 + brightness/100.0)
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast)
        return image
    else:
        # NumPy method
        image = image.astype(np.float32)
        image = image * contrast + brightness
        return np.clip(image, 0, 255).astype(np.uint8)

def histogram_equalization(image):
    """🎯 Cân bằng histogram
    📝 Dùng khi: Đề yêu cầu "cân bằng histogram" hoặc "histogram equalization"
    """
    if isinstance(image, Image.Image):
        return ImageOps.equalize(image)
    else:
        if image.ndim == 2:
            return cv2.equalizeHist(image)
        else:
            # For color images, apply to each channel
            yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
            yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
            return cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)

def gamma_correction(image, gamma=1.0):
    """🎯 Hiệu chỉnh gamma
    📝 Dùng khi: Đề yêu cầu "gamma correction"
    🔢 gamma < 1: làm sáng, gamma > 1: làm tối
    """
    if isinstance(image, Image.Image):
        image = np.array(image)
    
    # Normalize to [0,1], apply gamma, then back to [0,255]
    normalized = image.astype(np.float32) / 255.0
    corrected = np.power(normalized, gamma)
    result = (corrected * 255).astype(np.uint8)
    
    return Image.fromarray(result) if isinstance(image, Image.Image) else result

def apply_threshold(image, threshold=128, max_value=255):
    """🎯 Áp dụng ngưỡng nhị phân
    📝 Dùng khi: Đề yêu cầu "threshold" hoặc "binarization"
    """
    if isinstance(image, Image.Image):
        image = np.array(image.convert('L'))
    
    if image.ndim > 2:
        image = rgb_to_grayscale(image)
    
    binary = np.where(image > threshold, max_value, 0).astype(np.uint8)
    return binary

# =============================================================================
# SECTION 5: GEOMETRIC TRANSFORMS - DÙNG KHI ĐỀ YÊU CẦU BIẾN ĐỔI HÌNH HỌC
# =============================================================================

def rotate_image(image, angle, expand=True):
    """🎯 Xoay ảnh với góc cho trước
    📝 Dùng khi: Đề yêu cầu "xoay ảnh" hoặc "rotate image"
    🔢 angle: độ (degree), expand=True để không crop
    """
    if isinstance(image, Image.Image):
        return image.rotate(angle, expand=expand, fillcolor='white')
    else:
        # OpenCV method
        h, w = image.shape[:2]
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        
        if expand:
            # Calculate new dimensions
            cos_val = np.abs(matrix[0, 0])
            sin_val = np.abs(matrix[0, 1])
            new_w = int((h * sin_val) + (w * cos_val))
            new_h = int((h * cos_val) + (w * sin_val))
            
            # Adjust translation
            matrix[0, 2] += (new_w / 2) - center[0]
            matrix[1, 2] += (new_h / 2) - center[1]
            
            return cv2.warpAffine(image, matrix, (new_w, new_h), 
                                borderMode=cv2.BORDER_CONSTANT, 
                                borderValue=(255, 255, 255))
        else:
            return cv2.warpAffine(image, matrix, (w, h))

def flip_image(image, direction='horizontal'):
    """🎯 Lật ảnh theo chiều ngang hoặc dọc
    📝 Dùng khi: Đề yêu cầu "lật ảnh" hoặc "flip image"
    🔢 direction: 'horizontal' hoặc 'vertical'
    """
    if isinstance(image, Image.Image):
        if direction == 'horizontal':
            return ImageOps.mirror(image)
        else:
            return ImageOps.flip(image)
    else:
        if direction == 'horizontal':
            return cv2.flip(image, 1)
        else:
            return cv2.flip(image, 0)

def resize_image(image, new_size, maintain_aspect=True):
    """🎯 Thay đổi kích thước ảnh
    📝 Dùng khi: Đề yêu cầu "resize" hoặc "scale image"
    🔢 new_size: (width, height), maintain_aspect: giữ tỷ lệ
    """
    if isinstance(image, Image.Image):
        if maintain_aspect:
            image.thumbnail(new_size, Image.Resampling.LANCZOS)
            return image
        else:
            return image.resize(new_size, Image.Resampling.LANCZOS)
    else:
        return cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)

def translate_image(image, tx, ty):
    """🎯 Dịch chuyển ảnh
    📝 Dùng khi: Đề yêu cầu "dịch chuyển" hoặc "translate image"
    🔢 tx, ty: pixel dịch chuyển theo x, y
    """
    if isinstance(image, Image.Image):
        return image.transform(image.size, Image.AFFINE, (1, 0, tx, 0, 1, ty))
    else:
        h, w = image.shape[:2]
        matrix = np.float32([[1, 0, tx], [0, 1, ty]])
        return cv2.warpAffine(image, matrix, (w, h))

# =============================================================================
# SECTION 6: FILTERING & CONVOLUTION - DÙNG KHI ĐỀ YÊU CẦU LỌC ẢNH
# =============================================================================

def apply_gaussian_blur(image, kernel_size=5, sigma=1.0):
    """🎯 Áp dụng bộ lọc Gaussian (làm mờ)
    📝 Dùng khi: Đề yêu cầu "gaussian blur" hoặc "làm mờ ảnh"
    🔢 kernel_size: 3,5,7,9... (số lẻ), sigma: độ mờ
    """
    if isinstance(image, Image.Image):
        return image.filter(ImageFilter.GaussianBlur(radius=sigma))
    else:
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

def apply_median_filter(image, kernel_size=5):
    """🎯 Áp dụng bộ lọc median (loại bỏ nhiễu muối tiêu)
    📝 Dùng khi: Đề yêu cầu "median filter" hoặc "loại bỏ nhiễu"
    """
    if isinstance(image, Image.Image):
        return image.filter(ImageFilter.MedianFilter(size=kernel_size))
    else:
        return cv2.medianBlur(image, kernel_size)

def detect_edges_canny(image, low_threshold=50, high_threshold=150):
    """🎯 Phát hiện cạnh bằng Canny
    📝 Dùng khi: Đề yêu cầu "edge detection" hoặc "phát hiện cạnh"
    🔢 low_threshold: 50, high_threshold: 150 (thường dùng)
    """
    if isinstance(image, Image.Image):
        image = np.array(image.convert('L'))
    
    if image.ndim > 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    edges = cv2.Canny(image, low_threshold, high_threshold)
    return edges

def apply_sobel_filter(image, direction='both'):
    """🎯 Áp dụng bộ lọc Sobel
    📝 Dùng khi: Đề yêu cầu "sobel filter" hoặc "gradient detection"
    🔢 direction: 'x', 'y', hoặc 'both'
    """
    if isinstance(image, Image.Image):
        image = np.array(image.convert('L'))
    
    if image.ndim > 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    if direction == 'x':
        return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    elif direction == 'y':
        return cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    else:
        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        return np.sqrt(sobel_x**2 + sobel_y**2)

# Predefined kernels for custom filtering
KERNELS = {
    'sharpen': np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
    'edge_detect': np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
    'emboss': np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
    'blur': np.ones((3, 3)) / 9
}

def apply_custom_kernel(image, kernel):
    """🎯 Áp dụng kernel tùy chỉnh
    📝 Dùng khi: Đề yêu cầu "convolution" hoặc "custom filter"
    """
    if isinstance(image, Image.Image):
        image = np.array(image)
    
    return cv2.filter2D(image, -1, kernel)

# =============================================================================
# SECTION 7A: VIDEO PROCESSING - KEYFRAMES
# =============================================================================

def extract_keyframes(video_path, threshold=0.3, output_dir="keyframes"):
    """🎯 Trích xuất keyframes dựa trên histogram difference
    📝 Dùng khi: Đề yêu cầu "keyframe extraction" hoặc "trích xuất khung hình quan trọng"
    🔢 threshold: 0.3 (cao hơn = ít keyframe hơn)
    """
    ensure_output_dir(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    prev_hist = None
    frame_count = 0
    keyframe_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Calculate histogram
        hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, None).flatten()
        
        if prev_hist is not None:
            # Calculate difference
            diff = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA)
            
            if diff > threshold:
                # Save keyframe
                filename = os.path.join(output_dir, f"keyframe_{keyframe_count:04d}.jpg")
                cv2.imwrite(filename, frame)
                keyframe_count += 1
                prev_hist = hist
        else:
            prev_hist = hist
        
        frame_count += 1
    
    cap.release()
    return keyframe_count

# =============================================================================
# SECTION 7B: INTERLACING/DEINTERLACING
# =============================================================================

def simulate_interlacing(image):
    """🎯 Mô phỏng interlacing
    📝 Dùng khi: Đề yêu cầu "interlacing" hoặc "mô phỏng quét xen kẽ"
    """
    if isinstance(image, Image.Image):
        image = np.array(image)
    
    h, w = image.shape[:2]
    
    # Create even and odd fields
    even_field = np.zeros_like(image)
    odd_field = np.zeros_like(image)
    
    even_field[0::2] = image[0::2]  # Even rows (0, 2, 4, ...)
    odd_field[1::2] = image[1::2]   # Odd rows (1, 3, 5, ...)
    
    return even_field, odd_field

def deinterlace_simple(even_field, odd_field):
    """🎯 Deinterlacing đơn giản
    📝 Dùng khi: Đề yêu cầu "deinterlacing" hoặc "ghép các field"
    """
    return even_field + odd_field

# =============================================================================
# SECTION 7C: CHROMA SUBSAMPLING
# =============================================================================

def chroma_subsample(yuv_image, mode='420'):
    """🎯 Chroma subsampling simulation
    📝 Dùng khi: Đề yêu cầu "chroma subsampling 4:4:4, 4:2:2, 4:2:0"
    🔢 mode: '444' (no subsampling), '422' (half horizontal), '420' (half both)
    """
    Y, U, V = cv2.split(yuv_image)
    h, w = Y.shape
    
    if mode == '422':
        # Subsample U and V horizontally by factor of 2
        U_sub = cv2.resize(U, (w//2, h), interpolation=cv2.INTER_AREA)
        V_sub = cv2.resize(V, (w//2, h), interpolation=cv2.INTER_AREA)
        
        # Upsample back
        U_up = cv2.resize(U_sub, (w, h), interpolation=cv2.INTER_LINEAR)
        V_up = cv2.resize(V_sub, (w, h), interpolation=cv2.INTER_LINEAR)
        
    elif mode == '420':
        # Subsample U and V both horizontally and vertically by factor of 2
        U_sub = cv2.resize(U, (w//2, h//2), interpolation=cv2.INTER_AREA)
        V_sub = cv2.resize(V, (w//2, h//2), interpolation=cv2.INTER_AREA)
        
        # Upsample back
        U_up = cv2.resize(U_sub, (w, h), interpolation=cv2.INTER_LINEAR)
        V_up = cv2.resize(V_sub, (w, h), interpolation=cv2.INTER_LINEAR)
    else:
        # 444 - no subsampling
        U_up, V_up = U, V
    
    return cv2.merge([Y, U_up, V_up])

# =============================================================================
# SECTION 8: QUALITY METRICS - DÙNG KHI CẦN TÍNH CHẤT LƯỢNG
# =============================================================================

def calculate_mse(image1, image2):
    """🎯 Tính Mean Square Error
    📝 Dùng khi: Đề yêu cầu "tính MSE" hoặc "so sánh chất lượng ảnh"
    🔢 Công thức: MSE = mean((I1 - I2)²)
    """
    if isinstance(image1, Image.Image):
        image1 = np.array(image1)
    if isinstance(image2, Image.Image):
        image2 = np.array(image2)
    
    mse = np.mean((image1.astype(np.float64) - image2.astype(np.float64)) ** 2)
    return mse

def calculate_psnr(image1, image2, max_pixel_value=255):
    """🎯 Tính Peak Signal-to-Noise Ratio
    📝 Dùng khi: Đề yêu cầu "tính PSNR" hoặc "đánh giá chất lượng nén"
    🔢 Công thức: PSNR = 20*log10(MAX) - 10*log10(MSE)
    """
    mse = calculate_mse(image1, image2)
    if mse == 0:
        return float('inf')
    
    psnr = 20 * np.log10(max_pixel_value) - 10 * np.log10(mse)
    return psnr

# =============================================================================
# SECTION 10A: COMPLETE EXAMPLE - BÀI TỔNG HỢP XỬ LÝ ẢNH
# =============================================================================

def complete_image_processing_example():
    """🎯 Template hoàn chỉnh cho bài thi xử lý ảnh
    📝 Copy toàn bộ khi: Đề yêu cầu bài tổng hợp nhiều kỹ thuật
    """
    # Input file - THAY ĐỔI THEO ĐỀ BÀI
    input_file = "sample.jpg"
    output_dir = "outputs"
    
    try:
        # 1. Đọc ảnh
        info, image, array = get_image_info(input_file)
        print("=== THÔNG TIN ẢNH ===")
        for key, value in info.items():
            print(f"{key}: {value}")
        
        # 2. Chuyển đổi color space
        gray_image = rgb_to_grayscale(image)
        hsv_image = rgb_to_hsv(array)
        yuv_image = rgb_to_yuv(array)
        
        # 3. Enhancement
        enhanced = adjust_brightness_contrast(image, brightness=20, contrast=1.2)
        equalized = histogram_equalization(gray_image)
        gamma_corrected = gamma_correction(image, gamma=0.8)
        
        # 4. Geometric transforms
        rotated = rotate_image(image, 45)
        flipped = flip_image(image, 'horizontal')
        resized = resize_image(image, (400, 300))
        
        # 5. Filtering
        blurred = apply_gaussian_blur(image, kernel_size=5)
        edges = detect_edges_canny(gray_image)
        sobel_result = apply_sobel_filter(gray_image)
        
        # 6. Save results
        ensure_output_dir(output_dir)
        save_image_pil(gray_image, f"{output_dir}/01_grayscale.png")
        save_image_pil(enhanced, f"{output_dir}/02_enhanced.jpg", quality=90)
        save_image_pil(rotated, f"{output_dir}/03_rotated.png")
        save_image_pil(blurred, f"{output_dir}/04_blurred.jpg")
        
        # 7. Display results với subplot
        plt.figure(figsize=(15, 10))
        
        images_to_show = [
            (image, 'Original'),
            (gray_image, 'Grayscale'),
            (enhanced, 'Enhanced'),
            (rotated, 'Rotated 45°'),
            (blurred, 'Gaussian Blur'),
            (edges, 'Canny Edges')
        ]
        
        for i, (img, title) in enumerate(images_to_show, 1):
            plt.subplot(2, 3, i)
            if isinstance(img, Image.Image):
                if img.mode == 'L':
                    plt.imshow(img, cmap='gray')
                else:
                    plt.imshow(img)
            else:
                if img.ndim == 2:
                    plt.imshow(img, cmap='gray')
                else:
                    plt.imshow(img)
            plt.title(title)
            plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"✅ Đã xử lý ảnh thành công!")
        print(f"📁 Kết quả lưu tại: {output_dir}/")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# =============================================================================
# SECTION 10B: COMPLETE EXAMPLE - BÀI TỔNG HỢP XỬ LÝ VIDEO  
# =============================================================================

def complete_video_processing_example():
    """🎯 Template hoàn chỉnh cho bài thi xử lý video
    📝 Copy toàn bộ khi: Đề yêu cầu bài tổng hợp video
    """
    # Input file - THAY ĐỔI THEO ĐỀ BÀI
    video_file = "sample.mp4"
    output_dir = "video_outputs"
    
    try:
        # 1. Đọc thông tin video
        props = read_video_properties(video_file)
        print("=== THÔNG TIN VIDEO ===")
        for key, value in props.items():
            print(f"{key}: {value}")
        
        # 2. Extract một vài frames
        frames = extract_frames_from_video(video_file, max_frames=5, save_frames=True, 
                                         output_dir=f"{output_dir}/frames")
        print(f"Extracted {len(frames)} frames")
        
        # 3. Extract keyframes  
        keyframe_count = extract_keyframes(video_file, threshold=0.3, 
                                         output_dir=f"{output_dir}/keyframes")
        print(f"Extracted {keyframe_count} keyframes")
        
        # 4. Xử lý frame đầu tiên
        if frames:
            first_frame = frames[0]
            
            # Các phép xử lý
            gray_frame = rgb_to_grayscale(first_frame)
            blurred_frame = apply_gaussian_blur(first_frame, kernel_size=5)
            edges_frame = detect_edges_canny(gray_frame)
            
            # Hiển thị kết quả
            plt.figure(figsize=(12, 8))
            
            frame_results = [
                (first_frame, 'Original Frame'),
                (gray_frame, 'Grayscale'),
                (blurred_frame, 'Blurred'),
                (edges_frame, 'Edges')
            ]
            
            for i, (frame, title) in enumerate(frame_results, 1):
                plt.subplot(2, 2, i)
                if isinstance(frame, np.ndarray) and frame.ndim == 2:
                    plt.imshow(frame, cmap='gray')
                else:
                    plt.imshow(frame)
                plt.title(title)
                plt.axis('off')
            
            plt.tight_layout()
            plt.show()
            
            # Lưu frame đã xử lý
            save_image_pil(gray_frame, f"{output_dir}/processed_frame_gray.png")
            save_image_pil(blurred_frame, f"{output_dir}/processed_frame_blur.jpg")
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"✅ Đã xử lý video thành công!")
        print(f"📁 Kết quả lưu tại: {output_dir}/")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# =============================================================================
# SECTION 11: QUICK TESTING & DEBUGGING
# =============================================================================

def quick_test_image_functions():
    """🎯 Test nhanh các functions để đảm bảo hoạt động
    📝 Chạy khi: Muốn kiểm tra code trước khi nộp bài
    """
    print("🧪 Testing image processing functions...")
    
    # Test với ảnh mẫu
    test_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    test_image = Image.fromarray(test_array)
    
    try:
        # Test basic functions
        gray = rgb_to_grayscale(test_image)
        enhanced = adjust_brightness_contrast(test_image, brightness=10, contrast=1.1)
        rotated = rotate_image(test_image, 30)
        blurred = apply_gaussian_blur(test_image, kernel_size=5)
        
        print("✅ All basic functions work!")
        return True
        
    except Exception as e:
        print(f"❌ Error in testing: {e}")
        return False

# =============================================================================
# MAIN FUNCTION - DEMO & TESTING
# =============================================================================

if __name__ == "__main__":
    """
    🎯 CÁCH SỬ DỤNG TRONG THI:
    
    1️⃣ Đọc đề bài
    2️⃣ Tìm dạng đề trong MỤC LỤC NHANH ở đầu file
    3️⃣ Copy section tương ứng theo hướng dẫn
    4️⃣ Thay đổi đường dẫn file theo đề bài
    5️⃣ Chạy test trước khi nộp
    
    📝 VÍ DỤ:
    - Đề: "Chuyển ảnh RGB sang grayscale" → Copy Section 3: rgb_to_grayscale
    - Đề: "Xoay ảnh 45 độ" → Copy Section 5: rotate_image  
    - Đề: "Phát hiện cạnh Canny" → Copy Section 6: detect_edges_canny
    """
    
    print("=== LAB3-4 CODE TEMPLATES READY ===")
    print("🔍 Tìm function cần thiết bằng Ctrl+F")
    print("📋 Xem MỤC LỤC NHANH ở đầu file để biết copy gì")
    
    # Test functions
    if quick_test_image_functions():
        print("🚀 Templates sẵn sàng cho kỳ thi!")
    
    # Uncomment để chạy examples
    # complete_image_processing_example()
    # complete_video_processing_example()

"""
🔍 QUICK REFERENCE - TÌM NHANH THEO TỪ KHÓA:

📸 IMAGE I/O:
- read_image_pil(filepath) → Đọc ảnh PIL
- read_image_cv2_rgb(filepath) → Đọc ảnh OpenCV  
- save_image_pil(image, filepath) → Lưu ảnh
- get_image_info(filepath) → Thông tin ảnh

🎨 COLOR CONVERSION:
- rgb_to_grayscale(image) → RGB sang xám
- rgb_to_hsv(image) → RGB sang HSV
- rgb_to_yuv(image) → RGB sang YUV
- split_color_channels(image) → Tách kênh R,G,B

✨ ENHANCEMENT:  
- adjust_brightness_contrast(image, brightness, contrast) → Sáng/tương phản
- histogram_equalization(image) → Cân bằng histogram
- gamma_correction(image, gamma) → Hiệu chỉnh gamma
- apply_threshold(image, threshold) → Ngưỡng hóa

🔄 GEOMETRIC:
- rotate_image(image, angle) → Xoay ảnh
- flip_image(image, direction) → Lật ảnh  
- resize_image(image, new_size) → Đổi kích thước
- translate_image(image, tx, ty) → Dịch chuyển

🔍 FILTERING:
- apply_gaussian_blur(image, kernel_size, sigma) → Làm mờ Gaussian
- detect_edges_canny(image, low_thresh, high_thresh) → Phát hiện cạnh Canny
- apply_sobel_filter(image, direction) → Bộ lọc Sobel
- apply_median_filter(image, kernel_size) → Lọc median

🎬 VIDEO:
- read_video_properties(video_path) → Thông tin video
- extract_frames_from_video(video_path, max_frames) → Trích frame
- extract_keyframes(video_path, threshold) → Keyframes
- simulate_interlacing(image) → Mô phỏng interlace
- chroma_subsample(yuv_image, mode) → Chroma subsampling

📊 QUALITY:
- calculate_mse(image1, image2) → Tính MSE
- calculate_psnr(image1, image2) → Tính PSNR
"""
