# retropangui-slate 작업 목록

## ES 설정 기본값 적용 (빌드 시)

### TransitionStyle 기본값 변경
- **파일**: `es_settings.cfg` 기본 템플릿
- **위치**: 빌드 시스템에서 타겟 이미지에 복사되는 설정 파일
- **변경 내용**:
  ```xml
  <string name="TransitionStyle" value="instant" />
  ```
- **참고**: 현재 기본값이 `fade`라 시스템 전환 시 블랙 플래시 발생

### 스탯 행 게임 수 숫자/레이블 분리
- **목적**: systemView 스탯 행에서 "512 GAMES AVAILABLE" 대신 숫자(512)와 레이블(GAMES)을 별도 요소로 노출
- **파일**: `es-app/src/views/SystemView.cpp`
- **현재 코드** (line 268): `ss << gameCount << " " << _("GAMES AVAILABLE");`
- **변경 방향**: `gameCount`를 별도 테마 바인딩 필드로 노출 (예: `gameCountText`) 추가
- **이유**: 테마에서 숫자만 크게, 레이블은 작게 2행 레이아웃 구현 불가

### 비디오 전환 크로스페이드 시간 조정
- **현상**: 스냅샷 이미지 → 비디오 전환 시 약 1초 페이드 발생
- **원인**: ES 내장 크로스페이드, 테마에서 제어 불가
- **변경 방향**: `VideoComponent.cpp` 의 페이드 지속 시간 하드코딩 값 수정
- **참고**: `showSnapshotDelay false`로 하면 페이드 없이 컷 전환되나 delay 동안 빈 화면

### system view longdescription 스크롤 지원
- **목적**: 긴 설명글이 고정 박스를 초과할 때 클리핑 없이 스크롤 가능하게
- **현상**: ES가 `<size>` 박스를 초과한 텍스트를 클리핑하지 않고 렌더해서 다른 요소와 겹침
- **참고**: `ScrollableContainer`는 현재 `md_description`에만 하드코딩 (`DetailedGameListView.cpp` line 141)
- **변경 방향**: `SystemView.cpp`에 `ScrollableContainer mDescContainer` 추가 후 `longdescription` extra 요소에 바인딩

---

## 테마 추가 작업

### 시스템 theme.xml 미완성 항목
- 로고 SVG가 있지만 per-system `theme.xml`이 없는 시스템들은 `systemfullname`, `shortdescription`, `longdescription` 데이터 없음
- `add_system_fullnames.py` 스크립트로 `systemfullname` 자동 추가 가능
- `shortdescription`(연도·제조사·비트), `longdescription`(한국어 설명)은 수동 작성 필요

### RECENTLY PLAYED 섹션
- 현재 숨김 처리 (pos 1.5 1.5)
- ES 기능 연동 구현 필요
