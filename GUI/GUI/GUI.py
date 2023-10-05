import tkinter
from asyncio import windows_events
from tkinter import *
from time import *


window = Tk()

#mga image converter
#onbutton = PhotoImage(file='on64p.png')
exitbutton = PhotoImage(file='logout.png')


window.title("Computerized Production Process of Arabica Coffee Bean")
window.geometry("800x480") #size of the screen
window.resizable(False,False) #para di sya resizable
window.config(bg="#371B14")
main_frame = Frame(window, bg="#371B14")
main_frame.pack(expand=TRUE, fill=BOTH)


#About the time section
def updatetime():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text = time_string)

    date_string = strftime("%m/%d/%Y")
    date_label.config(text =  date_string)

    window.after(1000, updatetime)


timeframe = Frame(main_frame, width=200, height=50,  highlightthickness='10', bg="#653125")
timeframe.pack(pady=10, padx=10)
time_label = Label(timeframe, font=("Arial", 20), fg="white", bg="#653125")
time_label.pack(side="left")

date_label = Label(timeframe, font=("Arial", 10), fg="white", bg="#653125")
date_label.pack(side="left")

updatetime()

############################################################################################

#frame2

def turn_on():
    hours = int(hour_spinbox.get())
    minutes = int(minutes_spinbox.get())
    seconds = int(seconds_spinbox.get())

    total_time = hours * 3600 + minutes * 60 + seconds

    drying_time(total_time)
    drying_on.config(state="disabled")


def drying_time(time):

    if time >= 0:

        hours, remainder = divmod(time, 3600)
        minutes, seconds = divmod(remainder, 60)

        dryer_time.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        time -= 1
        window.after(1000, drying_time, time)


def reset_time(): #this is where the reset happens
    hour_var = IntVar(window)
    hour_var.set(0)
    minutes_var = IntVar(window)
    minutes_var.set(0)
    seconds_var = IntVar(window)
    seconds_var.set(0)
    hour_spinbox.config(textvariable=hour_var)
    minutes_spinbox.config(textvariable=minutes_var)
    seconds_spinbox.config(textvariable=seconds_var)
    #dryer_time.config(text="00:00:00")
    drying_on.config(state="normal")


""""#para sa reset ni sa spinbox
hour_var = IntVar(window)
hour_var.set(0)

minutes_var = IntVar(window)
minutes_var.set(0)

seconds_var = IntVar(window)
seconds_var.set(0)
#reset in the spinbox """


drying_frame = Frame(main_frame, width=250, height=100,  highlightthickness='10', bg="#653125")
drying_frame.pack(pady=10, padx=10)
#drying_frame.grid(row=10, column=0, ipadx = 10, ipady = 20)

drying_text = (Label(drying_frame, font=("Arial", 30), fg="white", bg="#653125", text="Drying Time"))
drying_text.pack()


dryer_time = Label(drying_frame, text="00:00:00", font=('Arial', 30))
dryer_time.pack(pady=20, side="bottom")


tkinter.Label(drying_frame, text="Hours").pack(side="left", padx=5)
hour_spinbox = Spinbox(drying_frame, from_= 0, to=6, width=2, font=("calibri", 25),state="readonly")
hour_spinbox.pack(side="left", padx=10)

tkinter.Label(drying_frame, text="Minutes").pack(side="left", padx=5)
minutes_spinbox = Spinbox(drying_frame, from_= 0, to=59, width=2, font=("calibri", 25), state="readonly")
minutes_spinbox.pack(side="left", padx=10)

tkinter.Label(drying_frame, text="seconds").pack(side="left", padx=5)
seconds_spinbox = Spinbox(drying_frame, from_= 0, to=59, width=2, font=("calibri", 25), state="readonly")
seconds_spinbox.pack(side="left", padx=10)

drying_on = (Button(drying_frame, width=10, pady=10 ,text="On", command=turn_on))
drying_on.pack()

drying_reset = Button(drying_frame, width=10,  pady=10, text="Reset", command=reset_time)
drying_reset.pack(pady=10)


on_button_frame = Frame(main_frame, width=250, highlightthickness='3', bg="#653125")
on_button_frame.pack(pady=10, padx=10)
#on_button_frame.grid(row=30,pady = 30)


exit_button = Button(on_button_frame, image= exitbutton, command= window.destroy)
exit_button.pack(side="right", padx=10)


#window2
def Open():
    window2 = Toplevel()
    window2.geometry("800x480")
    second_frame = Frame(window2, bg="#371B14")
    second_frame.pack(expand=TRUE, fill=BOTH)
    #label = Label(second_frame, text="Insert the Camera").pack(pady=10)
    close = Button(second_frame, text="Go back",command=window2.destroy).pack(side="bottom",pady=10)
    temp_frame = Frame(second_frame, width=500, height=150,  highlightthickness='10', bg="#653125")
    temp_frame.pack(pady=20)
    camera_frame = Frame(second_frame, width=500, height=150, highlightthickness='10', bg="#653125")
    camera_frame.pack(pady=10, padx=10)



second_window = Button(on_button_frame, text="Go to 2nd Window", command=Open)
second_window.pack(side="left", padx=10)









window = mainloop()
