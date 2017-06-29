import turtle
import socket
import random
import time
import sys

height = 100
width = 800

file = open('server.config')
line = file.readline().split(' ')

scrn = turtle.Screen()
flag = False

def drawbeat(x,y):
	turtle.goto(x,y)
		
def reset():
	turtle.clear()
	turtle.up()
	turtle.setx(0)
	turtle.sety(height/2)
	turtle.down()	

def stop():
	global flag
	flag = True
	
def draw():
	global flag
	flag = False
	try:
		x=0
		while not flag:
			if x==(width/8)*2:
				file = open('server.config')
				line = file.readline().split(' ')
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect((line[0], int(line[1])))	
				x = (width/8)*3
				y = int(sock.recv(2))
				drawbeat(x,y)
				x = (width/2)
				y = int(sock.recv(2))
				drawbeat(x, y)
				x = (width/8)*5
				drawbeat(x, height/2)
			elif x==width:
				x=0
				reset()
			else:					
				drawbeat(x,height/2)
				x=x+10
	except:	
		quit()			
		turtle.bye()

def init():
	turtle.setup(320,235)
	turtle.setworldcoordinates(0,0,width,height)
	turtle.onkey(draw, 'b')
	turtle.onkey(stop, 's')
	turtle.onkey(turtle.bye, 'e')
	scrn.title('Heartbeat Monitor')
	scrn.listen()
	turtle.up()
	turtle.setx(0)
	turtle.sety(height/2)
	turtle.speed(0)
	turtle.down()	
	turtle.mainloop()

def main():
	init()
	
main()
