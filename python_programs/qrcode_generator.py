import qrcode as qr
from PIL import Image

code = qr.QRCode(version=1, error_correction=qr.ERROR_CORRECT_H,
                 box_size=10, border=4)

code.add_data("https://github.com/HyPhen404")
code.make(fit=True)

image = code.make_image(fill_color="cyan", back_color="grey")

image.save("Github_qrcode.png")
