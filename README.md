# Secure Data Hiding in Image Using Steganography

## 📌 Project Description
This project implements **steganography** to securely hide data inside images using the **Least Significant Bit (LSB) technique**. The system allows users to **embed** secret messages into an image and later **extract** them without noticeable changes to the image. 

## 🔥 Features
- **Secure Data Hiding:** Conceals secret messages within an image file.
- **LSB Technique:** Uses Least Significant Bit modification for imperceptible changes.
- **Encryption Support:** Adds extra security using encryption before embedding data.
- **User-Friendly Interface:** Web-based interface for easy interaction.
- **Data Extraction:** Extracts hidden messages without degrading the image quality.

## 📌 Technologies Used
- **Programming Language:** Python 🐍
- **Libraries:** OpenCV, NumPy, Pillow (PIL), Cryptography
- **Framework:** Flask (for web-based interface)
- **Algorithm:** LSB (Least Significant Bit)

## 🚀 Installation Guide
### Step 1: Clone the Repository
```bash
 git clone https://github.com/your-username/secure-steganography.git
 cd secure-steganography
```

### Step 2: Install Dependencies
```bash
 pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
 python app.py
```
Access the web interface at `http://127.0.0.1:5000/`

## 🎯 Usage
### **1. Hide a Secret Message**
- Upload an image.
- Enter the secret message.
- Encrypt the message (optional).
- Download the stego image with the hidden message.

### **2. Extract Hidden Message**
- Upload the stego image.
- Enter the decryption key (if applied).
- Retrieve the hidden message.

## 📸 Screenshots
| Image Upload | Data Extraction |
|-------------|----------------|
| ![Upload](screenshots/upload.png) | ![Extract](screenshots/extract.png) |

## 🔮 Future Scope
- AI-based Steganalysis Resistance
- Support for Video & Audio Steganography
- Blockchain Integration for Secure Data Sharing

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the project and contribute improvements.

## 📜 License
This project is licensed under the MIT License.

## 🔗 GitHub Repository
[Secure Data Hiding in Image Using Steganography](https://github.com/Raje0906/Edunet_Internship_cybersecurity.git)

---

**Developed by Aditya Raje**
