#!/usr/bin/env python3
"""
Generate 10 high-res forest images with different themes
Each optimized for terminal backgrounds
"""

import os
from openai import OpenAI
from datetime import datetime
from pathlib import Path
import httpx
import time

def generate_forest_images():
    # Setup
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        return []

    client = OpenAI(api_key=api_key)
    output_dir = Path.home() / "Pictures" / "konsole_forests"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 10 different forest themes optimized for terminal backgrounds
    forest_prompts = [
        {
            "name": "misty_morning",
            "prompt": "Ancient misty forest at dawn, soft blue-gray fog rolling through massive redwood trees, ethereal atmosphere, muted tones perfect for terminal background, peaceful and minimal, professional nature photography",
            "colors": "light"  # Will use light text colors
        },
        {
            "name": "dark_evergreen",
            "prompt": "Deep dark pine forest at twilight, almost black tree silhouettes, very dark atmospheric background perfect for bright terminal text, moody and dramatic, minimal light sources, cinematic photography",
            "colors": "bright"  # Will use bright text colors
        },
        {
            "name": "autumn_glow",
            "prompt": "Autumn forest with golden and amber leaves, warm orange and brown tones, soft diffused lighting, perfect depth for terminal text overlay, fall foliage, professional landscape photography",
            "colors": "dark"  # Will use dark text colors for contrast
        },
        {
            "name": "bamboo_zen",
            "prompt": "Serene bamboo forest with straight vertical stalks, filtered green light, minimalist composition ideal for terminal background, zen aesthetic, shallow depth of field, nature photography",
            "colors": "medium"  # Balanced colors
        },
        {
            "name": "snowy_pines",
            "prompt": "Snow-covered pine forest in winter, white and blue tones, frosted trees, clean minimal aesthetic perfect for terminal display, crisp and bright, professional winter photography",
            "colors": "dark"  # Dark text on light background
        },
        {
            "name": "tropical_rainforest",
            "prompt": "Lush tropical rainforest with vibrant green foliage, palm fronds and ferns, dappled sunlight, rich colors but balanced for text readability, exotic flora, nature photography",
            "colors": "bright"  # Bright text
        },
        {
            "name": "sunset_canopy",
            "prompt": "Forest canopy at sunset, warm golden hour light filtering through leaves, orange and purple sky visible through branches, perfect depth for terminal overlay, dramatic lighting, landscape photography",
            "colors": "bright"  # Bright contrasting text
        },
        {
            "name": "mossy_grove",
            "prompt": "Ancient moss-covered oak forest, deep green tones, twisted branches, mystical atmosphere, perfect texture for terminal background without being too busy, soft natural lighting, fantasy-like photography",
            "colors": "light"  # Light text colors
        },
        {
            "name": "birch_minimal",
            "prompt": "Minimalist birch forest with white bark trees, soft gray-blue background, very clean composition ideal for terminal text display, Nordic aesthetic, professional minimalist photography",
            "colors": "dark"  # Dark text for contrast
        },
        {
            "name": "night_forest",
            "prompt": "Dark forest at night with subtle moonlight, very dark background perfect for bright terminal text, mysterious atmosphere, deep shadows, only hints of tree silhouettes, cinematic night photography",
            "colors": "bright"  # Brightest text colors
        }
    ]

    generated_images = []

    for i, theme in enumerate(forest_prompts, 1):
        print(f"\n[{i}/10] Generating: {theme['name']}")
        print(f"Theme: {theme['prompt'][:80]}...")

        try:
            # Generate image
            response = client.images.generate(
                model="dall-e-3",
                prompt=theme['prompt'],
                size="1792x1024",  # HD landscape format
                quality="hd",
                n=1
            )

            # Download and save
            image_url = response.data[0].url
            filename = f"{i:02d}_{theme['name']}.png"
            filepath = output_dir / filename

            print(f"  Downloading...")
            img_response = httpx.get(image_url)

            with open(filepath, 'wb') as f:
                f.write(img_response.content)

            size_mb = filepath.stat().st_size / 1024 / 1024
            print(f"  ✓ Saved: {filepath.name} ({size_mb:.2f} MB)")

            generated_images.append({
                'path': str(filepath),
                'name': theme['name'],
                'colors': theme['colors'],
                'number': i
            })

            # Rate limiting - wait between requests
            if i < len(forest_prompts):
                print("  Waiting 3 seconds...")
                time.sleep(3)

        except Exception as e:
            print(f"  ✗ Error: {e}")
            continue

    return generated_images

if __name__ == "__main__":
    print("=" * 70)
    print("Generating 10 High-Res Forest Images for Konsole Backgrounds")
    print("=" * 70)

    images = generate_forest_images()

    print("\n" + "=" * 70)
    print(f"Complete! Generated {len(images)} images")
    print("=" * 70)

    for img in images:
        print(f"  {img['number']:2d}. {img['name']:20s} -> {img['path']}")
