from PIL import Image
import numpy as np
import os

# 아이콘 디렉토리
icons_dir = r"C:\Users\기광우\makepage\tax-beom-website\assets\icons"

icon_files = [
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

print("Removing backgrounds from icons...")

for icon_file in icon_files:
    icon_path = os.path.join(icons_dir, icon_file)

    if not os.path.exists(icon_path):
        print(f"[SKIP] {icon_file} - file not found")
        continue

    # 이미지 로드
    img = Image.open(icon_path).convert("RGBA")
    img_array = np.array(img)

    # 밝은 회색/흰색 배경 제거 (더 공격적으로)
    # RGB 값이 200 이상인 픽셀을 투명으로 (회색 체크무늬 포함)
    threshold = 200

    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]

    # 회색톤 배경 (RGB 값이 비슷하고 밝은 경우)
    is_gray = (np.abs(r.astype(int) - g.astype(int)) < 20) & \
              (np.abs(g.astype(int) - b.astype(int)) < 20) & \
              (r >= threshold)

    # 알파 채널을 0으로 설정
    img_array[is_gray, 3] = 0

    # 결과 이미지 생성
    result_img = Image.fromarray(img_array, mode='RGBA')

    # 저장
    result_img.save(icon_path, 'PNG')
    print(f"[OK] {icon_file} - background removed")

print(f"\nComplete! All icons processed.")
