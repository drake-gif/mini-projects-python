QR Code Generator

A simple command-line Python script that turns any URL or text into a QR code image. Type in what you want to encode, pick a filename and the script saves a ready-to-use PNG.

Features

- Encodes any URL or plain text
- Lets you choose the output filename (defaults to `qrcode.png`)
- Automatically adjusts the QR code size to fit your data
- Uses medium error correction (~15% recovery), so the code still scans if slightly damaged or smudged
- Easy to customize colors, size, and border

Requirements

- Python 3.6 or newer
- The [`qrcode`](https://pypi.org/project/qrcode/) library with Pillow support

Installation

From the folders terminal, install the dependencies with pip:

```bash
pip install "qrcode[pil]"
```

Usage
--> Clone the repository from git hub:  ``` git clone https://github.com/drake-gif/mini-projects-python ```
Cd to qr generator folder to find the qr_generator.py

1. Run the script:

   ```bash
   python qr_generator.py
   ```

2. Enter the URL or text you want to encode.
3. Enter an output filename, or press **Enter** to use the default `qrcode.png`.

### Example session

```
Enter the URL or text to encode: https://github.com
Enter output filename (e.g., my_qr.png): github_qr.png
Success! QR code saved as github_qr.png
```

The QR code image is saved in the folder you ran the script from.
