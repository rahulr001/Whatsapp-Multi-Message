import sys
import pywhatkit
from tkinter import *
import tkinter.messagebox

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
total_number = len(numbers)
fw = open(r"C:\igswhatsapp_automation\log.txt", "a")


def success():
    tkinter.messagebox.showinfo('Status', 'Message sent successfully')


def default():
    delay = int(delay_time.get())
    for number in numbers:
        number = number.strip()
        if number == "":
            continue
        contact = '+91' + number
        pywhatkit.sendwhatmsg_instantly(contact, message, delay, True)
        fw.write('Sent message successfully to {}.'.format(number))
        fw.write('\n')
    success()


def s_img():
    delay = int(delay_time.get())

    for number in numbers:
        number = number.strip()
        if number == "":
            continue
        contact = '+91' + number

        pywhatkit.sendwhats_image(contact, "C:\igswhatsapp_automation\IGS.jpg", caption, delay, True)
        fw.write('Sent Image successfully to {}.'.format(number))
        fw.write('\n')
    success()


window = Tk()
window.geometry('600x500')
window.configure(bg='black')

delay = IntVar()
window.title('IGS-WhatsApp-Automation')
Label(window, text='WHATSAPP AUTOMATION', font=80,
      bg='black', fg='white').place(x=170, y=50)
Label(window, text="Time delay in seconds : ", font=5, bg='black', fg='white').place(x=20, y=110)
delay_time = Entry(window, textvariable=delay, width=15)
delay_time.place(x=240, y=110)

Button(window, text="Sent Text", bg='white', command=default, font=50, width=10, height=1).place(x=240, y=170)
Button(window, text="Sent Image", bg='white', command=s_img, font=50, width=10, height=1).place(x=240, y=250)
Button(window, text="Exit", bg='white', command=sys.exit, font=50, width=10, height=1).place(x=240, y=330)
Label(window, text="*note : Time delay should not be less than 10 seconds. ", bg='black', fg='white').place(x=20, y=460)
mainloop()
