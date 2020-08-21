from tkinter import*

# main window:
window = Tk()
window.title('tkinterTutor')
window.configure(background='#222222',borderwidth=0)


def clr():
	display.pack_forget()
def clr2():
	display2.pack_forget()
def submit(event):
	global display
	global display2
	display = Label(window,width=20, bg='#222222',fg='orange',font=('nintendo ds bios',18),text=txtentry.get())
	display.pack()
	display2 = Label(window,width=20, bg='#222222',fg='orange',font=('nintendo ds bios',18),text=txtentry2.get())
	display2.pack()

window.bind('<Return>', submit)



titler = Label(window, text='Employee Database',bg='#222222',fg='orange',font=('nintendo ds bios',24))
titler.pack()

firstname = Label(window, text='first name',bg='#222222',fg='#777777',font=('nintendo ds bios',18))
firstname.pack()
txtentry = Entry(window,width=20,font=('nintendo ds bios',18),bg='#333333',fg='white',borderwidth=0)
txtentry.pack()
correctorButt =  Button(window, text ='>>>',font=14, width=5,bg='#222222',fg='#79ADBE',borderwidth=0,command=clr)
correctorButt.pack()
firstname = Label(window, text='last name',bg='#222222',fg='#777777',font=('nintendo ds bios',18))
firstname.pack()
txtentry2 = Entry(window,width=20,font=('nintendo ds bios',18),bg='#333333',fg='white',borderwidth=0)
txtentry2.pack()
correctorButt2 =  Button(window, text ='>>>',font=14, width=5,bg='#222222',fg='#79ADBE',borderwidth=0,command=clr2)
correctorButt2.pack()








window.mainloop()