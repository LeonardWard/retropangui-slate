# retropangui-slate

RetroPangUI용 EmulationStation 테마 — 다크 사이드바와 밝은 콘텐츠 영역을 가진 모던 슬레이트 디자인.

## 디자인

- **시스템 뷰**: 다크 네이비 사이드바 + 세로 캐러셀 + 큰 시스템 로고 + 설명 + 콘솔 아트
- **게임목록 뷰**: 3단 레이아웃 (사이드바 / 게임 목록 / 스크린샷 + 메타데이터)
- **폰트**: [Pretendard](https://github.com/orioncactus/pretendard) (한글 + 라틴)
- **강조 색상**: `#4A8FE7` (파랑)
- **배경**: `#EEF1F7` (밝은 회색)
- **사이드바**: `#1A1E2D` (다크 네이비)

## 레이아웃

### 시스템 뷰
| 영역 | 위치 | 내용 |
|---|---|---|
| 사이드바 | 좌측 18% | 세로 캐러셀 (시스템 선택) |
| 헤더 | 상단 6.5% | 앱 이름 (RETROPANGUI-C5) |
| 메인 좌측 | 18~62% | 큰 시스템 로고 + 부제목 + 설명 + 게임 수 |
| 메인 우측 | 62~100% | 콘솔 아트 이미지 |

### 게임목록 뷰
| 영역 | 위치 | 내용 |
|---|---|---|
| 사이드바 | 좌측 18% | 시스템 로고 + 짧은 설명 + 긴 설명 + 게임 수 |
| 게임 목록 | 18~53% | 게임 리스트 (textlist) |
| 상세 패널 | 53~100% | 스크린샷 + 게임 이름 + 메타데이터 + 설명 |

## 파일 구조 — 뭘 고치려면 어디를 봐야 하나

- **`theme.xml`(루트)**: 모든 화면의 실제 위치·크기·폰트·색상이 전부 여기 인라인으로 들어있음.
  게임목록류 화면(`<view name="basic, detailed, video, grid">`)과 메인 시스템 화면
  (`<view name="system">`)이 둘 다 이 파일 안에 있음. **위치/크기/폰트/색상을 고치려면
  항상 이 파일을 본다.**
- **`<system>/theme.xml`**(예: `snes/theme.xml`): 그 시스템만의 텍스트 **내용**(이름·
  짧은 설명·긴 설명·overview)만 담음. `<include>./../theme.xml</include>`로 루트의
  스타일을 그대로 물려받아 화면에 배치됨. **시스템별 문구 내용만 고치려면 이 파일.**
- 같은 이름의 요소(예: `longdescription`)가 루트와 시스템 파일 양쪽에 있으면 **병합**됨 -
  보통은 위치/크기(`pos`/`size`/`fontSize` 등)는 루트에서, 내용(`<text>...</text>`)은
  시스템 파일에서 온다. `<include>`가 시스템 파일 자신의 내용보다 먼저 파싱되므로,
  시스템 파일에 스타일 속성을 또 적으면 그게 루트 값을 **덮어쓴다**(무시되는 게
  아니라 우선함) - 특별한 이유 없이는 시스템 파일에 스타일을 적지 않는다.

빠른 참조:

| 하고 싶은 것 | 수정할 파일 | 찾을 요소 |
|---|---|---|
| 게임목록 화면 롬 목록 폰트/줄간격 | `theme.xml` | `<textlist name="gamelist">` |
| 게임목록 화면 스크린샷 이미지 크기 | `theme.xml` | `<image name="md_image">` |
| 게임목록 화면 게임 설명(우측 하단) 폰트/크기 | `theme.xml` | `<text name="md_description">` |
| 게임목록 화면 사이드바 상세설명(overview) 위치/크기 | `theme.xml` (basic/detailed/video/grid 뷰) | `<text name="overview">` |
| 게임목록 화면 overview **문구 내용** | `<system>/theme.xml` | `<text name="overview">` |
| 메인 화면(system view) 긴 설명 폰트/크기 | `theme.xml` (system 뷰) | `<text name="longdescription">` |
| 메인 화면 긴 설명 **문구 내용** | `<system>/theme.xml` | `<text name="longdescription">` |
| 시스템 로고 옆 이름/짧은 설명 문구 | `<system>/theme.xml` | `<text name="systemfullname">` / `<text name="shortdescription">` |

> **주의**: `_inc/` 폴더는 삭제됨(2026-07-18). 예전엔 여기 파일들을 `<include>`할
> 구상이었던 것으로 보이나 실제로는 한 번도 연결된 적 없이 루트 `theme.xml`에
> 전부 인라인하는 방식으로 굳어짐 - 이 문서가 만들어지기 전까지 `_inc/`를
> 고치는 실수가 반복되며 실기기에 반영이 안 됐었음(효과 자체가 없는 죽은 파일).

## 에셋

```
_assets/
  white.png              # 색상 레이어용 1×1 흰색 이미지
  fonts/
    Pretendard-Regular.ttf
    Pretendard-Bold.ttf
  logos/
    {system.theme}.svg   # 시스템 로고 (흰색 SVG, 사이드바용)
  consoles/
    {system.theme}.png   # 콘솔 아트 이미지 (시스템 뷰용)
```

## 지원 시스템

`arcade`, `dreamcast`, `famicom`, `fba`, `gb`, `gba`, `gbc`, `gc`,
`genesis`, `mame`, `megadrive`, `n64`, `neogeo`, `nes`, `pcengine`,
`ps2`, `psx`, `saturn`, `sfc`, `snes`

## 로컬 개발 및 테스트

```bash
# 1. 심볼릭 링크 (최초 1회)
ln -s /home/pangui/scripts/retropangui-slate /home/pangui/share/themes/retropangui-slate

# 2. EmulationStation 실행 (디버그 모드)
/opt/retropangui/bin/emulationstation --debug

# 3. 테마 변경사항 즉시 적용 (ES 실행 중)
# Ctrl+R — UI 전체 리로드 (--debug 모드에서만)
```

ES 설정 (`/home/pangui/share/system/configs/emulationstation/es_settings.cfg`) 에
`ThemeSet` 값이 `retropangui-slate`로 지정되어 있어야 합니다.

## 설치 (자동 — RetroPangUI 빌드 경유)

이 테마는 RetroPangUI Buildroot 빌드 과정에서 자동으로 다운로드·설치됩니다.

## 수동 설치

```bash
# 기기에서:
cp -r retropangui-slate /retropangui/share/system/emulationstation/themes/
```

## 크레딧

- 시스템 로고: [nostalgia-pure-lite-ko](https://github.com/LeonardWard/retropangui-c5)
- 콘솔 아트: [es-theme-epicnoir](https://github.com/c64-dev/es-theme-epicnoir)
- 폰트: [Pretendard](https://github.com/orioncactus/pretendard) by Kil Hyung-jin
