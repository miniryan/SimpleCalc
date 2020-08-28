import tkinter as tk

enterednum = ""
operator = None
firstnum = None
secondnum = None
result = None

window = tk.Tk()
window.resizable(False, False)
window.title("Calculator")

rightframe = tk.Frame(window)
rightframe.grid(row=1, column=0)
leftframe = tk.Frame(window)
leftframe.grid(row=1, column=1)

buttons = tk.Frame(rightframe, bg="red")
buttons.config()
buttons.grid(row=1, column=0)

text = tk.Frame(rightframe, bg="black")
text.config(height=50, width=150)
text.grid(row=0, column=0)


operators = tk.Frame(leftframe, bg="orange")
operators.config(height=50, width=150)
operators.grid(row=1, column=1)

field = tk.Label(text, height=2, width=15, borderwidth=4, relief="groove")
field.grid(row=0, column=0)

def numadd(num):
    global result
    if result == None:
        global enterednum
        enterednum = enterednum + num
        field['text'] = enterednum
    else:
        result = None
        enterednum = enterednum + num
        field['text'] = enterednum
def opadd(op) :
    global result
    if result == None:
        global enterednum
        global firstnum
        firstnum = enterednum
        enterednum = ""
        global operator
        operator = op
        field['text'] = op
    else:
        firstnum = result
        enterednum = ""   
        operator = op
        field['text'] = op
def equals():
    global result
    if result == None:
        global enterednum
        global secondnum
        secondnum = enterednum
        enterednum = ""
        if operator == "x":
            result = float(firstnum) * float(secondnum)
        elif operator == "-":
            result = float(firstnum) - float(secondnum)
        elif operator == "+":
            result = float(firstnum) + float(secondnum)
        elif operator == "/":
            result = float(firstnum) / float(secondnum)
        field['text'] = result
    else:
        secondnum = enterednum
        enterednum = ""
        if operator == "x":
            result = firstnum * float(secondnum)
        elif operator == "-":
            result = firstnum - float(secondnum)
        elif operator == "+":
            result = firstnum + float(secondnum)
        elif operator == "/":
            result = firstnum / float(secondnum)
        field['text'] = result

def clear():
    global enterednum
    global secondnum
    global firstnum
    global operator
    enterednum = ""
    operator = None
    firstnum = None
    secondnum = None    
    global result
    result = None
    field['text'] = ""



o1 = tk.Button(operators, text="+", height=2, width=4, command=lambda : opadd("+"))
o2 = tk.Button(operators, text="-", height=2, width=4, command=lambda : opadd("-"))
o3 = tk.Button(operators, text="x", height=2, width=4, command=lambda : opadd("x"))
o4 = tk.Button(operators, text="/", height=2, width=4, command=lambda : opadd("/"))
c = tk.Button(operators, text="C", height=2, width=4, command=clear)

o1.grid(row=1, column=0)
o2.grid(row=2, column=0)
o3.grid(row=3, column=0)
o4.grid(row=4, column=0)
c.grid(row=0, column=0)




b1 = tk.Button(buttons, text="1", height=2, width=4, command=lambda : numadd("1"))
b2 = tk.Button(buttons, text="2", height=2, width=4, command=lambda : numadd("2"))
b3 = tk.Button(buttons, text="3", height=2, width=4, command=lambda : numadd("3"))
b4 = tk.Button(buttons, text="4", height=2, width=4, command=lambda : numadd("4"))
b5 = tk.Button(buttons, text="5", height=2, width=4, command=lambda : numadd("5"))
b6 = tk.Button(buttons, text="6", height=2, width=4, command=lambda : numadd("6"))
b7 = tk.Button(buttons, text="7", height=2, width=4, command=lambda : numadd("7"))
b8 = tk.Button(buttons, text="8", height=2, width=4, command=lambda : numadd("8"))
b9 = tk.Button(buttons, text="9", height=2, width=4, command=lambda : numadd("9"))
b0 = tk.Button(buttons, text="0", height=2, width=4, command=lambda : numadd("0"))
eq = tk.Button(buttons, text="=", height=2, width=4, command=lambda : equals())
pd = tk.Button(buttons, text=".", height=2, width=4, command=lambda : numadd("."))


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=3, column=0)
eq.grid(row=3, column=2)
pd.grid(row=3, column=1)
window.mainloop()
