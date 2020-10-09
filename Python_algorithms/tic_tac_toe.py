print("***WELCOME TO PLAY TIC TAC TOE***")
print("LET\'s START THE GAME")
print("Player 1[X]----Player 2[O]")
import time
from tkinter import *
from tkinter import messagebox
p1=input("Enter Player 1 Name: ")
p2=input("Enter Player 2 Name: ")
tk=Tk()
tk.title("X and O game ")
click=True
def checkwin(buttons):
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click=False
    elif buttons["text"]==" " and click==False:
        buttons["text"]="O"
        click=True
    if(b1["text"]==b2["text"]==b3["text"]=="X" or
       b4["text"]==b5["text"]==b6["text"]=="X" or
       b7["text"]==b8["text"]==b9["text"]=="X" or
       b1["text"]==b4["text"]==b7["text"]=="X" or
       b2["text"]==b5["text"]==b8["text"]=="X" or
       b3["text"]==b6["text"]==b9["text"]=="X" or
       b1["text"]==b5["text"]==b9["text"]=="X" or
       b3["text"]==b5["text"]==b7["text"]=="X"):
        messagebox.showinfo("Winner '"+p1+"'","Congrats '"+p1+" 'you won the Game")
        tk.destroy()
        print(p1+" is Winner of the Game")
    elif(b1["text"]==b2["text"]==b3["text"]=="O" or
         b4["text"]==b5["text"]==b6["text"]=="O" or
         b7["text"]==b8["text"]==b9["text"]=="O" or
         b1["text"]==b4["text"]==b7["text"]=="O" or
         b2["text"]==b5["text"]==b8["text"]=="O" or
         b3["text"]==b6["text"]==b9["text"]=="O" or
         b1["text"]==b5["text"]==b9["text"]=="O" or
         b3["text"]==b5["text"]==b7["text"]=="O"):
        messagebox.showinfo("Winner '"+p2+"'","Congrats '"+p2+" 'you won the Game")
        tk.destroy()
        print(p2+" is Winner of the Game")
    elif(b1["text"]!=" "and b2["text"]!=" " and b3["text"]!=" " and
         b4["text"]!=" "and b5["text"]!=" " and b6["text"]!=" " and
         b7["text"]!=" "and b8["text"]!=" " and b9["text"]!=" " and
         b1["text"]!=" "and b4["text"]!=" " and b7["text"]!=" " and
         b2["text"]!=" "and b5["text"]!=" " and b8["text"]!=" " and
         b3["text"]!=" "and b6["text"]!=" " and b9["text"]!=" " and
         b1["text"]!=" "and b5["text"]!=" " and b9["text"]!=" " and
         b3["text"]!=" "and b5["text"]!=" " and b7["text"]!=" "):
        messagebox.showinfo("NO WINNER ","Game Draw")
        tk.destroy()
        print("No winner,game draw")
buttons=StringVar()
print("Please Wait.....")
time.sleep(0.5)
b1=Button(tk,text=" ",font=('Times 26 bold'),bg="red",fg="white",height=4,width=8,command=lambda:checkwin(b1))
b1.grid(row=1,column=0,sticky=S+N+E+W)
b2=Button(tk,text=" ",font=("Times 26 bold"),bg="brown",fg="white",height=4,width=8,command=lambda:checkwin(b2))
b2.grid(row=1,column=1,sticky=S+N+E+W)
b3=Button(tk,text=" ",font=("Times 26 bold"),bg="violet",fg="white",height=4,width=8,command=lambda:checkwin(b3))
b3.grid(row=1,column=2,sticky=S+N+E+W)
b4=Button(tk,text=" ",font=("Times 26 bold"),bg="blue",fg="white",height=4,width=8,command=lambda:checkwin(b4))
b4.grid(row=2,column=0,sticky=S+N+E+W)
b5=Button(tk,text=" ",font=("Times 26 bold"),bg="orange",fg="white",height=4,width=8,command=lambda:checkwin(b5))
b5.grid(row=2,column=1,sticky=S+N+E+W)
b6=Button(tk,text=" ",font=("Times 26 bold"),bg="green",fg="white",height=4,width=8,command=lambda:checkwin(b6))
b6.grid(row=2,column=2,sticky=S+N+E+W)
b7=Button(tk,text=" ",font=("Times 26 bold"),bg="black",fg="white",height=4,width=8,command=lambda:checkwin(b7))
b7.grid(row=3,column=0,sticky=S+N+E+W)
b8=Button(tk,text=" ",font=("Times 26 bold"),bg="gray",fg="white",height=4,width=8,command=lambda:checkwin(b8))
b8.grid(row=3,column=1,sticky=S+N+E+W)
b9=Button(tk,text=" ",font=("Times 26 bold"),bg="pink",fg="white",height=4,width=8,command=lambda:checkwin(b9))
b9.grid(row=3,column=2,sticky=S+N+E+W)
tk.mainloop()
