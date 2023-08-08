import pyqrcode
import png
url= input("Enter your URL:")
text_code=pyqrcode.create(url)
text_code.png("qrcode.png")
print(text_code)