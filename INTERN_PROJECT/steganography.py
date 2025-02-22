import cv2
import numpy as np
import binascii

# Function to convert text to binary
def text_to_bin(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Function to convert binary to text
def bin_to_text(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 0)

# Function to hide data inside an image
def encode_image(image_path, secret_message, output_path):
    image = cv2.imread(image_path)
    binary_secret = text_to_bin(secret_message) + '1111111111111110'  # Delimiter
    
    data_index = 0
    total_bytes = len(binary_secret)
    height, width, _ = image.shape
    
    for row in range(height):
        for col in range(width):
            for channel in range(3):
                if data_index < total_bytes:
                    image[row, col, channel] = (image[row, col, channel] & 254) | int(binary_secret[data_index])
                    data_index += 1
    
    cv2.imwrite(output_path, image)
    print("Data successfully encoded into image.")

# Function to extract hidden data from an image
def decode_image(image_path):
    image = cv2.imread(image_path)
    binary_data = ""
    
    for row in image:
        for pixel in row:
            for channel in pixel:
                binary_data += str(channel & 1)
    
    delimiter = "1111111111111110"
    end_index = binary_data.find(delimiter)
    hidden_message = bin_to_text(binary_data[:end_index])
    print("Decoded Message:", hidden_message)
    return hidden_message

# Example usage
if __name__ == "__main__":
    choice = input("Enter 'e' to encode or 'd' to decode: ")
    
    if choice == 'e':
        image_path = input("Enter image path: ")
        secret_message = input("Enter secret message: ")
        output_path = "encoded_image.png"
        encode_image(image_path, secret_message, output_path)
    elif choice == 'd':
        image_path = input("Enter image path: ")
        decode_image(image_path)
    else:
        print("Invalid choice!")
