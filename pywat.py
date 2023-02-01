import sys
import pywhatkit
from tkinter import *
import tkinter.messagebox
import configparser

config = configparser.ConfigParser()


config.read(r'C:\igswhatsapp_automation\config.txt')

delay_time = int(config['config']['buffer_time'])
print(delay_time)

f = open(r"C:\igswhatsapp_automation\message.txt", "r")
message = f.read()
f.close()

f = open(r"C:\igswhatsapp_automation\caption.txt", "r")
caption = f.read()
f.close()

numbers = []
f = open(r"C:\igswhatsapp_automation\numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
# total_number = len(numbers)
# fw = open(r"C:\igswhatsapp_automation\log.txt", "a")


def success():
    tkinter.messagebox.showinfo('Status', 'Process Completed Sucessfully')


def default():
    for number in numbers:
        number = number.strip()
        if number == "":
            continue
        contact = number
        pywhatkit.sendwhatmsg_instantly(contact, message, delay_time, True)
        
    success()


def s_img():
    for number in numbers:
        number = number.strip()
        if number == "":
            continue
        contact = number

        pywhatkit.sendwhats_image(
            contact, "C:\igswhatsapp_automation\IGS.jpg", caption, delay_time, True)
        
    success()


window = Tk()
window.geometry('600x500')
window.configure(bg='black')

 
window.title('IGS-WhatsApp-Automation')
Label(window, text='WHATSAPP AUTOMATION', font=80,
      bg='black', fg='white').place(x=170, y=50)
 

Button(window, text="Click here to send Text", bg='white', command=default, font=50, width=20, height=1).place(x=185, y=170)
Button(window, text="Click here to sent Image", bg='white', command=s_img, font=50, width=20, height=1).place(x=185, y=250)
Button(window, text="Exit", bg='white', command=sys.exit, font=50, width=10, height=1).place(x=240, y=330)
 
mainloop()
