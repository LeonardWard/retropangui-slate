#!/usr/bin/env python3
"""
각 시스템 theme.xml에 systemfullname 필드 추가
- es_systems.xml/systems.json 우선 참조
- 없으면 내장 매핑 사용
"""
import os
import json
import xml.etree.ElementTree as ET

ES_SYSTEMS_XML = "/home/pangui/scripts/retropangui-c5/buildroot/output/target/etc/emulationstation/es_systems.xml"
SYSTEMS_JSON   = "/home/pangui/scripts/retropangui-c5/board/odroidc5/systems.json"
THEME_DIR      = os.path.dirname(os.path.abspath(__file__))

# 내장 fullname 매핑 (es_systems.xml에 없는 시스템 보완)
BUILTIN = {
    "3do":              "3DO INTERACTIVE MULTIPLAYER",
    "amiga":            "COMMODORE AMIGA",
    "amigacd32":        "COMMODORE AMIGA CD32",
    "amstradcpc":       "AMSTRAD CPC",
    "apple2":           "APPLE II",
    "arcade":           "ARCADE",
    "atari2600":        "ATARI 2600",
    "atari5200":        "ATARI 5200",
    "atari7800":        "ATARI 7800",
    "atari800":         "ATARI 800",
    "atarijaguar":      "ATARI JAGUAR",
    "atarilynx":        "ATARI LYNX",
    "atarist":          "ATARI ST",
    "atomiswave":       "ATOMISWAVE",
    "c64":              "COMMODORE 64",
    "channelf":         "FAIRCHILD CHANNEL F",
    "coleco":           "COLECO",
    "colecovision":     "COLECOVISION",
    "dreamcast":        "SEGA DREAMCAST",
    "famicom":          "NINTENDO FAMICOM",
    "fba":              "FINAL BURN ALPHA",
    "fds":              "FAMICOM DISK SYSTEM",
    "gamegear":         "SEGA GAME GEAR",
    "gb":               "NINTENDO GAME BOY",
    "gba":              "NINTENDO GAME BOY ADVANCE",
    "gbc":              "NINTENDO GAME BOY COLOR",
    "gc":               "NINTENDO GAMECUBE",
    "genesis":          "SEGA GENESIS",
    "intellivision":    "MATTEL INTELLIVISION",
    "lynx":             "ATARI LYNX",
    "macintosh":        "APPLE MACINTOSH",
    "mame":             "MAME",
    "mastersystem":     "SEGA MASTER SYSTEM",
    "mega32x":          "SEGA 32X",
    "megacd":           "SEGA MEGA-CD",
    "megadrive":        "SEGA MEGA DRIVE",
    "megadrive-japan":  "SEGA MEGA DRIVE",
    "msx":              "MSX",
    "msx2":             "MSX2",
    "n64":              "NINTENDO 64",
    "naomi":            "SEGA NAOMI",
    "nds":              "NINTENDO DS",
    "neogeo":           "SNK NEO GEO",
    "neogeocd":         "SNK NEO GEO CD",
    "nes":              "NINTENDO ENTERTAINMENT SYSTEM",
    "ngp":              "SNK NEO GEO POCKET",
    "ngpc":             "SNK NEO GEO POCKET COLOR",
    "odyssey2":         "MAGNAVOX ODYSSEY 2",
    "pc":               "PC (DOS)",
    "pc88":             "NEC PC-8800",
    "pcengine":         "NEC PC ENGINE",
    "pcenginecd":       "NEC PC ENGINE CD",
    "pcfx":             "NEC PC-FX",
    "ps2":              "SONY PLAYSTATION 2",
    "psp":              "SONY PLAYSTATION PORTABLE",
    "pspminis":         "PLAYSTATION PORTABLE MINIS",
    "psx":              "SONY PLAYSTATION",
    "samcoupe":         "SAM COUPÉ",
    "saturn":           "SEGA SATURN",
    "scummvm":          "SCUMMVM",
    "sega32x":          "SEGA 32X",
    "segacd":           "SEGA CD",
    "sfc":              "SUPER FAMICOM",
    "sg-1000":          "SEGA SG-1000",
    "snes":             "SUPER NINTENDO ENTERTAINMENT SYSTEM",
    "snes-usa":         "SUPER NINTENDO ENTERTAINMENT SYSTEM",
    "snescd":           "SUPER NINTENDO CD-ROM",
    "supergrafx":       "NEC SUPERGRAFX",
    "tg16":             "NEC TURBOGRAFX-16",
    "tg16cd":           "NEC TURBOGRAFX-CD",
    "ti99":             "TEXAS INSTRUMENTS TI-99",
    "vectrex":          "VECTREX",
    "videopac":         "PHILIPS VIDEOPAC",
    "virtualboy":       "NINTENDO VIRTUAL BOY",
    "wii":              "NINTENDO WII",
    "wiiu":             "NINTENDO WII U",
    "wonderswan":       "BANDAI WONDERSWAN",
    "wonderswancolor":  "BANDAI WONDERSWAN COLOR",
    "x68000":           "SHARP X68000",
    "zxspectrum":       "SINCLAIR ZX SPECTRUM",
}

def load_official_fullnames():
    mapping = {}
    # es_systems.xml
    try:
        tree = ET.parse(ES_SYSTEMS_XML)
        for sys in tree.getroot().findall("system"):
            n = sys.findtext("name")
            f = sys.findtext("fullname")
            if n and f:
                mapping[n] = f.upper()
    except Exception:
        pass
    # systems.json
    try:
        with open(SYSTEMS_JSON) as f:
            data = json.load(f)
        for sys in data.get("systems", data if isinstance(data, list) else []):
            n = sys.get("name")
            f = sys.get("fullname")
            if n and f:
                mapping[n] = f.upper()
    except Exception:
        pass
    return mapping

def get_fullname(system_id, official):
    return official.get(system_id) or BUILTIN.get(system_id)

def add_fullname_to_theme(theme_path, fullname):
    with open(theme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "systemfullname" in content:
        print(f"  [SKIP] 이미 존재")
        return False

    insert = (
        '    <text name="systemfullname" extra="true">\n'
        f'      <text>{fullname}</text>\n'
        '    </text>\n'
    )
    # shortdescription 앞에 삽입
    marker = '    <text name="shortdescription" extra="true">'
    if marker in content:
        new_content = content.replace(marker, insert + marker, 1)
    else:
        # shortdescription 없으면 </view> 앞에 삽입
        new_content = content.replace('  </view>', insert + '  </view>', 1)

    with open(theme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  [OK] {fullname}")
    return True

def main():
    official = load_official_fullnames()
    print(f"공식 소스에서 {len(official)}개 로드\n")

    updated, skipped, missing = 0, 0, []

    for entry in sorted(os.listdir(THEME_DIR)):
        system_dir = os.path.join(THEME_DIR, entry)
        theme_path = os.path.join(system_dir, "theme.xml")
        if not os.path.isdir(system_dir) or not os.path.isfile(theme_path):
            continue
        if entry.startswith("_"):
            continue

        fullname = get_fullname(entry, official)
        if not fullname:
            print(f"{entry}: [MISSING] 매핑 없음")
            missing.append(entry)
            continue

        print(f"{entry}:")
        result = add_fullname_to_theme(theme_path, fullname)
        if result:
            updated += 1
        else:
            skipped += 1

    print(f"\n완료: {updated}개 추가, {skipped}개 스킵, {len(missing)}개 미매칭")
    if missing:
        print(f"수동 확인 필요: {', '.join(missing)}")

if __name__ == "__main__":
    main()
