#importing tkinter module
from tkinter import *
from PIL import ImageTk,Image
#making root object of Tk class
root=Tk()
root.title("Image Viewer")
root.iconbitmap("download.png")





#calling object of class ImageTk using dot operator
my_Img1=ImageTk.PhotoImage(Image.open("images/nasa1.png"))
my_Img2=ImageTk.PhotoImage(Image.open("images/nasa2.png"))
my_Img3=ImageTk.PhotoImage(Image.open("images/nasa3.png"))
my_Img4=ImageTk.PhotoImage(Image.open("images/nasa4.png"))
my_Img5=ImageTk.PhotoImage(Image.open("images/nasa5.png"))
my_Img6=ImageTk.PhotoImage(Image.open("images/nasa6.png"))
my_Img7=ImageTk.PhotoImage(Image.open("images/nasa7.png"))
my_Img8=ImageTk.PhotoImage(Image.open("images/nasa8.png"))
my_Img9=ImageTk.PhotoImage(Image.open("images/nasa9.png"))
my_Img10=ImageTk.PhotoImage(Image.open("images/nasa10.png"))

my_list=[my_Img1,my_Img2,my_Img3,my_Img4,my_Img5,my_Img6,my_Img7,my_Img8,my_Img9,my_Img10]



#print(my_list)

#creating a label
my_label=Label(image=my_Img1)
#putting it on the screen
my_label.grid(row=0,column=0, columnspan=3)


#creating a status level to display no of images shown
status=Label(root,text="images 1 of " + str(len(my_list)),bd=1,relief="sunken",anchor=E)
# putting it on the screen
status.grid(row=2,column=0,columnspan=3,sticky=W+E)


#backward function to back the images; button_before is associated to work with this function
def backward(img_number):
	global my_label
	global button_after
	global button_before

	my_label.grid_forget()

	my_label=Label(image=my_list[img_number-1])
	button_after=Button(root,text=">>",command=lambda:foreward(img_number+1))
	button_before=Button(root,text="<<",command=lambda:backward(img_number-1))

	if img_number==1:
		button_before=Button(root,text="<<",state=DISABLED)
	
	status=Label(root,text="images"+str(img_number)+  "of " + str(len(my_list)),bd=1,relief="sunken",anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)



    


	my_label.grid(row=0,column=0, columnspan=3)
	button_after.grid(row=1,column=2)
	button_before.grid(row=1,column=0)
	return


# foreward function to foreward the images; button_after is associated to work with this function
def foreward(img_number):
	global my_label
	global button_after
	global button_before
	my_label.grid_forget()
	

	my_label=Label(image=my_list[img_number-1])
	button_after=Button(root,text=">>",command=lambda:foreward(img_number+1))
	button_before=Button(root,text="<<",command=lambda:backward(img_number-1))
	#my_label.grid_forget()
	
	if img_number == 10:
		button_after=Button(root,text=">>",state=DISABLED)
		#button_before=Button(root,text="<<",command=lambda:backward(img_number-1))

	status=Label(root,text="images"+ str(img_number)+ "of " + str(len(my_list)),bd=1,relief="sunken",anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)
	my_label.grid(row=0,column=0, columnspan=3)
	button_after.grid(row=1,column=2)
	button_before.grid(row=1,column=0)

	return

#beforebutton to back the images
button_before=Button(root,text="<<",state=DISABLED,command=backward)
#displayig before button on to the scren
button_before.grid(row=1,column=0)
#after button to foreward the images
button_after=Button(root,text=">>",command=lambda:foreward(2))
#displaying after button on to the screen
button_after.grid(row=1,column=2)
#exit button to exit the application
button_exit=Button(root,text="exit",command=root.quit)
#displaying exit button on to the screen
button_exit.grid(row=1,column=1,pady=10)
root.mainloop()
