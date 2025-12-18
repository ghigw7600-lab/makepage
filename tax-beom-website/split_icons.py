from PIL import Image
import numpy as np
import os

# Gemini 생성 이미지 경로
input_image_path = r"C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\범\Gemini_Generated_Image_y3ehs2y3ehs2y3eh.png"
output_dir = r"C:\Users\기광우\makepage\tax-beom-website\assets\icons"

# 아이콘 이름 (handoff 문서 순서대로)
icon_names = [
    "consultant.png",
    "lightning.png",
    "chat-heart.png",
    "checklist-search.png",
    "question-bulb.png",
    "bulb-dollar.png",
    "doc-calculator.png",
    "folder.png",
    "target-person.png",
    "money-cycle.png",
    "coins-down.png",
    "family-home.png"
]

print("이미지 로딩 중...")
img = Image.open(input_image_path)
img = img.convert("RGBA")  # RGBA 모드로 변환
img_array = np.array(img)

print(f"원본 이미지 크기: {img.size}")
print(f"배열 shape: {img_array.shape}")

# 이미지가 3x4 그리드인지 확인
width, height = img.size

# 12개 아이콘을 3x4 또는 4x3 그리드로 가정
# 먼저 어떤 배치인지 확인
rows = 3
cols = 4

icon_width = width // cols
icon_height = height // rows

print(f"\n각 아이콘 크기: {icon_width} x {icon_height}")
print(f"그리드 배치: {rows}행 x {cols}열")

# 12개 아이콘 분리
print("\n아이콘 분리 및 투명화 시작...")
for idx, icon_name in enumerate(icon_names):
    row = idx // cols
    col = idx % cols

    # 아이콘 영역 추출
    left = col * icon_width
    top = row * icon_height
    right = left + icon_width
    bottom = top + icon_height

    icon = img.crop((left, top, right, bottom))
    icon_array = np.array(icon)

    # 흰색 및 밝은 회색 배경을 투명으로 변환
    # RGB 값이 (230, 230, 230) 이상인 픽셀을 투명하게
    mask = (icon_array[:, :, 0] >= 230) & \
           (icon_array[:, :, 1] >= 230) & \
           (icon_array[:, :, 2] >= 230)

    # 알파 채널을 0으로 설정 (완전 투명)
    icon_array[mask, 3] = 0

    # PIL Image로 변환
    transparent_icon = Image.fromarray(icon_array, mode='RGBA')

    # 여백 제거 (crop to content)
    bbox = transparent_icon.getbbox()
    if bbox:
        transparent_icon = transparent_icon.crop(bbox)

    # 512x512로 리사이즈 (여백 포함)
    # 비율 유지하면서 512x512 캔버스 중앙에 배치
    final_icon = Image.new('RGBA', (512, 512), (0, 0, 0, 0))

    # 아이콘을 캔버스보다 작게 유지 (여백 확보)
    max_size = 400  # 512의 78%
    transparent_icon.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

    # 중앙 배치
    paste_x = (512 - transparent_icon.width) // 2
    paste_y = (512 - transparent_icon.height) // 2
    final_icon.paste(transparent_icon, (paste_x, paste_y), transparent_icon)

    # 저장
    output_path = os.path.join(output_dir, icon_name)
    final_icon.save(output_path, 'PNG')
    print(f"[OK] {icon_name} saved ({transparent_icon.width}x{transparent_icon.height} -> 512x512)")

print(f"\nComplete! 12 icons saved to {output_dir}")
