import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def encrypt_image(image_path, key):
    try:
        image = Image.open(image_path)
        width, height = image.size
        pixels = list(image.getdata())
        encrypted_pixels = [(pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key) for pixel in pixels]
        encrypted_image = Image.new('RGB', (width, height))
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image.save('encrypted_' + os.path.basename(image_path))
        print('Encryption Done...')
    except Exception as e:
        print('Error caught : ', str(e))

def decrypt_image(image_path, key):
    try:
        image = Image.open(image_path)
        width, height = image.size
        pixels = list(image.getdata())
        decrypted_pixels = [(pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key) for pixel in pixels]
        decrypted_image = Image.new('RGB', (width, height))
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save('decrypted_' + os.path.basename(image_path))
        print('Decryption Done...')
    except Exception as e:
        print('Error caught : ', str(e))

def browse_file():
    filepath = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", ".jpg.jpeg.png.bmp")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filepath)

def encrypt():
    image_path = entry_path.get()
    key = int(entry_key.get())
    encrypt_image(image_path, key)

def decrypt():
    image_path = entry_path.get()
    key = int(entry_key.get())
    decrypt_image(image_path, key)

root = tk.Tk()
root.title("Image Encryption and Decryption")

label_path = tk.Label(root, text="Image Path:")
label_path.grid(row=0, column=0, padx=5, pady=5)

entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

label_key = tk.Label(root, text="Key:")
label_key.grid(row=1, column=0, padx=5, pady=5)

entry_key = tk.Entry(root, width=10)
entry_key.grid(row=1, column=1, padx=5, pady=5)

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt)
button_encrypt.grid(row=2, column=0, padx=5, pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
button_decrypt.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
