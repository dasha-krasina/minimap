from tkinter import *

root = Tk()

canvas = Canvas(width = 3000, height = 3000, bg = "white")

canvas.pack()

poly1 = [50,50,200,50,200,150,50,150]#beatsaber room
poly2 = [200,50,300,50,300,100,200,100]#blanket space
poly3 = [300,50,450,50,450,150,300,150]#mom and dad sleep room
poly4 = [450,50,500,50,500,150,450,150]#small electric room
poly5 = [300,150,500,150,500,400,300,400]#the big room
poly6 = [300,400,400,400,400,600,300,600]#chulan(russian)
poly7 = [400,400,500,400,500,600,400,600]#Alena's room
poly8 = [50,350,200,350,200,500,50,500]#my room
poly9 = [50,500,50,600,300,600,300,450,200,450,200,500]#entry room
poly10 = [50,250,150,250,150,350,50,350]#left br
poly11 = [150,200,200,200,200,350,150,350]#heater space
poly12 = [50,150,200,150,200,200,150,200,150,250,50,250]#right br


canvas.create_polygon(poly1, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly2, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly3, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly4, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly5, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly6, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly7, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly8, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly9, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly10, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly11, fill = "white", outline = "black", width = 3)
canvas.create_polygon(poly12, fill = "white", outline = "black", width = 3)
