# -*- coding: utf-8 -*-
"""
PNG 이미지를 WebP로 변환하는 스크립트
30-50% 파일 크기 감소 효과
"""

from PIL import Image
import os
import sys

# UTF-8 출력 설정
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def convert_to_webp(input_path, output_path, quality=85):
    """
    PNG/JPG 이미지를 WebP로 변환

    Args:
        input_path: 원본 이미지 경로
        output_path: 출력 WebP 경로
        quality: WebP 품질 (1-100, 기본 85)
    """
    try:
        img = Image.open(input_path)

        # RGBA 모드가 아니면 RGB로 변환
        if img.mode != 'RGBA' and img.mode != 'RGB':
            img = img.convert('RGB')

        # WebP로 저장
        img.save(output_path, 'WEBP', quality=quality, method=6)

        # 파일 크기 비교
        original_size = os.path.getsize(input_path)
        webp_size = os.path.getsize(output_path)
        reduction = ((original_size - webp_size) / original_size) * 100

        print(f"OK {os.path.basename(input_path)} -> {os.path.basename(output_path)}")
        print(f"   원본: {original_size/1024:.1f}KB, WebP: {webp_size/1024:.1f}KB (감소율: {reduction:.1f}%)")

        return True
    except Exception as e:
        print(f"Error {input_path}: {e}")
        return False

def convert_directory(directory):
    """
    디렉토리 내 모든 PNG/JPG를 WebP로 변환
    """
    converted_count = 0
    total_original_size = 0
    total_webp_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)

                # 이미 WebP가 존재하면 스킵
                webp_filename = os.path.splitext(file)[0] + '.webp'
                output_path = os.path.join(root, webp_filename)

                if os.path.exists(output_path):
                    print(f"Skip {file} (이미 WebP 존재)")
                    continue

                original_size = os.path.getsize(input_path)

                if convert_to_webp(input_path, output_path):
                    webp_size = os.path.getsize(output_path)
                    total_original_size += original_size
                    total_webp_size += webp_size
                    converted_count += 1

    return converted_count, total_original_size, total_webp_size

if __name__ == "__main__":
    print("=" * 60)
    print("세무회계 범 - 이미지 WebP 변환")
    print("=" * 60)

    # 변환할 디렉토리
    directories = [
        "assets/icons",
        "assets/logo",
        "assets/photos"
    ]

    total_converted = 0
    total_original = 0
    total_webp = 0

    for directory in directories:
        if os.path.exists(directory):
            print(f"\n[{directory}] 변환 중...")
            count, original_size, webp_size = convert_directory(directory)
            total_converted += count
            total_original += original_size
            total_webp += webp_size
        else:
            print(f"[{directory}] 디렉토리가 존재하지 않습니다.")

    print("=" * 60)
    print(f"변환 완료! 총 {total_converted}개 파일")

    if total_original > 0:
        total_reduction = ((total_original - total_webp) / total_original) * 100
        print(f"원본 총 크기: {total_original/1024:.1f}KB")
        print(f"WebP 총 크기: {total_webp/1024:.1f}KB")
        print(f"절감 용량: {(total_original - total_webp)/1024:.1f}KB ({total_reduction:.1f}% 감소)")

    print("=" * 60)
    print("\n다음 단계: index.html에서 이미지 경로를 .webp로 변경하세요")
    print("예: <img src='assets/logo/beom-logo1.png'> → <img src='assets/logo/beom-logo1.webp'>")
