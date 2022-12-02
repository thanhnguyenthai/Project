import QRcode
img = QRcode.make('https://www.facebook.com/dddstudio22pl/')
img.save('myQRcode.png')
img.show()