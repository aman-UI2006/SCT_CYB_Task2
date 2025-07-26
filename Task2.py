from PIL import Image
import random

# Load image
def load_image(path):
    return Image.open(path)

# Save image
def save_image(image, path):
    image.save(path)

# Encrypt using inversion
def encrypt_image(image):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
           pixel = pixels[x, y]
           if len(pixel) == 4:
               r, g, b, a = pixel
               pixels[x, y] = (255 - r, 255 - g, 255 - b, a)
           else:
               r, g, b = pixel
               pixels[x, y] = (255 - r, 255 - g, 255 - b)

    return image

# Swap pixels randomly
def swap_pixels(image, seed=42):
    random.seed(seed)
    pixels = image.load()
    width, height = image.size
    total_swaps = width * height  # Swap every pixel once for better scramble

    for _ in range(total_swaps):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    return image


# Main execution
if __name__ == "__main__":
    img = load_image("input.png")

    encrypted_math = encrypt_image(img.copy())
    save_image(encrypted_math, "encrypted_math.png")

    encrypted_swapped = swap_pixels(img.copy())
    save_image(encrypted_swapped, "encrypted_swapped.png")

    print("Encryption completed! Check the output files.")
