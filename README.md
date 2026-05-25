# retropangui-slate

EmulationStation theme for RetroPangUI — a modern slate design with dark sidebar and light content area.

## Design

- **System view**: Dark navy sidebar with vertical carousel + large system logo + description + console art
- **Gamelist view**: 3-column layout (sidebar / game list / screenshot + metadata)
- **Font**: [Pretendard](https://github.com/orioncactus/pretendard) (Korean + Latin)
- **Accent color**: `#4A8FE7` (blue)
- **Background**: `#EEF1F7` (light gray)
- **Sidebar**: `#1A1E2D` (dark navy)

## Layout

### System View
| 영역 | 위치 | 내용 |
|---|---|---|
| 사이드바 | 좌측 18% | 세로 캐러셀 (시스템 선택) |
| 헤더 | 상단 6.5% | 앱 이름 (RETROPANGUI-C5) |
| 메인 좌측 | 18~62% | 큰 시스템 로고 + 부제목 + 설명 + 게임 수 |
| 메인 우측 | 62~100% | 콘솔 아트 이미지 |

### Gamelist View
| 영역 | 위치 | 내용 |
|---|---|---|
| 사이드바 | 좌측 18% | 시스템 로고 + 짧은 설명 + 긴 설명 + 게임 수 |
| 게임 목록 | 18~53% | 게임 리스트 (textlist) |
| 상세 패널 | 53~100% | 스크린샷 + 게임 이름 + 메타데이터 + 설명 |

## Assets

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

## Supported Systems

`arcade`, `dreamcast`, `famicom`, `fba`, `gb`, `gba`, `gbc`, `gc`,
`genesis`, `mame`, `megadrive`, `n64`, `neogeo`, `nes`, `pcengine`,
`ps2`, `psx`, `saturn`, `sfc`, `snes`

## Local Development & Test

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

## Installation (Auto — via RetroPangUI build)

This theme is automatically downloaded and installed as part of the RetroPangUI Buildroot build.

## Manual Installation

```bash
# On the device:
cp -r retropangui-slate /retropangui/share/system/emulationstation/themes/
```

## Credits

- System logos: [nostalgia-pure-lite-ko](https://github.com/LeonardWard/retropangui-c5)
- Console art: [es-theme-epicnoir](https://github.com/c64-dev/es-theme-epicnoir)
- Font: [Pretendard](https://github.com/orioncactus/pretendard) by Kil Hyung-jin
