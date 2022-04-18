from tkinter import *
root=Tk()
root.title("Encrypted Name")
root.geometry("400x400")
root.configure(background="magenta")
enter_name=Entry(root)
enter_name.place(relx=0.5,rely=0.5,anchor=CENTER)
label_1=Label(root,text="Name In ASCII",bg="light blue",fg="purple")
label_2=Label(root,text="Encrypted Name",bg="light blue",fg="purple")
def ShowEncryption():
    word=enter_name.get()
    for letter in word:
        label_1["text"]+=str(ord(letter))+" "
        Encrypted=int(ord(letter))
        ascii=Encrypted-1
        label_2["text"]+=str(chr(ascii))+" "
button=Button(root,text="Encrypted Name",command=ShowEncryption)
button.place(relx=0.5,rely=0.6,anchor=CENTER)
label_1.place(relx=0.5,rely=0.7,anchor=CENTER)
label_2.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()