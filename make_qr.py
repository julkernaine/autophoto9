#making a qr code
def make_qr():
    import pyqrcode , png
    text = input("Enter a text/link here: ")
    qr_text = pyqrcode.create(text)
    qr_text.png("QR_image.png", scale= 5)
