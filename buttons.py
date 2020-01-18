from tkinter import *

root=Tk()
root.title("radiobuttons")

city=StringVar()
city.set("cuttack")
mylist=[("cuttack","cuttack"),('mohali','mohali'),('chandigarh','chandigarh'),('amritsar','amritsar')]

for n1,n2 in mylist:
	Radiobutton(root,text=n1,variable=city,value=n2 ).pack(anchor=W)

def click(value):
	mylabel=Label(root,text=value)
	mylabel.pack()


b=Button(root,text="click Me!",command=lambda:click(city.get()))
b.pack()
root.mainloop()