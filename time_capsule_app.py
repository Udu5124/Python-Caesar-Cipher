import tkinter as tk

# Function for encryption
def encrypt():

    text = txt.get()
    s = shift_value.get()
    result = ""

    # Iterate through plain text
    for char in text:
        # char = Character in the string

        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Skip mostly used characters
        elif (char in [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '.', '!', '#', '@', '&', '?', '$', '(', ')']):
            result += char

        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.insert(tk.END, result)


# Function for decryption
def decrypt():

    text = txt.get()
    s = shift_value.get()
    result = ""

    # Iterate through Cipher text
    for char in text:
        # char = Character in the string

        # Decrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Skip mostly used characters
        elif (char in [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '.', '!', '#', '@', '&', '?', '$', '(', ')']):
            result += char
        # Decrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.insert(tk.END, result)


# Function to clear text box that displays output
def clear_text():
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('0.0', tk.END)
    tkDisplay.config(state=tk.DISABLED)


# Set Window for application
window = tk.Tk()
window.title("Caesar Cipher Converter")
window.geometry("1000x600")
window.config(background="#454545")

# Top frame consists of Label and Entry to take imput
topFrame = tk.Frame(window)
topFrame.config(background="#454545")
lbl1 = tk.Label(topFrame, text="Enter the data to be Encrypted or Decrypted :", font=("Courier New", 15), bg='#EC5578').place(relx=0, rely=0)
txt = tk.Entry(topFrame, justify='center')
txt.place(relx=0, rely=0.125, relwidth=1, relheight=1)
topFrame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.35)

# Middle frame consists of slider for input for shifting pattern
# Encrypt Button for Encryption , Decrypt Button for Decryption
# Clear Button for clearing output
middleFrame = tk.Frame(window)
middleFrame.config(background="#454545")
shift_value = tk.Scale(middleFrame, from_=2, to=13, orient=tk.HORIZONTAL, font=("Courier New", 15))
shift_value.set(3)
shift_value.place(relx=0.05, rely=0.125, relwidth=0.15, relheight=0.4)
shift_value.config(background='#EC5578')
encrypt_button = tk.Button(middleFrame, text='Encrypt', bd='3', width=25, command=lambda: encrypt())
encrypt_button.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=0.4)
encrypt_button.config(background='#EC5578')
decrypt_button = tk.Button(middleFrame, text='Decrypt', bd='3', width=25, command=lambda: decrypt())
decrypt_button.place(relx=0.575, rely=0.1, relwidth=0.2, relheight=0.4)
decrypt_button.config(background='#EC5578')
clear_button = tk.Button(middleFrame, text='Clear', bd='3', width=10, command=lambda: clear_text())
clear_button.place(relx=0.8, rely=0.1, relwidth=0.15, relheight=0.4)
clear_button.config(background='#EC5578')
middleFrame.place(relx=0, rely=0.425, relwidth=1, relheight=0.3)

# Bottom frame displays the output to the user
bottomFrame = tk.Frame(window)
bottomFrame.config(background="#454545")
lbl2 = tk.Label(bottomFrame, text="Resultant Encrypted or Decrypted text :", font=("Courier New", 15), bg='#EC5578').place(relx=0, rely=0)
scrollBar = tk.Scrollbar(bottomFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(bottomFrame)
tkDisplay.place(relx=0, rely=0.15, relwidth=0.975, relheight=1)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
scrollBar.config(command=tkDisplay.yview)
bottomFrame.place(relwidth=0.9, relheight=0.3, rely=0.6, relx=0.05)

window.mainloop()

# pyinstaller.exe --onefile --noconsole time_capsule_app.py
