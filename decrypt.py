from PIL import Image
import random

# Load image
def load_image(path):
    return Image.open(path)

# Save image
def save_image(image, path):
    image.save(path)

# Reverse swaps using the same seed
def generate_swap_log(width, height, total_swaps, seed=42):
    random.seed(seed)
    swaps = []
    for _ in range(total_swaps):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        swaps.append(((x1, y1), (x2, y2)))
    return swaps

def reverse_swaps(image, swap_log):
    pixels = image.load()
    for (x1, y1), (x2, y2) in reversed(swap_log):
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    return image

# --- Main ---
if __name__ == "__main__":
    # Load the encrypted image
    img = load_image("encrypted_swapped.png")
    width, height = img.size
    total_swaps = width * height

    # Generate same swap log
    swaps = generate_swap_log(width, height, total_swaps, seed=42)

    # Reverse the swaps
    decrypted = reverse_swaps(img.copy(), swaps)
    save_image(decrypted, "decrypted_swapped.png")

    print("Decryption complete! Check decrypted_swapped.png")
