#!/usr/bin/env python3
"""
Generate a high-quality forest image using DALL-E 3
"""

import os
from openai import OpenAI
from datetime import datetime
from pathlib import Path
import httpx

def generate_forest_image():
    # Setup
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        return None

    client = OpenAI(api_key=api_key)
    output_dir = Path.home() / "Pictures" / "dalle_generated"
    output_dir.mkdir(parents=True, exist_ok=True)

    # High-quality forest prompt
    prompt = """A breathtaking high-resolution photograph of a pristine ancient forest at golden hour.
    Towering old-growth trees with moss-covered trunks reaching toward the sky, dappled sunlight
    filtering through dense green canopy creating dramatic light rays (god rays).
    Lush ferns carpeting the forest floor, a soft mist hovering near the ground.
    Rich depth of field with incredible detail in the bark textures and foliage.
    Cinematic composition, nature photography, 8K quality, professional landscape photography."""

    print(f"Generating forest image with DALL-E 3...")
    print(f"Prompt: {prompt[:100]}...")

    # Generate image
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",  # High quality landscape format
        quality="hd",       # HD quality
        n=1
    )

    # Download and save
    image_url = response.data[0].url
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"forest_{timestamp}.png"
    filepath = output_dir / filename

    print(f"Downloading image from: {image_url}")

    # Download the image
    img_response = httpx.get(image_url)
    with open(filepath, 'wb') as f:
        f.write(img_response.content)

    print(f"✓ Image saved to: {filepath}")
    print(f"✓ Size: {filepath.stat().st_size / 1024 / 1024:.2f} MB")

    return str(filepath)

if __name__ == "__main__":
    result = generate_forest_image()
    if result:
        print(f"\nSuccess! Your forest image is ready at:\n{result}")
    else:
        print("\nFailed to generate image.")
