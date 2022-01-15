from tkinter import *

root =Tk()
root.title("Encrypt")
input1 = Entry(root, width=50)
input1.pack()
input1.get()
data="hello"

def e():
    crack =["q", "m", "z", "n","r","c","v","j","i","u","s","@","$","k","d","t","x","a","g","y","e","w","o","f","l","b","h",]
    output1=Entry(root, width=50)
    output1.pack()

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
    print(encoded)

button =Button(root, text = "encript", command=e)
button.pack()

root.mainloop()
