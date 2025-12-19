# -*- coding: utf-8 -*-
"""
index.html의 모든 PNG/JPG 이미지를 WebP로 변경하고 lazy loading 추가
"""

import re
import sys

# UTF-8 출력 설정
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def update_images_to_webp(html_path):
    """
    HTML 파일의 모든 이미지를 WebP로 변경하고 lazy loading 추가
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. PNG/JPG → WebP 변환 (assets/ 경로만)
    replacements = [
        # 로고
        ('assets/logo/beom-logo1.png', 'assets/logo/beom-logo1.webp'),
        ('assets/logo/beom-logo2.png', 'assets/logo/beom-logo2.webp'),
        ('assets/logo/beom-logo1-white.png', 'assets/logo/beom-logo1-white.webp'),

        # 아이콘
        ('assets/icons/consultant.png', 'assets/icons/consultant.webp'),
        ('assets/icons/lightning.png', 'assets/icons/lightning.webp'),
        ('assets/icons/chat-heart.png', 'assets/icons/chat-heart.webp'),
        ('assets/icons/checklist-search.png', 'assets/icons/checklist-search.webp'),
        ('assets/icons/question-bulb.png', 'assets/icons/question-bulb.webp'),
        ('assets/icons/doc-calculator.png', 'assets/icons/doc-calculator.webp'),
        ('assets/icons/bulb-dollar.png', 'assets/icons/bulb-dollar.webp'),
        ('assets/icons/folder.png', 'assets/icons/folder.webp'),
        ('assets/icons/target-person.png', 'assets/icons/target-person.webp'),
        ('assets/icons/money-cycle.png', 'assets/icons/money-cycle.webp'),
        ('assets/icons/coins-down.png', 'assets/icons/coins-down.webp'),
        ('assets/icons/family-home.png', 'assets/icons/family-home.webp'),

        # 사진
        ('assets/photos/ceo.jpg', 'assets/photos/ceo.webp'),
    ]

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"OK {old} -> {new}")

    # 2. <img> 태그에 loading="lazy" 추가 (nav__logo-img는 제외)
    # 패턴: <img src="assets/... 로 시작하는 img 태그 중 loading 속성이 없는 것
    img_pattern = r'(<img\s+[^>]*src="assets/[^"]+\.webp"[^>]*)(>)'

    def add_lazy_loading(match):
        img_tag = match.group(1)
        closing = match.group(2)

        # 이미 loading 속성이 있으면 스킵
        if 'loading=' in img_tag:
            return match.group(0)

        # nav__logo-img 클래스는 제외 (메인 로고는 즉시 로딩)
        if 'nav__logo-img' in img_tag or 'footer__logo-img' in img_tag:
            return match.group(0)

        # lazy loading 추가
        return f'{img_tag} loading="lazy"{closing}'

    content = re.sub(img_pattern, add_lazy_loading, content)
    print("\nOK <img> 태그에 loading='lazy' 추가 완료")

    # 3. 파일 저장
    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nOK {html_path} 업데이트 완료!")
        return True
    else:
        print(f"\nNo changes needed for {html_path}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("index.html 이미지 WebP 변환 및 lazy loading 추가")
    print("=" * 60)

    update_images_to_webp('index.html')

    print("=" * 60)
    print("완료! 브라우저에서 확인하세요.")
    print("=" * 60)
