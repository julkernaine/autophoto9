#decoding qr code
def dec_qr():
    from pyzbar.pyzbar import decode
    from PIL import Image
    qr_decode = decode(Image.open('QR_image.png')) #opening the qr code

    decoded_text = qr_decode[0].data.decode('ascii')

    #print('The decoded QR is: ' + qr_decode[0].data.decode('ascii'))#decoding the qr into a text
    print('The decoded QR is: ' + decoded_text)
dec_qr()
