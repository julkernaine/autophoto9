import decode_qr
from tkinter import *
window=Tk()

window.title('Auto Image Editor')
window.geometry("300x200")
button_1 = Button(Tk(),text = "Decode QR Code", command =decode_qr.dec_qr)  
button_1.pack()

window.mainloop()
