import qrcode


def generate_qr():
  data = input("Enter the URL or text to encode: ").strip()
  filename = (
      input("Enter output filename (e.g., my_qr.png): ").strip() or "qrcode.png"
  )

  # Configure QR code properties
  qr = qrcode.QRCode(
      version=1,  # Controls size (1 to 40)
      error_correction=qrcode.constants.ERROR_CORRECT_M,  # ~15% error recovery
      box_size=10,  # Pixels per box
      border=4,  # Thickness of the white border
  )

  qr.add_data(data)
  qr.make(fit=True)

  # Create and save the image (supports color names or hex codes)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(filename)
  print(f"Success! QR code saved as {filename}")


if __name__ == "__main__":
  generate_qr()
