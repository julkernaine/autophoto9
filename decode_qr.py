#decoding qr code
def dec_qr():
    from pyzbar.pyzbar import decode
    from PIL import Image
    qr_decode = decode(Image.open('QR_image.png'))
    print('The decoded QR is: ' + qr_decode[0].data.decode('ascii'))
dec_qr()