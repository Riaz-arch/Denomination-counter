from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

# Setting up Main Window
root = Tk()
root.title('denomination counter')
root.configure(bg='lightblue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload=Image.open("app_img.jpg")

# Resize the image using resize() method
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,bg='lightblue')
label.place(x=180,y=120)

label1=Label(root,text="Hey user welcome to the denomination counter application",bg='lightblue')
label1.place(relx=0.5,y=340,anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo("alert","Do you want co calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1=Button(root,text="lets get started",command=msg,bg='brown',fg='white')
button1.place(x=260,y=360)

# Function for opening new/top window
def topwin():
    top=Toplevel()
    top.title("Denomination calculator")
    top.configure(bg='lightgray')
    top.geometry('600x350+50+50')


    label=Label(top,text="Enter total amount",bg='lightgray')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')

    l2 = Label(top, text="500", bg='light grey')

    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)

    t2 = Entry(top)

    t3 = Entry(top)
    
    def calculator():

        try:

            global amount

            amount = int(entry.get())

            note2000 = amount // 2000

            amount %= 2000

            note500 = amount // 500

            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)

            t2.delete(0, END)

            t3.delete(0, END)

            t1.insert(END, str(note2000))

            t2.insert(END, str(note500))

            t3.insert(END, str(note100))

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

# Centering Widgets in the Top Window

    label.place(x=230, y=50 )

    entry.place(x=200, y=80 )

    btn.place(x=240, y=120 )

    lbl.place(x=140, y=170 )

    l1.place(x=180, y=200 )

    l2.place(x=180, y=230 )

    l3.place(x=180, y=260 )

    t1.place(x=270, y=200 )

    t2.place(x=270, y=230 )

    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
