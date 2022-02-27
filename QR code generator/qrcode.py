# First small programm to create basic QR - code
import qrcode as qr

img = qr.make("Rutvik Jaiswal is alway best")
img.save("rutvik.jpeg")


#Some advance program to generate QR code

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,border=10,box_size=50)


qr.add_data("I am the best")
qr.make(fit=True)

img = qr.make_image(fill_color = 'red',back_color ='black')
img.save("rutvik.jpeg")
