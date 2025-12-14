#!/bin/bash
# Automatically set wallpapers for Konsole color schemes

KONSOLE_DIR="$HOME/.local/share/konsole"
IMAGES_DIR="$HOME/Pictures/konsole_forests"

echo "Setting wallpapers for Konsole color schemes..."
echo "================================================"

# Function to set wallpaper for a color scheme
set_wallpaper() {
    local colorscheme="$1"
    local wallpaper="$2"
    local colorscheme_file="$KONSOLE_DIR/${colorscheme}.colorscheme"

    if [ -f "$colorscheme_file" ]; then
        # Add wallpaper setting to colorscheme
        if grep -q "^\[General\]" "$colorscheme_file"; then
            # Update existing [General] section
            sed -i "/^\[General\]/a Wallpaper=$wallpaper" "$colorscheme_file"
            # Remove duplicate Wallpaper lines (keep only first)
            awk '!seen[$0]++ || !/^Wallpaper=/' "$colorscheme_file" > "${colorscheme_file}.tmp"
            mv "${colorscheme_file}.tmp" "$colorscheme_file"
        fi
        echo "✓ Set wallpaper for $colorscheme"
    else
        echo "✗ Color scheme file not found: $colorscheme_file"
    fi
}

# Note: Konsole doesn't directly support wallpapers in colorschemes
# Wallpapers need to be set manually per profile
echo ""
echo "NOTE: Konsole requires wallpapers to be set manually for each profile"
echo "      These cannot be set programmatically via color schemes"
echo ""
echo "To set wallpapers:"
echo "1. Open Konsole"
echo "2. Settings > Edit Current Profile > Appearance"
echo "3. Click 'Edit...' next to the Color Scheme"
echo "4. Go to the 'Background' tab"
echo "5. Select 'Image' and choose the corresponding forest image"
echo ""
echo "Profile to Image Mapping:"
echo "========================="
echo ""
echo "Forest_MistyMorning       -> $IMAGES_DIR/01_misty_morning.png"
echo "Forest_DarkEvergreen      -> $IMAGES_DIR/02_dark_evergreen.png"
echo "Forest_AutumnGlow         -> $IMAGES_DIR/03_autumn_glow.png"
echo "Forest_BambooZen          -> $IMAGES_DIR/04_bamboo_zen.png"
echo "Forest_SnowyPines         -> $IMAGES_DIR/05_snowy_pines.png"
echo "Forest_TropicalRainforest -> $IMAGES_DIR/06_tropical_rainforest.png"
echo "Forest_SunsetCanopy       -> $IMAGES_DIR/07_sunset_canopy.png"
echo "Forest_MossyGrove         -> $IMAGES_DIR/08_mossy_grove.png"
echo "Forest_BirchMinimal       -> $IMAGES_DIR/09_birch_minimal.png"
echo "Forest_NightForest        -> $IMAGES_DIR/10_night_forest.png"
echo ""
echo "================================================"
echo "Profiles are ready to use in Konsole!"
echo "================================================"
