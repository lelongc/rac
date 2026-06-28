# -*- coding: utf-8 -*-
"""
LAB: ĐỌC ẢNH & VIDEO + HIỂN THỊ THUỘC TÍNH (Spyder)
===================================================

Nội dung
--------
1) Nhập ảnh số (*.png, *.jpg/jpeg, *.tif/tiff, ...) và hiển thị các thuộc tính liên quan.
2) Nhập một đoạn video ngắn và hiển thị các thuộc tính liên quan.

Cách chạy
---------
- Mở file này trong Spyder → Run (F5).
- Thiết lập đường dẫn ở IMAGE_PATH / VIDEO_PATH, hoặc để None để bật hộp thoại chọn file.

Yêu cầu thư viện
----------------
- Pillow (PIL), OpenCV (cv2), NumPy, Matplotlib (để hiển thị).
"""

import os, sys, math, time
from pathlib import Path
import numpy as np

# --- Cấu hình đường dẫn (sửa theo ý bạn hoặc để None để chọn bằng hộp thoại) ---
IMAGE_PATH = None   # ví dụ: r"D:/data/image01.png"
VIDEO_PATH = None   # ví dụ: r"D:/data/clip01.mp4"

# ===== Imports an toàn =====
try:
    from PIL import Image, ImageOps, ExifTags
    PIL_OK = True
except Exception as e:
    print("[WARN] PIL chưa sẵn sàng:", e)
    PIL_OK = False

try:
    import cv2
    CV2_OK = True
except Exception as e:
    print("[WARN] OpenCV (cv2) chưa sẵn sàng:", e)
    CV2_OK = False

import matplotlib.pyplot as plt

# ====== Tiện ích chung ======
def choose_file_dialog(title="Chọn file", filetypes=(("All files","*.*"),)):
    """Hộp thoại chọn file (tkinter). Trả về str hoặc None."""
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk(); root.withdraw()
        path = filedialog.askopenfilename(title=title, filetypes=filetypes)
        root.destroy()
        return path if path else None
    except Exception as e:
        print("[INFO] Không dùng được hộp thoại, fallback input():", e)
        try:
            return input("Nhập đường dẫn file: ").strip() or None
        except EOFError:
            return None

def readable_bytes(n):
    """Đổi kích thước bytes -> dạng đọc được (KB, MB, ...)"""
    if n is None:
        return "N/A"
    units = ["B","KB","MB","GB","TB"]
    i = 0
    n = float(n)
    while n >= 1024 and i < len(units)-1:
        n /= 1024.0
        i += 1
    return f"{n:.2f} {units[i]}"

# ====== PHẦN 1: ẢNH ======
def image_properties(path: str):
    """Đọc ảnh bằng PIL, trả về dict thuộc tính hữu ích."""
    info = {}
    p = Path(path)
    info["filename"] = p.name
    info["suffix"] = p.suffix.lower()
    try:
        info["filesize"] = p.stat().st_size
    except Exception:
        info["filesize"] = None

    if not PIL_OK:
        info["error"] = "PIL không khả dụng"
        return info

    with Image.open(path) as im:
        info["format"] = im.format  # PNG/JPEG/TIFF/...
        info["mode"] = im.mode      # L, RGB, RGBA, I;16, etc.
        info["size"] = im.size      # (W,H)
        info["width"], info["height"] = im.size
        # Ẩn số kênh và bit-depth sơ bộ
        try:
            arr = np.array(im)
            info["ndim"] = arr.ndim
            info["dtype"] = str(arr.dtype)
            if arr.ndim == 2:
                info["channels"] = 1
            elif arr.ndim == 3:
                info["channels"] = arr.shape[2]
            else:
                info["channels"] = "unknown"
            # bit depth / channel ước lượng từ dtype
            dtype_to_bits = {
                "uint8":8, "int8":8,
                "uint16":16, "int16":16,
                "uint32":32, "int32":32,
                "float32":32, "float64":64
            }
            info["bit_depth_per_channel"] = dtype_to_bits.get(str(arr.dtype), "unknown")
        except Exception as e:
            info["ndim"] = None
            info["dtype"] = None
            info["channels"] = None
            info["bit_depth_per_channel"] = None

        # EXIF (nếu có)
        try:
            exif = im.getexif()
            exif_dict = {}
            if exif is not None:
                for tag_id, val in exif.items():
                    tag = ExifTags.TAGS.get(tag_id, tag_id)
                    # lọc vài trường hay dùng
                    if tag in ["DateTime", "Make", "Model", "Orientation", "XResolution", "YResolution", "ResolutionUnit"]:
                        exif_dict[tag] = val
            info["exif"] = exif_dict if exif_dict else None
        except Exception:
            info["exif"] = None

    return info

def show_image(path: str):
    """Hiển thị ảnh bằng matplotlib (phù hợp Spyder)."""
    if not PIL_OK:
        print("[ERR] PIL not available.")
        return
    im = Image.open(path)
    plt.figure(figsize=(5,5))
    if im.mode == 'L':
        plt.imshow(im, cmap='gray')
    else:
        plt.imshow(im)
    plt.title(Path(path).name)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    im.close()

# ====== PHẦN 2: VIDEO ======
def video_properties(path: str):
    """Đọc video bằng OpenCV, trả về dict thuộc tính."""
    info = {}
    p = Path(path)
    info["filename"] = p.name
    info["suffix"] = p.suffix.lower()
    try:
        info["filesize"] = p.stat().st_size
    except Exception:
        info["filesize"] = None

    if not CV2_OK:
        info["error"] = "OpenCV không khả dụng"
        return info

    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        info["error"] = "Không mở được video"
        return info

    # Lấy thuộc tính
    fw = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # FOURCC
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    codec = "".join([chr((fourcc >> 8*i) & 0xFF) for i in range(4)]) if fourcc else "unknown"
    duration = n_frames / fps if fps > 0 else None

    info.update({
        "width": fw, "height": fh,
        "fps": float(fps),
        "frame_count": n_frames,
        "duration_sec": duration,
        "codec_fourcc": codec
    })

    # Ước lượng bitrate từ kích thước file (nếu có)
    if info.get("filesize") and duration:
        bitrate_bps = info["filesize"] * 8.0 / duration
        info["approx_bitrate_bps"] = bitrate_bps
    else:
        info["approx_bitrate_bps"] = None

    # Lấy 1 frame đầu để hiển thị
    ok, frame = cap.read()
    if ok:
        info["first_frame_shape"] = tuple(frame.shape)  # (H, W, C)
        # Hiển thị frame đầu
        plt.figure(figsize=(5,5))
        # OpenCV dùng BGR -> chuyển RGB để hiển thị đúng màu
        frame_rgb = frame[:, :, ::-1]
        plt.imshow(frame_rgb)
        plt.title(f"{p.name} — first frame")
        plt.axis('off'); plt.tight_layout(); plt.show()
    else:
        info["first_frame_shape"] = None

    cap.release()
    return info

# ====== Helper: In kết quả gọn gàng ======
def print_kv_table(d: dict, title="Thông tin"):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))
    for k in sorted(d.keys()):
        v = d[k]
        if k in ("filesize", "approx_bitrate_bps") and v is not None:
            if k == "filesize":
                v_disp = f"{v} bytes ({readable_bytes(v)})"
            else:
                v_disp = f"{v:.0f} bps ({readable_bytes(v/8)}/s)"
        elif k == "duration_sec" and v is not None:
            v_disp = f"{v:.3f} s"
        else:
            v_disp = v
        print(f"{k:22s}: {v_disp}")

# ====== MAIN ======
def main():
    # 1) ẢNH
    img_path = IMAGE_PATH
    if img_path is None:
        img_path = choose_file_dialog(
            title="Chọn một ảnh (png/jpg/jpeg/tif/tiff/...)",
            filetypes=(("Images","*.png;*.jpg;*.jpeg;*.tif;*.tiff;*.bmp"),
                       ("All","*.*"))
        )
    if img_path and Path(img_path).exists():
        ip = image_properties(img_path)
        print_kv_table(ip, title="THUỘC TÍNH ẢNH")
        show_image(img_path)
    else:
        print("[INFO] Bỏ qua phần ẢNH (không chọn file).")

    # 2) VIDEO
    vid_path = VIDEO_PATH
    if vid_path is None:
        vid_path = choose_file_dialog(
            title="Chọn một video (mp4/avi/mov/mkv/...)",
            filetypes=(("Videos","*.mp4;*.avi;*.mov;*.mkv;*.wmv"),
                       ("All","*.*"))
        )
    if vid_path and Path(vid_path).exists():
        vp = video_properties(vid_path)
        print_kv_table(vp, title="THUỘC TÍNH VIDEO")
    else:
        print("[INFO] Bỏ qua phần VIDEO (không chọn file).")

if __name__ == "__main__":
    main()
