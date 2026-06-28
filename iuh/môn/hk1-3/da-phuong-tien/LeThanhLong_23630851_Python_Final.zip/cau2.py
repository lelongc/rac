
from PIL import Image


input_image = 'input.png'
output_image = 'output_gray.png'


img = Image.open(input_image)


gray_img = img.convert('L')


resized_img = gray_img.resize((256, 256))


resized_img.save(output_image)

print(f"Ảnh đã được chuyển sang grayscale và lưu tại: {output_image}")
