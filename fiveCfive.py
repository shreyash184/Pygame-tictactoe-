from tkinter import *
from tkinter import messagebox
test=input("Enter type of grid")

turn1 = 1;  # For first person turn1.
turn = 1;  # For first person turn1.
flag=1
def TCT():
    window=Tk()

    window.title("Welcome to The Gaming world TIC-Tac-Toe ")
    window.geometry("500x400")

    lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','25'))
    lbl.grid(row=0,column=0)
    lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
    lbl.grid(row=1,column=0)
    lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
    lbl.grid(row=2,column=0)

    turn1=1; #For first person turn1.

    def clicked1():
        global turn1
        if btn1["text"]==" ":   #For getting the text of a button
            if turn1==1:
                turn1 =2;
                btn1["text"]="X"
            elif turn1==2:
                turn1=1;
                btn1["text"]="O"
            check();
    def clicked2():
        global turn1
        if btn2["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn2["text"]="X"
            elif turn1==2:
                turn1=1;
                btn2["text"]="O"
            check();
    def clicked3():
        global turn1
        if btn3["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn3["text"]="X"
            elif turn1==2:
                turn1=1;
                btn3["text"]="O"
            check();
    def clicked4():
        global turn1
        if btn4["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn4["text"]="X"
            elif turn1==2:
                turn1=1;
                btn4["text"]="O"
            check();
    def clicked5():
        global turn1
        if btn5["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn5["text"]="X"
            elif turn1==2:
                turn1=1;
                btn5["text"]="O"
            check();
    def clicked6():
        global turn1
        if btn6["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn6["text"]="X"
            elif turn1==2:
                turn1=1;
                btn6["text"]="O"
            check();
    def clicked7():
        global turn1
        if btn7["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn7["text"]="X"
            elif turn1==2:
                turn1=1;
                btn7["text"]="O"
            check();
    def clicked8():
        global turn1
        if btn8["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn8["text"]="X"
            elif turn1==2:
                turn1=1;
                btn8["text"]="O"
            check();
    def clicked9():
        global turn1
        if btn9["text"]==" ":
            if turn1==1:
                turn1 =2;
                btn9["text"]="X"
            elif turn1==2:
                turn1=1;
                btn9["text"]="O"
            check();
    flag=1;
    def check():
        global flag;
        b1 = btn1["text"];
        b2 = btn2["text"];
        b3 = btn3["text"];
        b4 = btn4["text"];
        b5 = btn5["text"];
        b6 = btn6["text"];
        b7 = btn7["text"];
        b8 = btn8["text"];
        b9 = btn9["text"];
        flag=flag+1;
        if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
            win(btn1["text"])
        if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
            win(btn4["text"]);
        if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
            win(btn7["text"]);
        if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
            win(btn1["text"]);
        if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
            win(btn2["text"]);
        if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
            win(btn3["text"]);
        if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
            win(btn1["text"]);
        if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
            win(btn7["text"]);
        if flag ==10:
            messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
            window.destroy()

    def win(player):
        ans = "Game complete " +player + " wins ";
        messagebox.showinfo("Congratulations", ans)
        window.destroy()  # is used to close the program


    btn1 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
    btn2.grid(column=2, row=1)
    btn3 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
    btn3.grid(column=3, row=1)
    btn4 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
    btn4.grid(column=1, row=2)
    btn5 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
    btn5.grid(column=2, row=2)
    btn6 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
    btn6.grid(column=3, row=2)
    btn7 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
    btn7.grid(column=1, row=3)
    btn8 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
    btn8.grid(column=2, row=3)
    btn9 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
    btn9.grid(column=3, row=3)

    window.mainloop()

def FCF():
    window=Tk()

    window.title("Welcome to The Gaming world TIC-Tac-Toe ")
    window.geometry("1000x600")

    lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','25'))
    lbl.grid(row=0,column=0)
    lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
    lbl.grid(row=1,column=0)
    lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
    lbl.grid(row=2,column=0)

    turn=1; #For first person turn.

    def clicked1():
        global turn
        if btn1["text"]==" ":   #For getting the text of a button
            if turn==1:
                turn =2;
                btn1["text"]="X"
            elif turn==2:
                turn=1;
                btn1["text"]="O"
            check();
    def clicked2():
        global turn
        if btn2["text"]==" ":
            if turn==1:
                turn =2;
                btn2["text"]="X"
            elif turn==2:
                turn=1;
                btn2["text"]="O"
            check();
    def clicked3():
        global turn
        if btn3["text"]==" ":
            if turn==1:
                turn =2;
                btn3["text"]="X"
            elif turn==2:
                turn=1;
                btn3["text"]="O"
            check();
    def clicked4():
        global turn
        if btn4["text"]==" ":
            if turn==1:
                turn =2;
                btn4["text"]="X"
            elif turn==2:
                turn=1;
                btn4["text"]="O"
            check();
    def clicked5():
        global turn
        if btn5["text"]==" ":
            if turn==1:
                turn =2;
                btn5["text"]="X"
            elif turn==2:
                turn=1;
                btn5["text"]="O"
            check();
    def clicked6():
        global turn
        if btn6["text"]==" ":
            if turn==1:
                turn =2;
                btn6["text"]="X"
            elif turn==2:
                turn=1;
                btn6["text"]="O"
            check();
    def clicked7():
        global turn
        if btn7["text"]==" ":
            if turn==1:
                turn =2;
                btn7["text"]="X"
            elif turn==2:
                turn=1;
                btn7["text"]="O"
            check();
    def clicked8():
        global turn
        if btn8["text"]==" ":
            if turn==1:
                turn =2;
                btn8["text"]="X"
            elif turn==2:
                turn=1;
                btn8["text"]="O"
            check();
    def clicked9():
        global turn
        if btn9["text"]==" ":
            if turn==1:
                turn =2;
                btn9["text"]="X"
            elif turn==2:
                turn=1;
                btn9["text"]="O"
            check();
    def clicked10():
        global turn
        if btn10["text"]==" ":
            if turn==1:
                turn =2;
                btn10["text"]="X"
            elif turn==2:
                turn=1;
                btn10["text"]="O"
            check();
    def clicked11():
        global turn
        if btn11["text"]==" ":
            if turn==1:
                turn =2;
                btn11["text"]="X"
            elif turn==2:
                turn=1;
                btn11["text"]="O"
            check();
    def clicked12():
        global turn
        if btn12["text"]==" ":
            if turn==1:
                turn =2;
                btn12["text"]="X"
            elif turn==2:
                turn=1;
                btn12["text"]="O"
            check();
    def clicked13():
        global turn
        if btn13["text"]==" ":
            if turn==1:
                turn =2;
                btn13["text"]="X"
            elif turn==2:
                turn=1;
                btn13["text"]="O"
            check();
    def clicked14():
        global turn
        if btn14["text"]==" ":
            if turn==1:
                turn =2;
                btn14["text"]="X"
            elif turn==2:
                turn=1;
                btn14["text"]="O"
            check();
    def clicked15():
        global turn
        if btn15["text"]==" ":
            if turn==1:
                turn =2;
                btn15["text"]="X"
            elif turn==2:
                turn=1;
                btn15["text"]="O"
            check();
    def clicked16():
        global turn
        if btn16["text"]==" ":
            if turn==1:
                turn =2;
                btn16["text"]="X"
            elif turn==2:
                turn=1;
                btn16["text"]="O"
            check();
    def clicked17():
        global turn
        if btn17["text"]==" ":
            if turn==1:
                turn =2;
                btn17["text"]="X"
            elif turn==2:
                turn=1;
                btn17["text"]="O"
            check();
    def clicked18():
        global turn
        if btn18["text"]==" ":
            if turn==1:
                turn =2;
                btn18["text"]="X"
            elif turn==2:
                turn=1;
                btn18["text"]="O"
            check();
    def clicked19():
        global turn
        if btn19["text"]==" ":
            if turn==1:
                turn =2;
                btn19["text"]="X"
            elif turn==2:
                turn=1;
                btn19["text"]="O"
            check();
    def clicked20():
        global turn
        if btn20["text"]==" ":
            if turn==1:
                turn =2;
                btn20["text"]="X"
            elif turn==2:
                turn=1;
                btn20["text"]="O"
            check();
    def clicked21():
        global turn
        if btn21["text"]==" ":
            if turn==1:
                turn =2;
                btn21["text"]="X"
            elif turn==2:
                turn=1;
                btn21["text"]="O"
            check();
    def clicked22():
        global turn
        if btn22["text"]==" ":
            if turn==1:
                turn =2;
                btn22["text"]="X"
            elif turn==2:
                turn=1;
                btn22["text"]="O"
            check();
    def clicked23():
        global turn
        if btn23["text"]==" ":
            if turn==1:
                turn =2;
                btn23["text"]="X"
            elif turn==2:
                turn=1;
                btn23["text"]="O"
            check();
    def clicked24():
        global turn
        if btn24["text"]==" ":
            if turn==1:
                turn =2;
                btn24["text"]="X"
            elif turn==2:
                turn=1;
                btn24["text"]="O"
            check();
    def clicked25():
        global turn
        if btn25["text"]==" ":
            if turn==1:
                turn =2;
                btn25["text"]="X"
            elif turn==2:
                turn=1;
                btn25["text"]="O"
            check();

    flag=1;
    def check():
        global flag;
        b1 = btn1["text"];
        b2 = btn2["text"];
        b3 = btn3["text"];
        b4 = btn4["text"];
        b5 = btn5["text"];
        b6 = btn6["text"];
        b7 = btn7["text"];
        b8 = btn8["text"];
        b9 = btn9["text"];
        b10 = btn10["text"];
        b11 = btn11["text"];
        b12 = btn12["text"];
        b13 = btn13["text"];
        b14 = btn14["text"];
        b15 = btn15["text"];
        b16 = btn16["text"];
        b17 = btn17["text"];
        b18 = btn18["text"];
        b19 = btn19["text"];
        b20 = btn20["text"];
        b21 = btn21["text"];
        b22 = btn22["text"];
        b23 = btn23["text"];
        b24 = btn24["text"];
        b25 = btn25["text"];
        flag=flag+1;
        if b1==b2 and b2==b3 and b3==b4 and b4==b5 and b5==b1 and b1=="O" or b1==b2 and b2==b3 and b3==b4 and b4==b5 and b5==b1 and b1=="X":
            win(btn1["text"])
        if b6==b7 and b7==b8 and b8==b9 and b9==b10 and b10==b6 and b6=="O" or b6==b7 and b7==b8 and b8==b9 and b9==b10 and b10==b6 and b6=="X":
            win(btn6["text"])
        if b11==b12 and b12==b13 and b13==b14 and b14==b15 and b15==b11 and b11=="O" or b11==b12 and b12==b13 and b13==b14 and b14==b15 and b15==b11 and b11=="X":
            win(btn11["text"])
        if b16==b17 and b17==b18 and b18==b19 and b19==b20 and b20==b16 and b16=="O" or b16==b17 and b17==b18 and b18==b19 and b19==b20 and b20==b16 and b16=="X":
            win(btn16["text"])
        if b21==b22 and b22==b23 and b23==b24 and b24==b25 and b25==b21 and b21=="O" or b21==b22 and b22==b23 and b23==b24 and b24==b25 and b25==b21 and b21=="X":
            win(btn21["text"])
        if b1==b7 and b7==b13 and b13==b19 and b19==b25 and b25==b1 and b1=="O" or b1==b7 and b7==b13 and b13==b19 and b19==b25 and b25==b1 and b1=="X":
            win(btn1["text"])
        if b5==b9 and b9==b13 and b13==b17  and b17==b21 and b21==b5 and b5=="O" or b5==b9 and b9==b13 and b13==b17  and b17==b21 and b21==b5 and b5=="X":
            win(btn5["text"])
        if b1==b6 and b6==b11 and b11==b16 and b16==b21 and b21==b1 and b1=="O" or b1==b6 and b6==b11 and b11==b16 and b16==b21 and b21==b1 and b1=="X":
            win(btn1["text"])
        if b2==b7 and b7==b12 and b12==b17 and b17==b22 and b22==b2 and b2=="O" or b2==b7 and b7==b12 and b12==b17 and b17==b22 and b22==b2 and b2=="X":
            win(btn2["text"])
        if b3==b8 and b8==b13 and b13==b18 and b18==b23 and b23==b3 and b3=="O" or b3==b8 and b8==b13 and b13==b18 and b18==b23 and b23==b3 and b3=="X":
            win(btn3["text"])
        if b4==b9 and b9==b14 and b14==b19 and b19==b24 and b24==b4 and b4=="O" or b4==b9 and b9==b14 and b14==b19 and b19==b24 and b24==b4 and b4=="X":
            win(btn4["text"])
        if b5==b10 and b10==b15 and b15==b20 and b20==b25 and b25==b5 and b5=="O" or b5==b10 and b10==b15 and b15==b20 and b20==b25 and b25==b5 and b5=="X":
            win(btn5["text"])
        if flag ==26:
            messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
            window.destroy()

    def win(player):
        ans = "Game complete " +player + " wins ";
        messagebox.showinfo("Congratulations", ans)
        window.destroy()  # is used to close the program


    btn1 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
    btn2.grid(column=2, row=1)
    btn3 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
    btn3.grid(column=3, row=1)
    btn4 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
    btn4.grid(column=4, row=1)
    btn5 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
    btn5.grid(column=5, row=1)
    btn6 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
    btn6.grid(column=1, row=2)
    btn7 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
    btn7.grid(column=2, row=2)
    btn8 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
    btn8.grid(column=3, row=2)
    btn9 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
    btn9.grid(column=4, row=2)
    btn10 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked10)
    btn10.grid(column=5, row=2)
    btn11 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked11)
    btn11.grid(column=1, row=3)
    btn12 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked12)
    btn12.grid(column=2, row=3)
    btn13 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked13)
    btn13.grid(column=3, row=3)
    btn14 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked14)
    btn14.grid(column=4, row=3)
    btn15 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked15)
    btn15.grid(column=5, row=3)
    btn16 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked16)
    btn16.grid(column=1, row=4)
    btn17 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked17)
    btn17.grid(column=2, row=4)
    btn18 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked18)
    btn18.grid(column=3, row=4)
    btn19 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked19)
    btn19.grid(column=4, row=4)
    btn20 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked20)
    btn20.grid(column=5, row=4)
    btn21 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked21)
    btn21.grid(column=1, row=5)
    btn22 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked22)
    btn22.grid(column=2, row=5)
    btn23 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked23)
    btn23.grid(column=3, row=5)
    btn24 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked24)
    btn24.grid(column=4, row=5)
    btn25 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked25)
    btn25.grid(column=5, row=5)


    window.mainloop()

if test=='3':
    TCT()
else:
    FCF()