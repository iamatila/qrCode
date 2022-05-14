# Encoding QR Code
import qrcode

data = 'Don\'t forget to subscribe'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

pic = qr.make_image(fill_color = 'red', back_color = 'white')

pic.save('C:/Users/user/PycharmProjects/qrCode/qrcodesImages/myQrCode0.png')
