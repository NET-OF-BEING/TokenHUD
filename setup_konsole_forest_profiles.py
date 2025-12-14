#!/usr/bin/env python3
"""
Setup Konsole profiles for all forest backgrounds
"""

import sys
from pathlib import Path

# Import the profile creator
sys.path.insert(0, str(Path(__file__).parent))
from create_konsole_profiles import create_konsole_profiles, create_wallpaper_script

def main():
    # Get all generated images
    images_dir = Path.home() / "Pictures" / "konsole_forests"

    if not images_dir.exists():
        print("Error: No forest images found. Run generate_forest_collection.py first.")
        return

    # Get image info
    images_info = [
        {'path': str(images_dir / "01_misty_morning.png"), 'name': 'misty_morning', 'colors': 'light', 'number': 1},
        {'path': str(images_dir / "02_dark_evergreen.png"), 'name': 'dark_evergreen', 'colors': 'bright', 'number': 2},
        {'path': str(images_dir / "03_autumn_glow.png"), 'name': 'autumn_glow', 'colors': 'dark', 'number': 3},
        {'path': str(images_dir / "04_bamboo_zen.png"), 'name': 'bamboo_zen', 'colors': 'medium', 'number': 4},
        {'path': str(images_dir / "05_snowy_pines.png"), 'name': 'snowy_pines', 'colors': 'dark', 'number': 5},
        {'path': str(images_dir / "06_tropical_rainforest.png"), 'name': 'tropical_rainforest', 'colors': 'bright', 'number': 6},
        {'path': str(images_dir / "07_sunset_canopy.png"), 'name': 'sunset_canopy', 'colors': 'bright', 'number': 7},
        {'path': str(images_dir / "08_mossy_grove.png"), 'name': 'mossy_grove', 'colors': 'light', 'number': 8},
        {'path': str(images_dir / "09_birch_minimal.png"), 'name': 'birch_minimal', 'colors': 'dark', 'number': 9},
        {'path': str(images_dir / "10_night_forest.png"), 'name': 'night_forest', 'colors': 'bright', 'number': 10},
    ]

    print("=" * 70)
    print("Setting Up Konsole Forest Profiles")
    print("=" * 70)
    print()

    # Create profiles and color schemes
    print("Creating color schemes...")
    profiles, colorschemes = create_konsole_profiles(images_info)
    print()

    print("=" * 70)
    print(f"Successfully created {len(colorschemes)} color schemes and {len(profiles)} profiles!")
    print("=" * 70)
    print()

    print("Color Schemes:")
    for cs in colorschemes:
        print(f"  ✓ {Path(cs).name}")
    print()

    print("Profiles:")
    for p in profiles:
        print(f"  ✓ {p['name']}")
        print(f"     Image: {p['image']}")
        print(f"     Color Scheme: {p['colorscheme']}")
        print()

    # Create wallpaper helper script
    print("Creating wallpaper setup helper script...")
    script_path = create_wallpaper_script(profiles)
    print(f"  ✓ {script_path}")
    print()

    print("=" * 70)
    print("Setup Complete!")
    print("=" * 70)
    print()
    print("To use the profiles:")
    print("1. Open Konsole")
    print("2. Go to Settings > Manage Profiles")
    print("3. Select any of the Forest* profiles")
    print("4. For wallpapers, you need to manually set them:")
    print("   - Settings > Edit Current Profile > Appearance")
    print("   - Click 'Edit...' next to Color scheme")
    print("   - Go to Background tab")
    print("   - Select 'Image' and browse to the corresponding image")
    print()
    print("Or run the helper script for instructions:")
    print(f"  {script_path}")
    print()

if __name__ == "__main__":
    main()
