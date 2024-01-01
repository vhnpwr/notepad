from tkinter import*
from  PIL import Image,ImageTk
root=Tk()

root.title("Notepad")
root.geometry("650x650")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))

lbl_FileName=Label(root,text="File Name",font=("Arial",18,"bold"))
lbl_FileName.place(relx=0.3,rely=0.05,anchor=CENTER)

input_FileName=Entry(root,font=("Arial",18,"bold"))
input_FileName.place(relx=0.6,rely=0.05,anchor=CENTER)

my_text=Text(root,height=30,width=80)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

btn_openFile=Button(root,text="Open File",image=open_img)
btn_openFile.place(relx=0.05,rely=0.1,anchor=CENTER)

btn_saveFile=Button(root,text="Save File",image=save_img)
btn_saveFile.place(relx=0.1,rely=0.1,anchor=CENTER)

btn_exitFile=Button(root,text="Exit Button",image=exit_img)
btn_exitFile.place(relx=0.15,rely=0.1,anchor=CENTER)

root.mainloop()
