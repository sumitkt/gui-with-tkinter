from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("weather info")
root.geometry("425x175")

my_label=Label(root,text="How's the temperature?",relief="sunken",fg="red")
my_label.grid(row=0,column=1)

def click():


	import requests
	import json
	global ci_field
	global temp_id
	global e3
	global e4
	global e5
	

	



	half_api="http://api.openweathermap.org/data/2.5/weather?appid=8570627d41c50d9904aea32b5403f3cd&q="
	city=ci_field.get()
	#city=input("enter city name:")
	url=half_api+city
	api_request=requests.get(url).json()
	#print(api_request)

	try:
		api_request=requests.get(url)
		#api=json.loads(api_request.content)
		x=api_request.json()
	except Exception as e:
		api="Error"


	#my_label1=Label(root,text=api)
	#my_label1.grid(row=1,column=0)

	if x['cod']!="404":

		y=x["main"]

		temp=y["temp"]
		press=y["pressure"]
		hum=y["humidity"]
		z = x["weather"] 
		weather_description = z[0]["description"]
		#insert into fields
		temp_id.insert(0, str(temp) + " Kelvin") 
		e3.insert(0, str(press) + " hPa") 
		e4.insert(0, str(hum) + " %") 
		e5.insert(0, str(weather_description) ) 

def allclear():
	ci_field.delete(0,END)
	temp_id.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e5.delete(0,END)
	ci_field.focus_set()







#creating labels
label1=Label(root,text="City name:")
label2=Label(root,text="Temperature:")
label3=Label(root,text="atmospheric pressure:")
label4=Label(root,text="humidity:")
label5=Label(root,text="Description:")
#packing labels on to the screen
label1.grid(row=1,column=0,sticky="E")
label2.grid(row=3,column=0,sticky="E")
label3.grid(row=4,column=0,sticky="E")
label4.grid(row=5,column=0,sticky="E")
label5.grid(row=6,column=0,sticky="E")

#creating entry
ci_field=Entry(root,width=40)
temp_id=Entry(root,width=40)
e3=Entry(root,width=40)
e4=Entry(root,width=40)
e5=Entry(root,width=40)
#packing on to the screen
ci_field.grid(row=1,column=1,ipadx=100,pady=10)
temp_id.grid(row=3,column=1,ipadx=100,pady=10)
e3.grid(row=4,column=1,ipadx=100,pady=10)
e4.grid(row=5,column=1,ipadx=100,pady=10)
e5.grid(row=6,column=1,ipadx=100,pady=10)
#button to submit the query
bt1=Button(root,text="submit",command=click)
bt1.grid(row=2,column=1)
#button to clear the screen
bt2=Button(root,text="clear",command=allclear)
bt2.grid(row=7,column=1)
#button to quit
bt3=Button(root,text="Exit",command=root.quit)
bt3.grid(row=8,column=1,pady=10)





root.mainloop()