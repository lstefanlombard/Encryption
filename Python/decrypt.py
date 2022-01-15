from tkinter import *

root =Tk()
root.title("Decrypt")
input1 = Entry(root, width=50 )
input1.pack()
input1.get()
data="hello"

def e():
    crack =["q","m","z","n","r","c","v","j","i","u","s","@","$","k","d","t","x","a","g","y","e","w","o","f","l","b","h"]
    output1=Entry(root, width=50)
    output1.pack()

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

button =Button(root, text = "encript", command=e)
button.pack()

root.mainloop()
