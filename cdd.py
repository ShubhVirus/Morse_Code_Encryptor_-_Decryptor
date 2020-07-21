
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk, Image

top = Tk()
top.title("WELCOME")
top.iconbitmap(r'chip_y3q_icon.ico')
top.configure(background='red')



l5=Label(top, text="WELCOME TO MORSE CODE CLUB",font=("Impact",24),bg="royalblue3",fg="goldenrod2")
l5.pack()
l0=Label(top, text="With A Social Site\nThat's By Developers",font=("Impact",16),bg="red")
l0.pack()
#photo=PhotoImage(file="Morse_Code.svg.png")
#l9=Label(top,image=photo)
#l9.pack()





def login():
    top.destroy()
    root = Tk()
    root.title("MORSECODE.COM")
    root.configure(background="gray")
    root.iconbitmap(r'1698566_jC3_icon.ico')
    root.geometry("600x600")

    def shubham():
        email = E1.get()
        pas = E2.get()

        if email == "shubham9769@gmail.com" and pas == "1234":
            messagebox.showinfo('WELCOME', 'ACCESS GRANTED')
            root.destroy()
            sk=Tk()
            sk.title("PROCESS")
            sk.geometry("500x400")
            sk.configure(background="royalblue2")
            sk.iconbitmap(r'354134_Wok_icon.ico')

            bf = Label(sk, text="CONVERT INTO",bg="royalblue1",font=("serif",16), justify=LEFT,)
            bf.pack()

            def clicked1():
                sk.destroy()
                master=Tk()
                master.title("MORSE CODE ENCRYTOR")
                master.iconbitmap(r'791406_8GL_icon.ico')
                Label(master, text="Enter your mesaage:", font=("BOLD", 16)).grid(row=0)
                Label(master, text="Your encrypted mesaage:", font=("Your encrypted mesaage:", 16)).grid(row=3)
                var1 = StringVar()
                var2 = StringVar()

                e1 = Entry(master,textvariable=var1,bd=5, relief=SUNKEN, bg="dark turquoise", font=("", 16))
                e2 = Entry(master,textvariable=var2,bd=5, relief=SUNKEN, bg="dark turquoise", font=("", 16))
                e1.grid(row=0, column=1)
                e2.grid(row=3, column=1)

                morseAlphabet = {
                    "A": ".-",
                    "B": "-...",
                    "C": "-.-.",
                    "D": "-..",
                    "E": ".",
                    "F": "..-.",
                    "G": "--.",
                    "H": "....",
                    "I": "..",
                    "J": ".---",
                    "K": "-.-",
                    "L": ".-..",
                    "M": "--",
                    "N": "-.",
                    "O": "---",
                    "P": ".--.",
                    "Q": "--.-",
                    "R": ".-.",
                    "S": "...",
                    "T": "-",
                    "U": "..-",
                    "V": "...-",
                    "W": ".--",
                    "X": "-..-",
                    "Y": "-.--",
                    "Z": "--..",
                    " ": "/",
                    "1": ". _ _ _ _",
                    "2":"..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----.",
                    "0": "-----",
                    "&": ".-...",
                    "'": ".----.",
                    "@": ".--.-.",
                    ")": "-.--.-",
                    "(": "-.--.",
                    ":": "---...",
                    ",": "--..--",
                    "=": "-...-",
                    "!": "-.-.--",
                    ".": ".-.-.-",
                    "-": "-....-",
                    "+": ".-.-.",
                    #""": ".-..-.",
                    "?": "..--..",
                    "/": "-..-.",
                }

                # encode a message in morse code, spaces between words are represented by '/'
                def encodemsg():
                    encodedMessage = ""
                    mystring = var1.get()
                    for char in mystring[:]:
                        encodedMessage += morseAlphabet[char.upper()] + " "

                    return var2.set(encodedMessage)

                b6 = Button(master, text="Encrypt", command=encodemsg, bg="snow4", fg="goldenrod2",
                            font=("Times", 16)).grid(row=1, column=1)
                Button(master, text="Close", command=master.quit, bg="snow4", fg="goldenrod2", font=("Close", 16)).grid(
                    row=9, column=1)
                #Button(master, text="Back", command=login, bg="snow4", fg="goldenrod2", font=("Close", 16)).grid(
                #   row=9, column=0)

            def clicked2():
                sk.destroy()
                insect=Tk()
                insect.title("MORSE CODE DECRYTOR")
                insect.iconbitmap(r'791406_8GL_icon.ico')
                Label(insect, text="Enter your mesaage:", font=("Enter your mesaage:", 16)).grid(row=5)
                Label(insect, text="Your decrypted mesaage:", font=("Your decrypted mesaage:", 16)).grid(row=7)
                var3 = StringVar()
                var4 = StringVar()
                e3 = Entry(insect,textvariable=var3,bd=5, relief=SUNKEN, bg="dark turquoise", font=("", 16))
                e4 = Entry(insect,textvariable=var4, bd=5,relief=SUNKEN, bg="dark turquoise", font=("", 16))
                e3.grid(row=5, column=1)
                e4.grid(row=7, column=1)

                inverseMorseAlphabet = {"---": "O", "--.": "G", "-...": "B", "-..-": "X", ".-.": "R", "--.-": "Q",
                                        "--..": "Z",
                                        ".--": "W", ".-": "A", "..": "I", "-.-.": "C", "..-.": "F", "-.--": "Y",
                                        "-": "T",
                                        "/": "",
                                        ".": "E", ".-..": "L", "...": "S", "..-": "U", "-.-": "K", "-..": "D",
                                        ".---": "J",
                                        ".--.": "P",
                                        "--": "M", "-.": "N", "....": "H", "...-": "V",
                                        ".----": "1",
                                        "..---": "2",
                                        "...--": "3",
                                        "....-": "4",
                                        ".....": "5",
                                        "-....": "6",
                                        "--...": "7",
                                        "---..": "8",
                                        "----.": "9",
                                        "-----": "0",
                                        ".-...": "&",
                                        ".----.": "'",
                                        ".--.-.": "@",
                                        "-.--.-": ")",
                                        "-.--.": "(",
                                        "---...": ":",
                                        "--..--": ",",
                                        "-...-": "=",
                                        "-.-.--": "!",
                                        ".-.-.-": ".",
                                        "-....-": "-",
                                        ".-.-.": "+",
                                        # ".-..-.":""",
                                        "..--..": "?",
                                        "-..-.": "/"}

                # parse a morse code string positionInString is the starting point for decoding
                def decodeMorse():
                    decodedmsg = ""
                    mystring = var3.get()

                    for char in mystring[:]:
                        decodedmsg += inverseMorseAlphabet[char.upper()] + " "

                    return var4.set(decodedmsg)

                b8 = Button(insect, text="Decrypt", command=decodeMorse, bg="snow4", fg="goldenrod2",
                            font=("Decrypt", 16)).grid(row=6, column=1)
                Button(insect, text="Close", command=insect.quit, bg="snow4", fg="goldenrod2", font=("Close", 16)).grid(
                    row=9, column=1)

            bu21 = Radiobutton(sk, text="Morse Code",bg="royalblue1",font=("Times",16),command=clicked1,value=0,bd=4,relief=FLAT)
            bu22 = Radiobutton(sk, text="Simple English",bg="royalblue1",font=("Times",16),command=clicked2,value=1,bd=4,relief=SUNKEN)

            bu21.pack()
            bu22.pack()


        elif email == "shubham9769@gmail.com" and pas == "":
            messagebox.showwarning('USER','Enter The Password First')
        else:
            messagebox.showwarning('USER', 'You Are Not A Valid User')

    L1 = Label(root,text="Enter EMAIL",bg="GRAY",font=("Times",16))
    L1.pack()
    E1 = Entry(root,text="",bg="dark turquoise",bd=5,relief=SUNKEN,font=("",16))
    E1.pack()

    L2 = Label(root,text="PASSWORD",bg="GRAY",font=("Times",16))
    L2.pack()
    E2 = Entry(root,text="",bd=5,bg="dark turquoise",relief=SUNKEN,font=("",16),show='*')
    E2.pack()

    b = Button(root, text="LOGIN",font=("Times",16), bg="blue",bd=4,relief=RAISED, command=shubham)
    b.pack()
    B3 = Button(root,text="Forgot Password",font=("Times",16),bd=4,relief=RAISED,command=forgot)
    B3.pack()


def forgot():
    messagebox.askquestion('Ask_Question', 'Are You A Robot?')
    kt = Tk()
    kt.title("HELP PAGE")



b5=Button(top,text="GET STARTED",font=("Impact",24),bg="blue",fg="goldenrod2",command=login,bd=5,relief=GROOVE)
b5.pack()

mainloop()