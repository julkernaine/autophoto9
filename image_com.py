#image_compression
def comp_img():
    import PIL
    from PIL import Image 
    img = Image.open('picture.jpg')
    img.save("image_compressed.jpg", optimize = True, quality = 10)
    print("Image has been compressed.")
comp_img()
