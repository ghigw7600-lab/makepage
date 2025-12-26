#!/usr/bin/env python3
"""
엘림세무회계컨설팅 파비콘 및 OG 이미지 생성 스크립트
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
FAVICON_DIR = os.path.join(ASSETS_DIR, 'favicon')
OG_DIR = os.path.join(ASSETS_DIR, 'og')

# 폴더 생성
os.makedirs(FAVICON_DIR, exist_ok=True)
os.makedirs(OG_DIR, exist_ok=True)

# 브랜드 색상
PRIMARY_BLUE = (26, 92, 184)      # #1a5cb8
MINT = (78, 205, 196)              # #4ecdc4
SKY_BLUE = (91, 163, 224)          # #5ba3e0
DARK_BLUE = (26, 58, 92)           # #1a3a5c
WHITE = (255, 255, 255)

def create_favicon_icon(size):
    """파비콘 아이콘 생성 (정사각형)"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 비율 계산
    padding = size * 0.05
    icon_size = size - (padding * 2)

    # 메인 배경 (파란색 사각형)
    corner_radius = int(size * 0.1)
    draw.rounded_rectangle(
        [padding, padding, size - padding, size - padding],
        radius=corner_radius,
        fill=PRIMARY_BLUE
    )

    # 민트색 작은 사각형 (우상단)
    small_size = icon_size * 0.4
    small_x = size - padding - small_size - (icon_size * 0.08)
    small_y = padding + (icon_size * 0.08)
    draw.rounded_rectangle(
        [small_x, small_y, small_x + small_size, small_y + small_size],
        radius=int(corner_radius * 0.5),
        fill=MINT
    )

    # 하늘색 큰 사각형 (좌하단)
    big_width = icon_size * 0.55
    big_height = icon_size * 0.6
    big_x = padding + (icon_size * 0.08)
    big_y = size - padding - big_height - (icon_size * 0.08)
    draw.rounded_rectangle(
        [big_x, big_y, big_x + big_width, big_y + big_height],
        radius=int(corner_radius * 0.5),
        fill=SKY_BLUE
    )

    return img

def create_og_image():
    """OG 이미지 생성 (1200x630)"""
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(img)

    # 배경 그라데이션 효과 (상단에 연한 파란색)
    for y in range(height):
        ratio = y / height
        r = int(255 - (255 - 232) * (1 - ratio) * 0.3)
        g = int(255 - (255 - 240) * (1 - ratio) * 0.3)
        b = int(255 - (255 - 254) * (1 - ratio) * 0.3)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 좌측에 아이콘 배치
    icon_size = 180
    icon = create_favicon_icon(icon_size)
    icon_x = 120
    icon_y = (height - icon_size) // 2
    img.paste(icon, (icon_x, icon_y), icon)

    # 텍스트 영역
    text_x = icon_x + icon_size + 60

    # 폰트 설정 (시스템 폰트 사용)
    try:
        font_large = ImageFont.truetype("malgun.ttf", 72)
        font_medium = ImageFont.truetype("arial.ttf", 28)
        font_small = ImageFont.truetype("malgun.ttf", 32)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # 회사명
    draw.text((text_x, height//2 - 80), "엘림세무회계컨설팅", fill=DARK_BLUE, font=font_large)

    # 영문명
    draw.text((text_x, height//2 + 20), "ELIMTAX CONSULTING", fill=PRIMARY_BLUE, font=font_medium)

    # 슬로건
    draw.text((text_x, height//2 + 70), "세금은 가볍게, 계좌는 무겁게", fill=(102, 102, 102), font=font_small)

    # 하단 라인
    draw.rectangle([0, height - 8, width, height], fill=PRIMARY_BLUE)

    return img

def main():
    print("[START] Elim Tax Favicon & OG Image Generation...")

    # 파비콘 생성 (4종)
    favicon_sizes = [16, 32, 180, 512]

    for size in favicon_sizes:
        icon = create_favicon_icon(size)

        if size == 180:
            filename = 'apple-touch-icon.png'
        elif size == 512:
            filename = 'android-chrome-512x512.png'
        else:
            filename = f'favicon-{size}x{size}.png'

        filepath = os.path.join(FAVICON_DIR, filename)
        icon.save(filepath, 'PNG')
        print(f"  [OK] {filename}")

    # ICO 파일 생성 (16, 32 합본)
    icon_16 = create_favicon_icon(16)
    icon_32 = create_favicon_icon(32)
    ico_path = os.path.join(FAVICON_DIR, 'favicon.ico')
    icon_32.save(ico_path, format='ICO', sizes=[(16, 16), (32, 32)])
    print(f"  [OK] favicon.ico")

    # OG 이미지 생성
    og_image = create_og_image()
    og_path = os.path.join(OG_DIR, 'og-image.png')
    og_image.save(og_path, 'PNG', optimize=True)
    print(f"  [OK] og-image.png (1200x630)")

    print("\n[DONE] All images generated!")
    print(f"   Favicon: {FAVICON_DIR}")
    print(f"   OG Image: {OG_DIR}")

if __name__ == "__main__":
    main()
