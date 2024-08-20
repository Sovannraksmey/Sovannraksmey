#Create an application to generate shapes.
#First page is to log in. Log in must be correct username and password.
#Second page is to generate shape. Can generate one shape after another.


#import turtle library
import turtle
import time #to allow time to use as delay

#create a turtle object
user = turtle.Turtle()

#the correct set of username and password"
username_set = "Sovannraksmey"
password_set = "Sovannraksmey@1234"

#WHILE LOOP to make sure the username and password MUST be correct before proceeding to shape sections
while True:
	#prompt user for username and password
	username_user_input = turtle.textinput("Login", "Enter your username")
	password_user_input = turtle.textinput("Login", "Enter your password")

	#clear the screen before moving forward
	turtle.clearscreen() #clear the screen before proceeding

	#check for correct username and password
	if username_user_input == username_set and password_user_input == password_set:
	user.write(f"Welcome, {username_set}", align="center", font=("Arial",30,"bold"))
	time.sleep(2) #display the "Welcome USERNAME" for 2 seconds
	turtle.clearscreen() #clear the welcome message
	break #exit the loop and allow to proceed to shape section

	else:
	user.write("Please check username and password", Align="center", font=("Arial",30,"bold"))
	time.sleep(2) #keep the message for 2 seconds before input username and password again
	turtle.clearscreen()


#create turtle object for shape section
writer=turtle.Turtle()

#WHILE LOOP to stop the input box from closing automatically
while True:
	#set up input box
	Box = turtle.textinput("Input Shape", "Enter Shape Here or type 'Exit' to quit")
	
	#check if user wants to exit
	if Box is None or Box.lower() == "exit":
        break #exit the loop upon clicking the x button

	#set up condition to display shapes

	#condition for square
	if Box == ("Square"):
		writer.color("Green") 
		writer.begin_fill()
		#draw square
		for i in range(4):
			writer.forward(200)
			writer.left(90)
		writer.end_fill()

	#condition for rectangle
	elif Box == ("Rectangle"):
		writer.color("Yellow")
		writer.begin_fill()
		#draw rectangle
		for i in range(2):
			writer.forward(200)
			writer.left(90)
			writer.forward(100)
			writer.left(90)
		writer.end_fill()

	#condition for triangle
	elif Box == ("Triangle"):
		writer.color("Blue")
		writer.begin_fill()
		#draw triangle
		for i in range(3):
			writer.forward(200)
			writer.left(120)
		writer.end_fill()
	
	#condition for circle
	elif Box == ("Circle"):
		writer.color("Black")
		writer.begin_fill()
		#draw circle
		writer.circle(100)
		writer.end_fill()

	#handle incorrect shape input
	else:
		writer.color("Red")
		writer.write("Please choose Square, Rectangle, Triangle, or Circle", align="center",font=("Arial",30,"bold"))

#end of algorithm
turtle.done()
