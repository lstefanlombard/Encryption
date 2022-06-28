from tkinter import *
import pyperclip
def open_encrypt():
    def paste():
        input1.insert(0, pyperclip.paste())
        
    def copy():
         pyperclip.copy(output1.get())
        
    def clear():
        output1.delete(0, END)
        input1.delete(0, END)

    root2 =Toplevel()
    root2.title("Encrypt")
    input1 = Entry(root2, width=50)
    input1.grid(row=0,column=0)
    input1.get()
    data="hello"

    output1=Entry(root2, width=50)
    output1.grid(row=2,column=0)
    output1.get()

    def e():
        crack =["q", "m", "z", "n","r","c","v","j","i","u","s","@","$","k","d","t","x","a","g","y","e","w","o","f","l","b","h",]
        

        message = input1.get()
        encoded = ""
        for char in message:
            if char == "a" or char == "A":
                encoded += crack[0]
            elif char == "b" or char == "B":
                encoded += crack[1]
            elif char == "c" or char == "C":
                encoded += crack[2]
            elif char == "d" or char == "D":
                encoded += crack[3]
            elif char == "e" or char == "E":
                encoded += crack[4]
            elif char == "f" or char == "F":
                encoded += crack[5]
            elif char == "g" or char == "G":
                encoded += crack[6]
            elif char == "h" or char == "H":
                encoded += crack[7]
            elif char == "i" or char == "I":
                encoded += crack[8]
            elif char == "j" or char == "J":
                encoded += crack[9]
            elif char == "k" or char == "K":
                encoded += crack[10]
            elif char == "l" or char == "L":
                encoded += crack[11]
            elif char == "m" or char == "M":
                encoded += crack[12]
            elif char == "n" or char == "N":
                encoded += crack[13]
            elif char == "o" or char == "O":
                encoded += crack[14]
            elif char == "p" or char == "P":
                encoded += crack[15]
            elif char == "q" or char == "Q":
                encoded += crack[16]
            elif char == "r" or char == "R":
                encoded += crack[17]
            elif char == "s" or char == "S":
                encoded += crack[18]
            elif char == "t" or char == "T":
                encoded += crack[19]
            elif char == "u" or char == "U":
                encoded += crack[20]
            elif char == "v" or char == "V":
                encoded += crack[21]
            elif char == "w" or char == "W":
                encoded += crack[22]
            elif char == "x" or char == "X":
                encoded += crack[23]
            elif char == "y" or char == "Y":
                encoded += crack[24]
            elif char == "z" or char == "Z":
                encoded += crack[25]
            elif char == " " or char == " ":
                encoded += crack[26]
            else:
                encoded += char

        #output1=Entry(root, width=50)
        #output1.pack()
        output1.insert(0, encoded)

    button =Button(root2, text = "encript", command=e, width = 10, bg='lime')
    button.grid(row=1,column=0)

    button_paste =Button(root2, text = "Past", command=paste, width = 10, bg='aqua')
    button_paste.grid(row=0, column=1)

    button_clear =Button(root2, text = "Clear", command=clear, width = 10, bg='red')
    button_clear.grid(row=1, column=1)

    button_paste =Button(root2, text = "Copy", command=copy, width = 10, bg='aqua')
    button_paste.grid(row=2, column=1)

    root.mainloop()
def open_decrypt():
    def paste():
        input1.insert(0, pyperclip.paste())
    
    def copy():
         pyperclip.copy(output1.get())
        
    def clear():
        output1.delete(0, END)
        input1.delete(0, END)


    root1 =Toplevel(root)
    root1.title("Decrypt")
    input1 = Entry(root1, width=50)
    input1.grid(row=0,column=0)
    input1.get()
    data="hello"

    output1=Entry(root1, width=50)
    output1.grid(row=3, column=0)
    output1.get()


        
        


    def e():
        crack =["q","m","z","n","r","c","v","j","i","u","s","@","$","k","d","t","x","a","g","y","e","w","o","f","l","b","h"]
        
        message = input1.get()
        encoded = ""
        for char in message:
            if char == crack[0]:
                encoded += "a"
            elif char == crack[1]:
                encoded += "b"
            elif char == crack[2]:
                encoded += "c"
            elif char == crack[3]:
                encoded += "d"
            elif char == crack[4]:
                encoded += "e"
            elif char == crack[5]:
                encoded += "f"
            elif char == crack[6]:
                encoded += "g"
            elif char == crack[7]:
                encoded += "h"
            elif char == crack[8]:
                encoded += "i"
            elif char == crack[9]:
                encoded += "j"
            elif char == crack[10]:
                encoded += "k"
            elif char == crack[11]:
                encoded += "l"
            elif char == crack[12]:
                encoded += "m"
            elif char == crack[13]:
                encoded += "n"
            elif char == crack[14]:
                encoded += "o"
            elif char == crack[15]:
                encoded += "p"
            elif char == crack[16]:
                encoded += "q"
            elif char == crack[17]:
                encoded += "r"
            elif char == crack[18]:
                encoded += "s"
            elif char == crack[19]:
                encoded += "t"
            elif char == crack[20]:
                encoded += "u"
            elif char == crack[21]:
                encoded += "v"
            elif char == crack[22]:
                encoded += "w"
            elif char == crack[23]:
                encoded += "x"
            elif char == crack[24]:
                encoded += "y"
            elif char == crack[25]:
                encoded += "z"
            elif char == crack[26]:
                encoded += " "
            else:
                encoded += char
        #output1=Entry(root, width=50)
        #output1.pack()
        output1.insert(0, encoded)
        msg=encoded

    button =Button(root1, text = "Decript", command=e, width =10, bg='lime')
    button.grid(row=2, column=0)

    button_paste =Button(root1, text = "Past", command=paste, width = 10, bg='aqua')
    button_paste.grid(row=0, column=1)

    button_clear =Button(root1, text = "Clear", command=clear, width = 10, bg='red')
    button_clear.grid(row=2, column=1)

    button_paste =Button(root1, text = "Copy", command=copy, width = 10, bg='aqua')
    button_paste.grid(row=3, column=1)
    root1.mainloop()
root=Tk()
root.geometry("500x100")
root.title("main window")
open_decrypt_button=Button(root, text="Encrypt Message", command=open_encrypt, bg="aqua")
open_decrypt_button.pack()

open_encrypt_button=Button(root, text="Decrypt Message", command=open_decrypt, bg="seagreen1")
open_encrypt_button.pack()
root.mainloop()