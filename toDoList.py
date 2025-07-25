from tkinter import *
from tkinter import messagebox
import webbrowser


# TK OBJECT ---->
tk = Tk()


# FRAME SIZE CONFIG ---->

tk.geometry('800x440+500+200')
tk.config(bg='#200719')
tk.resizable(width=True, height=True)


# FRAME IN THE APP ---->

frame = Frame(tk)
frame.pack(pady=14)


# TASKS LIST ---->

list_box = Listbox(
    frame, width=50, height=8, font=('Impact', 15), background='#702963',  bd=1,
    highlightthickness=6, foreground='#E20F61', selectforeground='purple',
    highlightcolor='#FAF68F', selectbackground='white', activestyle='underline'
)
list_box.pack(side=LEFT, fill=BOTH)
task_list = ['code', 'code', 'code', 'and', 'no sleep', 'repeat']


# RICK ROLL LINK COMMAND ---->


def rick_rooll():
    video_url = 'https://youtu.be/xm3YgoEiEDc?si=XcqGy5HN4u-HPDda'
    webbrowser.open(video_url)


# CREATE NEW TASK COMMAND ---->


def new_task():
    task = my_entry.get()
    if task != "":
        list_box.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('WARNING WARNING WARNING', 'You must enter something!')


# DELETE TASK COMMAND ---->


def delete_task():
    list_box.delete(ANCHOR)


# RICK ROLL BUTTON ---->

ricK_roll_btn = Button(
    text='p_i_z_z_a', font=('Impact', 13), bg='white', pady=-1, width=20, foreground='white',
    activebackground='black', activeforeground='white', command=rick_rooll
)
ricK_roll_btn.pack()


# INPUT TASK FIELD ---->

my_entry = Entry(
    tk,
    font=('Impact', 18),
    background='#FFF8DC',
    foreground='#800080'
)
my_entry.pack(pady=10)


# INSERT TASK TO THE END ---->

for item in task_list:
    list_box.insert(END, item)


# BUTTON FRAME ---->

button_frame = Frame(tk)
button_frame.pack(pady=5)


# ADD TASK BUTTON ---->

addTask_btn = Button(
    button_frame, text='add', font=('Ink free', 14), bg='#c5f776', padx=20, pady=10,
    activebackground='black', activeforeground='white', command=new_task
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


# DELETE TASK BUTTON ---->

delTask_btn = Button(
    button_frame, text='destroy task', font=('Ink free', 14), bg='#ff8b61', padx=20,  pady=10,
    activebackground='black', activeforeground='white', command=delete_task
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


# SCROLL BAR THINGY ---->

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)


# LOOPING THE APP ---->
tk.mainloop()

