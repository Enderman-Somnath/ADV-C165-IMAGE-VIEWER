from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("Planet Encyclopedia")
root.geometry("9999x9999")
root.configure(background="white")

imgpath=""
def Open():
    global imgpath
    imgpath=filedialog.askopenfilename(title = "Select Image File", filetypes= [("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(imgpath)
    img=ImageTk.PhotoImage(Image.open(imgpath))
    label_image.configure(image=img)
    label_image.image=img
def rotate():
    print("Rotate")
    print(imgpath)
    im=Image.open(imgpath)
    rotated_img=im.rotate(180)
    img=ImageTk.PhotoImage(rotated_img)
    label_image.configure(image=img)
    label_image.image=img
    
btn_open=Button(root,text="Open Image",command=Open,relief="flat",font=("verdana",15),bg="#bfbfbf",fg="white",bd=0)
btn_open.place(relx=0.5,rely=0.08,anchor=CENTER)

btn_rotate=Button(root,text="Rotate Image",command=rotate,relief="flat",font=("verdana",15),bg="#bfbfbf",fg="white",bd=0)
btn_rotate.place(relx=0.5,rely=0.8,anchor=CENTER)

label_image=Label(root,bg="blue",fg="blue",height=30,width=100)
label_image.place(rely=0.5,relx=0.5,anchor=CENTER)
root.mainloop()