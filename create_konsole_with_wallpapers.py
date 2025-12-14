#!/usr/bin/env python3
"""
Create Konsole profiles with embedded wallpapers
Each profile gets its own color scheme with the wallpaper built in
"""

from pathlib import Path

def create_profile_with_wallpaper(profile_info):
    """Create a complete Konsole profile with embedded wallpaper"""
    konsole_dir = Path.home() / ".local" / "share" / "konsole"
    konsole_dir.mkdir(parents=True, exist_ok=True)

    profile_name = profile_info['profile_name']
    image_path = profile_info['image']
    color_type = profile_info['color_type']

    # Color definitions based on background type
    color_defs = {
        'bright': {
            'Foreground': '230,230,230',
            'Background': '10,10,10',
            'BackgroundIntense': '30,30,30',
            'Color0': '40,40,40',
            'Color1': '255,100,100',
            'Color2': '100,255,100',
            'Color3': '255,255,100',
            'Color4': '100,150,255',
            'Color5': '255,100,255',
            'Color6': '100,255,255',
            'Color7': '240,240,240',
            'Color0Intense': '100,100,100',
            'Color1Intense': '255,150,150',
            'Color2Intense': '150,255,150',
            'Color3Intense': '255,255,150',
            'Color4Intense': '150,200,255',
            'Color5Intense': '255,150,255',
            'Color6Intense': '150,255,255',
            'Color7Intense': '255,255,255',
        },
        'light': {
            'Foreground': '240,240,240',
            'Background': '20,20,25',
            'BackgroundIntense': '40,40,45',
            'Color0': '50,50,50',
            'Color1': '255,120,120',
            'Color2': '120,255,120',
            'Color3': '255,255,120',
            'Color4': '120,180,255',
            'Color5': '255,120,255',
            'Color6': '120,255,255',
            'Color7': '250,250,250',
            'Color0Intense': '120,120,120',
            'Color1Intense': '255,160,160',
            'Color2Intense': '160,255,160',
            'Color3Intense': '255,255,160',
            'Color4Intense': '160,210,255',
            'Color5Intense': '255,160,255',
            'Color6Intense': '160,255,255',
            'Color7Intense': '255,255,255',
        },
        'dark': {
            'Foreground': '40,40,40',
            'Background': '240,240,240',
            'BackgroundIntense': '220,220,220',
            'Color0': '20,20,20',
            'Color1': '180,0,0',
            'Color2': '0,150,0',
            'Color3': '180,140,0',
            'Color4': '0,80,180',
            'Color5': '180,0,180',
            'Color6': '0,150,150',
            'Color7': '200,200,200',
            'Color0Intense': '80,80,80',
            'Color1Intense': '220,0,0',
            'Color2Intense': '0,200,0',
            'Color3Intense': '220,180,0',
            'Color4Intense': '0,120,220',
            'Color5Intense': '220,0,220',
            'Color6Intense': '0,200,200',
            'Color7Intense': '255,255,255',
        },
        'medium': {
            'Foreground': '220,220,220',
            'Background': '30,30,35',
            'BackgroundIntense': '50,50,55',
            'Color0': '45,45,45',
            'Color1': '255,110,110',
            'Color2': '110,255,110',
            'Color3': '255,255,110',
            'Color4': '110,170,255',
            'Color5': '255,110,255',
            'Color6': '110,255,255',
            'Color7': '245,245,245',
            'Color0Intense': '110,110,110',
            'Color1Intense': '255,150,150',
            'Color2Intense': '150,255,150',
            'Color3Intense': '255,255,150',
            'Color4Intense': '150,200,255',
            'Color5Intense': '255,150,255',
            'Color6Intense': '150,255,255',
            'Color7Intense': '255,255,255',
        }
    }

    colors = color_defs[color_type]
    colorscheme_name = f"{profile_name}Colors"

    # Create color scheme with wallpaper
    colorscheme_file = konsole_dir / f"{colorscheme_name}.colorscheme"
    colorscheme_content = f"""[Background]
Color={colors['Background']}

[BackgroundFaint]
Color={colors['Background']}

[BackgroundIntense]
Color={colors['BackgroundIntense']}

[Color0]
Color={colors['Color0']}

[Color0Faint]
Color={colors['Color0']}

[Color0Intense]
Color={colors['Color0Intense']}

[Color1]
Color={colors['Color1']}

[Color1Faint]
Color={colors['Color1']}

[Color1Intense]
Color={colors['Color1Intense']}

[Color2]
Color={colors['Color2']}

[Color2Faint]
Color={colors['Color2']}

[Color2Intense]
Color={colors['Color2Intense']}

[Color3]
Color={colors['Color3']}

[Color3Faint]
Color={colors['Color3']}

[Color3Intense]
Color={colors['Color3Intense']}

[Color4]
Color={colors['Color4']}

[Color4Faint]
Color={colors['Color4']}

[Color4Intense]
Color={colors['Color4Intense']}

[Color5]
Color={colors['Color5']}

[Color5Faint]
Color={colors['Color5']}

[Color5Intense]
Color={colors['Color5Intense']}

[Color6]
Color={colors['Color6']}

[Color6Faint]
Color={colors['Color6']}

[Color6Intense]
Color={colors['Color6Intense']}

[Color7]
Color={colors['Color7']}

[Color7Faint]
Color={colors['Color7']}

[Color7Intense]
Color={colors['Color7Intense']}

[Foreground]
Color={colors['Foreground']}

[ForegroundFaint]
Color={colors['Foreground']}

[ForegroundIntense]
Color={colors['Foreground']}

[General]
Blur=false
ColorRandomization=false
Description={profile_name}
Opacity=0.85
Wallpaper={image_path}
WallpaperFlipType=NoFlip
WallpaperOpacity=0.6
"""

    with open(colorscheme_file, 'w') as f:
        f.write(colorscheme_content)

    # Create profile
    profile_file = konsole_dir / f"{profile_name}.profile"
    profile_content = f"""[Appearance]
ColorScheme={colorscheme_name}
Font=Hack,11,-1,5,50,0,0,0,0,0
LineSpacing=0
UseFontLineChararacters=true

[General]
Command=/bin/bash
Name={profile_name}
Parent=FALLBACK/

[Interaction Options]
UnderlineFilesEnabled=true

[Scrolling]
HistorySize=10000
ScrollBarPosition=2

[Terminal Features]
BlinkingCursorEnabled=true
"""

    with open(profile_file, 'w') as f:
        f.write(profile_content)

    return {
        'profile': str(profile_file),
        'colorscheme': str(colorscheme_file),
        'name': profile_name
    }

def main():
    # Profile definitions
    profiles = [
        {'profile_name': 'Forest_MistyMorning', 'image': str(Path.home() / 'Pictures/konsole_forests/01_misty_morning.png'), 'color_type': 'light'},
        {'profile_name': 'Forest_DarkEvergreen', 'image': str(Path.home() / 'Pictures/konsole_forests/02_dark_evergreen.png'), 'color_type': 'bright'},
        {'profile_name': 'Forest_AutumnGlow', 'image': str(Path.home() / 'Pictures/konsole_forests/03_autumn_glow.png'), 'color_type': 'dark'},
        {'profile_name': 'Forest_BambooZen', 'image': str(Path.home() / 'Pictures/konsole_forests/04_bamboo_zen.png'), 'color_type': 'medium'},
        {'profile_name': 'Forest_SnowyPines', 'image': str(Path.home() / 'Pictures/konsole_forests/05_snowy_pines.png'), 'color_type': 'dark'},
        {'profile_name': 'Forest_TropicalRainforest', 'image': str(Path.home() / 'Pictures/konsole_forests/06_tropical_rainforest.png'), 'color_type': 'bright'},
        {'profile_name': 'Forest_SunsetCanopy', 'image': str(Path.home() / 'Pictures/konsole_forests/07_sunset_canopy.png'), 'color_type': 'bright'},
        {'profile_name': 'Forest_MossyGrove', 'image': str(Path.home() / 'Pictures/konsole_forests/08_mossy_grove.png'), 'color_type': 'light'},
        {'profile_name': 'Forest_BirchMinimal', 'image': str(Path.home() / 'Pictures/konsole_forests/09_birch_minimal.png'), 'color_type': 'dark'},
        {'profile_name': 'Forest_NightForest', 'image': str(Path.home() / 'Pictures/konsole_forests/10_night_forest.png'), 'color_type': 'bright'},
    ]

    print("=" * 70)
    print("Creating Complete Konsole Forest Profiles with Wallpapers")
    print("=" * 70)
    print()

    created = []
    for profile in profiles:
        result = create_profile_with_wallpaper(profile)
        created.append(result)
        print(f"✓ Created: {result['name']}")
        print(f"  Profile: {result['profile']}")
        print(f"  Colors: {result['colorscheme']}")
        print(f"  Wallpaper: {profile['image']}")
        print()

    print("=" * 70)
    print(f"Successfully created {len(created)} complete profiles!")
    print("=" * 70)
    print()
    print("To use:")
    print("1. Open Konsole")
    print("2. Settings → Manage Profiles")
    print("3. Select any Forest_* profile")
    print("4. Wallpapers are already configured!")
    print()
    print("Note: If wallpapers don't appear, restart Konsole")
    print()

if __name__ == "__main__":
    main()
