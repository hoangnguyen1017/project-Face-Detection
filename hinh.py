from tkinter import * 

root = Tk()
root.title("set image")
root.geometry("800x500")

bg = PhotoImage(file=r"C:\Users\nguye\Downloads\Project-FACE\pic1.png")

lb = Label(root, image=bg)
lb.place(x=100 ,y=0, relwidth=1, relheight=1)

my_text = Button(root, text="click",font="arial 10",fg= "red")
my_text.place(x=10,y=10)


root.mainloop()

