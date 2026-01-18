import os
from PIL import Image, ImageDraw, ImageFont

# 创建图片目录
os.makedirs('images', exist_ok=True)

# 定义图片配置
images_config = [
    {'filename': 'habitat-map.jpg', 'size': (800, 500), 'color': (74, 124, 89), 'text': 'Habitat Map'},
    {'filename': 'endangered-species.jpg', 'size': (600, 400), 'color': (231, 76, 60), 'text': 'Endangered Species'},
    {'filename': 'deforestation.jpg', 'size': (400, 300), 'color': (243, 156, 18), 'text': 'Deforestation'},
    {'filename': 'habitat-fragmentation.jpg', 'size': (400, 300), 'color': (230, 126, 34), 'text': 'Habitat Fragmentation'},
    {'filename': 'poaching.jpg', 'size': (400, 300), 'color': (192, 57, 43), 'text': 'Poaching'},
    {'filename': 'pollution.jpg', 'size': (400, 300), 'color': (142, 68, 173), 'text': 'Pollution'},
    {'filename': 'conservation-action.jpg', 'size': (600, 400), 'color': (39, 174, 96), 'text': 'Conservation Action'}
]

def create_placeholder_image(filename, size, bg_color, text):
    # 创建带有指定背景色的图像
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # 尝试使用默认字体，如果不可用则使用内置字体
    try:
        # 在Windows系统上常用的字体
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        try:
            # 尝试其他常见字体
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 40)
        except:
            # 使用默认字体
            font = ImageFont.load_default()
    
    # 获取文本尺寸
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # 计算文本位置（居中）
    x = (size[0] - text_width) / 2
    y = (size[1] - text_height) / 2
    
    # 绘制文本
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # 保存图像
    img.save(f'images/{filename}')
    print(f'Created {filename}')

# 创建所有占位图片
for config in images_config:
    create_placeholder_image(**config)

print('All placeholder images have been created successfully!')