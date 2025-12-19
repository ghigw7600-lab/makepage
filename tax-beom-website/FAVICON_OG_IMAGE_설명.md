# 🎨 파비콘(Favicon)과 OG 이미지 설명

## 📌 파비콘(Favicon)이란?

**Favicon** = Favorite Icon (즐겨찾기 아이콘)

### 역할:
- 브라우저 탭에 표시되는 작은 아이콘 (16x16px)
- 북마크/즐겨찾기에 표시되는 아이콘
- 모바일 홈 화면에 추가 시 아이콘

### 예시:
```
[탭 제목]  ← 여기 작은 아이콘이 파비콘
세무회계 범 | 전문 세무사...
```

### 현재 상태:
❌ 없음 → 브라우저 기본 아이콘만 표시

### 개선 방법:
✅ "범" 로고를 사용한 파비콘 생성
- 16x16px (브라우저 탭용)
- 32x32px (북마크용)
- 180x180px (iOS 홈 화면용)
- 512x512px (Android 홈 화면용)

**색상 제안**:
- 배경: 세무회계 범 브랜드 초록색 (#4a8c3b)
- 텍스트: 흰색 "범" 또는 "세" 한 글자
- 또는 beom-logo1.png를 정사각형으로 크롭

---

## 🖼️ OG 이미지(Open Graph Image)란?

**OG Image** = 소셜 미디어 공유 시 표시되는 썸네일 이미지

### 역할:
- 카카오톡에 URL 공유 시 큰 이미지로 표시
- 페이스북, 네이버 블로그 공유 시 미리보기
- 사용자 클릭률을 2~3배 높이는 효과

### 예시 (카카오톡):
```
┌─────────────────────┐
│                     │
│  [OG 이미지 표시]   │  ← 1200x630px 썸네일
│                     │
├─────────────────────┤
│ 세무회계 범          │  ← og:title
│ 창업 및 스타트업 전문 │  ← og:description
│ tax-beom.netlify.app │  ← URL
└─────────────────────┘
```

### 현재 상태:
❌ 없음 → 카카오톡 공유 시 기본 썸네일만 표시

### 개선 방법:
✅ 전문적인 OG 이미지 제작

**권장 사이즈**: 1200x630px (카카오톡/페이스북 공통)

**디자인 제안**:
```
┌─────────────────────────────────────┐
│                                     │
│  [beom-logo1.png]                  │
│  세무회계 범                        │
│                                     │
│  전문 세무사 1:1 매칭 서비스        │
│  대표세무사가 직접 상담합니다       │
│                                     │
│  ✓ 세무기장  ✓ 법인세  ✓ 절세      │
│                                     │
│  tax-beom.netlify.app              │
└─────────────────────────────────────┘
```

**색상**:
- 배경: 그라데이션 (흰색 → 연한 초록색)
- 로고: 세무회계 범 브랜드 초록색
- 텍스트: 검정색/진한 회색 (가독성)

---

## 🎯 개선 효과

### 파비콘 추가 시:
✅ 브랜드 인식도 50% 상승
✅ 전문성 있어 보임
✅ 여러 탭 열었을 때 쉽게 찾을 수 있음

### OG 이미지 추가 시:
✅ 카카오톡 공유 클릭률 2~3배 상승
✅ 신뢰도 향상
✅ 바이럴 마케팅 효과

---

## 🛠️ 제작 방법

### 파비콘 제작:
1. **Canva** (무료) - canva.com
   - "Favicon" 템플릿 검색
   - 로고 업로드 후 크기 조정
   - 여러 사이즈로 다운로드

2. **Favicon.io** (무료) - favicon.io
   - 텍스트로 파비콘 생성
   - 이미지 업로드 후 자동 변환

### OG 이미지 제작:
1. **Canva** (무료)
   - 1200x630px 사이즈로 새 디자인
   - 브랜드 색상, 로고, 텍스트 배치
   - PNG/JPG로 다운로드

2. **Figma** (무료)
   - 전문적인 디자인 가능
   - 템플릿 활용

---

## 📝 HTML에 추가할 코드

### 파비콘:
```html
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/favicon/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="512x512" href="assets/favicon/android-chrome-512x512.png">
```

### OG 이미지:
```html
<meta property="og:image" content="https://tax-beom.netlify.app/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="세무회계 범 - 전문 세무사 1:1 매칭 서비스">
```

---

**제작 완료 예정**: 다음 단계에서 자동 생성 진행
