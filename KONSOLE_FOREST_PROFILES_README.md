# Konsole Forest Profiles

10 beautiful high-resolution forest backgrounds with optimized color schemes for Konsole terminal.

## What's Included

### Images (1792x1024 HD)
Located in: `~/Pictures/konsole_forests/`

1. **Misty Morning** - Blue-gray misty dawn redwoods
2. **Dark Evergreen** - Almost black twilight pine forest
3. **Autumn Glow** - Golden and amber fall foliage
4. **Bamboo Zen** - Serene bamboo grove
5. **Snowy Pines** - Winter wonderland snow-covered pines
6. **Tropical Rainforest** - Lush green tropical vegetation
7. **Sunset Canopy** - Golden hour forest canopy
8. **Mossy Grove** - Ancient moss-covered oaks
9. **Birch Minimal** - Minimalist white birch forest
10. **Night Forest** - Dark mysterious moonlit forest

### Konsole Profiles
Located in: `~/.local/share/konsole/`

- 10 pre-configured profiles (one per forest theme)
- 4 optimized color schemes:
  - **ForestBright** - Bright colors for dark backgrounds
  - **ForestLight** - Light colors for medium backgrounds
  - **ForestDark** - Dark colors for bright backgrounds
  - **ForestMedium** - Balanced colors for medium tones

## Profile Details

| Profile | Image | Color Scheme | Best For |
|---------|-------|--------------|----------|
| Forest_MistyMorning | 01_misty_morning.png | ForestLight | Soft, easy on eyes |
| Forest_DarkEvergreen | 02_dark_evergreen.png | ForestBright | High contrast coding |
| Forest_AutumnGlow | 03_autumn_glow.png | ForestDark | Warm aesthetic |
| Forest_BambooZen | 04_bamboo_zen.png | ForestMedium | Focused work |
| Forest_SnowyPines | 05_snowy_pines.png | ForestDark | Clean minimal look |
| Forest_TropicalRainforest | 06_tropical_rainforest.png | ForestBright | Vibrant environment |
| Forest_SunsetCanopy | 07_sunset_canopy.png | ForestBright | Warm dramatic tones |
| Forest_MossyGrove | 08_mossy_grove.png | ForestLight | Mystical atmosphere |
| Forest_BirchMinimal | 09_birch_minimal.png | ForestDark | Ultra-clean Nordic |
| Forest_NightForest | 10_night_forest.png | ForestBright | Late night coding |

## How to Use

### Method 1: Select Profile in Konsole

1. Open Konsole
2. Go to **Settings → Manage Profiles**
3. Select any **Forest_*** profile
4. Click **Set as Default** (optional)

### Method 2: Set Wallpaper Manually

The profiles are configured with color schemes, but wallpapers must be set manually:

1. Open Konsole with a Forest profile active
2. Go to **Settings → Edit Current Profile**
3. Click **Appearance** tab
4. Click **Edit...** next to the Color Scheme
5. Go to **Background** tab
6. Select **Image** as background mode
7. Click **Choose...** and navigate to `~/Pictures/konsole_forests/`
8. Select the corresponding numbered image for your profile
9. Adjust **Opacity** if desired (recommended: 0.8-0.9)
10. Click **OK** to save

### Quick Reference Script

Run this for the image mapping:
```bash
~/Documents/PythonScripts/TokenHUD/set_wallpapers_auto.sh
```

## Color Scheme Features

Each color scheme is optimized for:
- High readability
- Proper contrast with background
- Easy distinction between colors (errors, success, info)
- Semi-transparent background (90% opacity)
- Professional appearance

### Color Scheme Breakdown

**ForestBright** (for dark backgrounds):
- Very bright foreground (230,230,230)
- High contrast colors
- Perfect for night forest, dark evergreen, tropical rainforest

**ForestLight** (for misty/medium backgrounds):
- Bright but not harsh (240,240,240)
- Soft color tones
- Perfect for misty morning, mossy grove

**ForestDark** (for bright backgrounds):
- Dark text (40,40,40)
- Muted colors
- Perfect for snowy pines, autumn glow, birch minimal

**ForestMedium** (balanced):
- Medium brightness (220,220,220)
- Versatile colors
- Perfect for bamboo zen

## Files Created

**Scripts:**
- `generate_forest_collection.py` - DALL-E image generator
- `create_konsole_profiles.py` - Profile and color scheme creator
- `setup_konsole_forest_profiles.py` - Main setup script
- `set_wallpapers_auto.sh` - Helper script with instructions

**Generated:**
- 10 HD forest images (2.2-3.8 MB each, ~30 MB total)
- 10 Konsole profile files
- 4 Konsole color scheme files

## Tips

1. **Opacity:** Adjust background opacity in color scheme editor for better text visibility
2. **Font:** Profiles use Hack font - install for best experience: `sudo zypper install hack-fonts`
3. **Switching:** Create keyboard shortcuts for quick profile switching
4. **Customization:** Edit color schemes to match your preferences
5. **Performance:** HD images may impact startup time on slower systems

## Troubleshooting

**Profiles don't appear:**
- Restart Konsole
- Check files exist in `~/.local/share/konsole/`

**Colors look wrong:**
- Ensure you selected the correct color scheme for the profile
- Try adjusting opacity

**Wallpaper not showing:**
- Wallpapers must be set manually (see Method 2 above)
- Check image path is correct

**Text hard to read:**
- Increase background opacity in color scheme settings
- Try a different color scheme variant

## Generation Details

- **AI Model:** DALL-E 3
- **Resolution:** 1792x1024 (HD landscape)
- **Quality:** HD
- **Format:** PNG
- **Average Size:** 3 MB per image
- **Generation Time:** ~5 minutes total
- **Color Optimization:** Custom RGB palettes for terminal use

## License

Images generated by DALL-E 3 for personal use.
