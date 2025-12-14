#!/usr/bin/env python3
"""
Create Konsole profiles with optimized color schemes for forest backgrounds
"""

from pathlib import Path
import json

def create_konsole_profiles(images_info):
    """
    Create Konsole profile files with appropriate color schemes
    """
    konsole_dir = Path.home() / ".local" / "share" / "konsole"
    konsole_dir.mkdir(parents=True, exist_ok=True)

    # Color schemes optimized for different background types
    color_schemes = {
        "bright": {
            # For dark backgrounds - bright, high contrast colors
            "name": "ForestBright",
            "Foreground": "230,230,230",
            "Background": "10,10,10,180",  # Semi-transparent dark
            "Color0": "40,40,40",      # Black
            "Color1": "255,100,100",   # Red
            "Color2": "100,255,100",   # Green
            "Color3": "255,255,100",   # Yellow
            "Color4": "100,150,255",   # Blue
            "Color5": "255,100,255",   # Magenta
            "Color6": "100,255,255",   # Cyan
            "Color7": "240,240,240",   # White
            "Color0Intense": "100,100,100",
            "Color1Intense": "255,150,150",
            "Color2Intense": "150,255,150",
            "Color3Intense": "255,255,150",
            "Color4Intense": "150,200,255",
            "Color5Intense": "255,150,255",
            "Color6Intense": "150,255,255",
            "Color7Intense": "255,255,255",
        },
        "light": {
            # For medium/misty backgrounds - soft but visible
            "name": "ForestLight",
            "Foreground": "240,240,240",
            "Background": "20,20,25,160",
            "Color0": "50,50,50",
            "Color1": "255,120,120",
            "Color2": "120,255,120",
            "Color3": "255,255,120",
            "Color4": "120,180,255",
            "Color5": "255,120,255",
            "Color6": "120,255,255",
            "Color7": "250,250,250",
            "Color0Intense": "120,120,120",
            "Color1Intense": "255,160,160",
            "Color2Intense": "160,255,160",
            "Color3Intense": "255,255,160",
            "Color4Intense": "160,210,255",
            "Color5Intense": "255,160,255",
            "Color6Intense": "160,255,255",
            "Color7Intense": "255,255,255",
        },
        "dark": {
            # For bright/light backgrounds - dark, readable text
            "name": "ForestDark",
            "Foreground": "40,40,40",
            "Background": "240,240,240,180",
            "Color0": "20,20,20",
            "Color1": "180,0,0",
            "Color2": "0,150,0",
            "Color3": "180,140,0",
            "Color4": "0,80,180",
            "Color5": "180,0,180",
            "Color6": "0,150,150",
            "Color7": "200,200,200",
            "Color0Intense": "80,80,80",
            "Color1Intense": "220,0,0",
            "Color2Intense": "0,200,0",
            "Color3Intense": "220,180,0",
            "Color4Intense": "0,120,220",
            "Color5Intense": "220,0,220",
            "Color6Intense": "0,200,200",
            "Color7Intense": "255,255,255",
        },
        "medium": {
            # Balanced for medium-toned backgrounds
            "name": "ForestMedium",
            "Foreground": "220,220,220",
            "Background": "30,30,35,170",
            "Color0": "45,45,45",
            "Color1": "255,110,110",
            "Color2": "110,255,110",
            "Color3": "255,255,110",
            "Color4": "110,170,255",
            "Color5": "255,110,255",
            "Color6": "110,255,255",
            "Color7": "245,245,245",
            "Color0Intense": "110,110,110",
            "Color1Intense": "255,150,150",
            "Color2Intense": "150,255,150",
            "Color3Intense": "255,255,150",
            "Color4Intense": "150,200,255",
            "Color5Intense": "255,150,255",
            "Color6Intense": "150,255,255",
            "Color7Intense": "255,255,255",
        }
    }

    created_profiles = []
    created_colorschemes = []

    # Create color scheme files
    for scheme_name, colors in color_schemes.items():
        colorscheme_file = konsole_dir / f"{colors['name']}.colorscheme"

        colorscheme_content = f"""[Background]
Color={colors['Background']}

[BackgroundIntense]
Color={colors['Background']}

[Color0]
Color={colors['Color0']}

[Color0Intense]
Color={colors['Color0Intense']}

[Color1]
Color={colors['Color1']}

[Color1Intense]
Color={colors['Color1Intense']}

[Color2]
Color={colors['Color2']}

[Color2Intense]
Color={colors['Color2Intense']}

[Color3]
Color={colors['Color3']}

[Color3Intense]
Color={colors['Color3Intense']}

[Color4]
Color={colors['Color4']}

[Color4Intense]
Color={colors['Color4Intense']}

[Color5]
Color={colors['Color5']}

[Color5Intense]
Color={colors['Color5Intense']}

[Color6]
Color={colors['Color6']}

[Color6Intense]
Color={colors['Color6Intense']}

[Color7]
Color={colors['Color7']}

[Color7Intense]
Color={colors['Color7Intense']}

[Foreground]
Color={colors['Foreground']}

[ForegroundIntense]
Color={colors['Foreground']}

[General]
Description={colors['name']}
Opacity=0.9
Wallpaper=
"""

        with open(colorscheme_file, 'w') as f:
            f.write(colorscheme_content)

        created_colorschemes.append(str(colorscheme_file))
        print(f"  ✓ Created color scheme: {colors['name']}")

    # Create profile for each image
    for img in images_info:
        profile_name = f"Forest_{img['name'].title().replace('_', '')}"
        profile_file = konsole_dir / f"{profile_name}.profile"

        color_scheme_name = color_schemes[img['colors']]['name']

        profile_content = f"""[Appearance]
ColorScheme={color_scheme_name}
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

[Terminal Features]
BlinkingCursorEnabled=true
"""

        with open(profile_file, 'w') as f:
            f.write(profile_content)

        created_profiles.append({
            'profile': str(profile_file),
            'name': profile_name,
            'image': img['path'],
            'colorscheme': color_scheme_name
        })

        print(f"  ✓ Created profile: {profile_name}")

    return created_profiles, created_colorschemes

def create_wallpaper_script(profiles_info):
    """
    Create a helper script to set wallpapers for profiles
    (Konsole doesn't support wallpapers directly in profiles, needs manual setting)
    """
    script_path = Path.home() / "Documents" / "PythonScripts" / "TokenHUD" / "set_konsole_wallpapers.sh"

    script_content = """#!/bin/bash
# Helper script to set Konsole wallpapers
# Konsole profiles don't directly support wallpaper setting via config files
# You need to manually set them or use this as a reference

echo "Konsole Profile Wallpaper Setup Instructions"
echo "=============================================="
echo ""
echo "To set wallpapers for each profile:"
echo "1. Open Konsole"
echo "2. Go to Settings > Edit Current Profile"
echo "3. Select the Appearance tab"
echo "4. Click 'Edit...' next to Color scheme"
echo "5. Go to the Background tab"
echo "6. Set the wallpaper image for each profile"
echo ""
echo "Profile to Image Mapping:"
echo "========================="
"""

    for profile in profiles_info:
        script_content += f'\necho "{profile["name"]} -> {profile["image"]}"\n'

    script_content += """
echo ""
echo "Or use kreadconfig6/kwriteconfig6 to automate (if available)"
echo "=============================================="
"""

    with open(script_path, 'w') as f:
        f.write(script_content)

    script_path.chmod(0o755)
    return str(script_path)

if __name__ == "__main__":
    # This will be called from the main script
    pass
