from tkinter import *
from tkinter import messagebox
import base64
import os


def encrypt():
    password = code.get()
    
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        message = text1.get("1.0", END).strip()  # Strip any trailing newline characters
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")
        
        Label(screen1, text="Encrypted Text", font="arial", bg="#ed3833", fg="white").place(x=10, y=0)
        text2 = Text(screen1, font="robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt_message)  # Insert encrypted message
        
    elif password == "":
        messagebox.showerror("Encryption", "Please Enter Password")
        
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")
        code.set("")
        text1.delete("1.0", END)


def decrypt():
    password = code.get()
    
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        message = text1.get("1.0", END).strip()  # Strip any trailing newline characters
        decode_message = message.encode("ascii")

        # Add padding if necessary
        padding_needed = len(decode_message) % 4
        if padding_needed != 0:
            decode_message += b'=' * (4 - padding_needed)

        try:
            base64_bytes = base64.b64decode(decode_message)
            decrypt_message = base64_bytes.decode("ascii")
            
            Label(screen2, text="Decrypted Text", font="arial", bg="#00bd56", fg="white").place(x=10, y=0)
            text2 = Text(screen2, font="robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypt_message)  # Insert decrypted message
            
        except Exception as e:
            messagebox.showerror("Decryption", f"An error occurred: {e}")
        
    elif password == "":
        messagebox.showerror("Decryption", "Please Enter Password")
        
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")
        code.set("")
        text1.delete("1.0", END)


def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("375x398")
    
    # Icon (replace 'logo.png' with your actual icon path if you have one)
    image_icon = PhotoImage(file="logo.png")
    screen.iconphoto(False, image_icon)
    screen.title("PCT App")
    
    def reset():
        code.set("")
        text1.delete("1.0", END)
    
    Label(text="Enter text for encryption/decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(font="robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    
    Label(text="Enter Secret key for encryption/decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)
    
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)
    
    Button(text="Encrypt", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="Decrypt", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    
    screen.mainloop()


if __name__ == "__main__":
    main_screen()
