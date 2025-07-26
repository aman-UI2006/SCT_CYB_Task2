# SCT_CYB_Task2

# 🛡️ Image Encryption and Decryption Tool

This is my **Task 2 submission** for the SkillCraft internship. It is a simple yet powerful Python tool that performs **image encryption and decryption** using pixel manipulation techniques.

## 📌 Features

- Encrypts images by scrambling pixels using a pseudorandom number generator.
- Decrypts encrypted images using the same random seed.
- Ensures reversible and deterministic image encryption.
- Clean and modular Python code with comments.

---

## 📂 Project Structure

ImageEncryptionTool/
├── encryption.py # Encrypts an image by scrambling pixels
├── decryption.py # Decrypts the scrambled image back to original
├── input_image.png # Original image (any PNG or JPG)
├── encrypted_swapped.png # Output after encryption
├── decrypted_image.png # Output after decryption


## 🔧 How It Works

1. **Encryption (`encryption.py`)**
   - Reads an image using `PIL`
   - Converts the image to pixel data
   - Randomly shuffles pixels using a fixed seed (e.g., `random.seed(42)`)
   - Saves the encrypted image

2. **Decryption (`decryption.py`)**
   - Uses the same random seed
   - Reverses the pixel shuffling
   - Restores the image back to its original form

> The fixed random seed ensures the encryption is reversible and secure for basic use cases.


🧠 Learnings & Experience
Learned about image processing using Pillow

Understood how PRNG works with a fixed seed

Explored the concept of reversible encryption using Python

Improved VS Code usage, GitHub workflow, and documentation skills

📄 License
This project is licensed under the MIT License.

🔗 Connect With Me
📍 Name: Aman Pokale
💼 Internship: SkillCraft
🌐 LinkedIn: www.linkedin.com/in/amanpokale

