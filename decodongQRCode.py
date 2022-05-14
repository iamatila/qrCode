from  pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/user/PycharmProjects/qrCode/qrcodesImages/myQrCode0.png')

result = decode(img)

print(result)