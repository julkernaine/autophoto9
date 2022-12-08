
from tkinter import *
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import make_qr
from image_com import comp_img
from convert_image import convert_img
from face_detection import face_det

root = Tk()
root.title('Imagify')


from pyzbar.pyzbar import decode
from PIL import Image

qr_decode = decode(Image.open('QR_image.png'))
decoded_text = qr_decode[0].data.decode('ascii')


root.resizable(False, False)



def myClick():
    myLabel = Label(root, text =("The decoded qr code is: " + decoded_text))
    myLabel.pack()
def myClick1():
    myLabel1 = Label(openNewwWindow, text =("QR Image has been made"))
    myLabel1.pack()
    

def openNewwWindow():
    newWindow = Toplevel(root)
    newWindow.title("Enter Your Text Here")
    newWindow.geometry("500x500")
    e = Entry(newWindow, width=50)
    e.pack()
    e.insert(0, "") 
    
    import pyqrcode , png
    qr_text = pyqrcode.create(e.get())
    qr_text.png("QR_image.png", scale= 5)
    myButtonnew = Button(newWindow, text = "Make QR Code",command = myClick1,height= 5, width=50)
    myButtonnew.pack()

def openNewwWindow1():
    newWindow = Toplevel(root)
    newWindow.title("Enter Your Text Here")
    newWindow.geometry("500x100")
    Label(newWindow,text ="The QR code is : "+ decoded_text).pack()


from tkinter.filedialog import askopenfilename

myButton = Button(root, text = "Decode QR ",command = openNewwWindow1,height= 2, width=50)
myButton1 = Button(root, text = "Select Image",command = askopenfilename,height= 2, width=50)
myButton3 = Button(root, text = "Make a QR Image", command = openNewwWindow,height= 2, width=50)
myButton4 = Button(root, text = "Compress the Image", command = comp_img,height= 2, width=50)
myButton5 = Button(root, text = "Make sketch Art", command = convert_img,height= 2, width=50)
myButton6 = Button(root, text = "Detect the faces", command = face_det,height= 2, width=50)

myButton.pack()
myButton1.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()
myButton6.pack()


root.mainloop()
