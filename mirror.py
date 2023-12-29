import tkinter as tk

def getUserInput():
    num1 = int(userinput.get())
    num2 = int(userinput2.get())
    if(num1 % 10 == num2 // 10) and (num2 % 10 == num1 // 10):
        output.config(text="mirror")
    elif(num1 % 10 != num2 // 10) and (num2 % 10 != num1 // 10):
        output.config(text="not mirror")
root = tk.Tk()
message = tk.Label(root, text="Enter two numbers")
message.pack()

output = tk.Label(root, text="")
output.pack()

userinput = tk.Entry(root)
userinput.pack()

userinput2 = tk.Entry(root)
userinput2.pack()

btn = tk.Button(root, text="See if they are mirrors", command=getUserInput)
btn.pack()

root.mainloop()
