from PIL import Image
import os

# Gemini 생성 이미지 경로
input_image_path = r"C:\Users\기광우\OneDrive\Desktop\기광우 업무\AI\범\Gemini_Generated_Image_y3ehs2y3ehs2y3eh.png"
output_dir = r"C:\Users\기광우\makepage\tax-beom-website\assets\icons"

# 이미지를 보고 handoff 문서 매핑에 맞게 선택
# 그리드 위치 (row, col) -> 파일명
icon_mapping = {
    # Row 0 (첫 번째 줄)
    (0, 0): "consultant.png",        # 헤드셋 상담사
    (0, 1): "lightning.png",          # 번개
    (0, 2): "chat-heart.png",         # 말풍선+하트
    (0, 3): "checklist-search.png",   # 체크리스트+돋보기

    # Row 1 (두 번째 줄)
    (1, 0): "doc-calculator.png",     # 문서+계산기
    (1, 1): "question-bulb.png",      # 물음표 전구
    (1, 2): "bulb-dollar.png",        # 전구+달러
    (1, 3): "bulb-dollar.png",        # 전구+달러 (중복, 다른 걸로 대체 필요)

    # Row 2 (세 번째 줄)
    (2, 0): None,                     # 문서 (사용 안 함)
    (2, 1): None,                     # 문서 (사용 안 함)
    (2, 2): "folder.png",             # 폴더+문서
    (2, 3): "target-person.png",      # 타겟+인물

    # Row 3 (네 번째 줄)
    (3, 0): "money-cycle.png",        # 코인 순환
    (3, 1): "coins-down.png",         # 코인+화살표
    (3, 2): "coins-down.png",         # 코인+화살표 (중복)
    (3, 3): "family-home.png",        # 집+가족
}

print("Loading image...")
img = Image.open(input_image_path)
img = img.convert("RGBA")

width, height = img.size
print(f"Image size: {width} x {height}")

# 4x4 그리드
rows = 4
cols = 4

icon_width = width // cols
icon_height = height // rows

print(f"Each icon size: {icon_width} x {icon_height}")
print(f"Grid layout: {rows} rows x {cols} cols")

# 실제 필요한 12개 아이콘만 추출
# handoff 문서의 순서대로
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

# 각 아이콘 위치 (수동 매핑 - 이미지 보고 판단)
positions = {
    "consultant.png": (0, 0),        # 헤드셋
    "lightning.png": (0, 1),          # 번개
    "chat-heart.png": (0, 2),         # 하트말풍선
    "checklist-search.png": (0, 3),   # 돋보기
    "doc-calculator.png": (1, 0),     # 클립보드+계산기
    "question-bulb.png": (1, 1),      # 물음표 전구
    "bulb-dollar.png": (1, 2),        # 달러 전구
    "folder.png": (2, 2),             # 폴더
    "target-person.png": (2, 3),      # 타겟
    "money-cycle.png": (3, 0),        # 재활용 화살표
    "coins-down.png": (3, 1),         # 코인 스택
    "family-home.png": (3, 3),        # 집
}

print("\nExtracting icons...")
for icon_name in icon_names:
    if icon_name not in positions:
        print(f"[SKIP] {icon_name} - no position mapping")
        continue

    row, col = positions[icon_name]

    # 아이콘 영역 추출
    left = col * icon_width
    top = row * icon_height
    right = left + icon_width
    bottom = top + icon_height

    icon = img.crop((left, top, right, bottom))

    # 여백 제거 (이미 투명 배경)
    bbox = icon.getbbox()
    if bbox:
        icon = icon.crop(bbox)

    # 512x512로 리사이즈 (여백 포함)
    final_icon = Image.new('RGBA', (512, 512), (0, 0, 0, 0))

    # 아이콘 크기 조정 (최대 400px)
    max_size = 400
    icon.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

    # 중앙 배치
    paste_x = (512 - icon.width) // 2
    paste_y = (512 - icon.height) // 2
    final_icon.paste(icon, (paste_x, paste_y), icon)

    # 저장
    output_path = os.path.join(output_dir, icon_name)
    final_icon.save(output_path, 'PNG')
    print(f"[OK] {icon_name} saved (position: row {row}, col {col})")

print(f"\nComplete! Icons saved to {output_dir}")
