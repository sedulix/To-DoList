from tkinter import *
from tkinter import messagebox
import webbrowser

tk = Tk()
tk.geometry('800x440+500+200')
tk.config(bg='#200719')
tk.resizable(width=True, height=True)
frame = Frame(tk)
frame.pack(pady=14)

list_box = Listbox(frame, width=50, height=8, font=('Impact', 15), background='#702963',  bd=1, highlightthickness=6,
                   foreground='#E20F61', selectforeground='purple', highlightcolor='#FAF68F',
                   selectbackground='white', activestyle='underline')

list_box.pack(side=LEFT, fill=BOTH)
task_list = ['code', 'code', 'code', 'and', 'no sleep', 'repeat']


def chaos():
    video_url = 'https://youtu.be/xm3YgoEiEDc?si=XcqGy5HN4u-HPDda'
    webbrowser.open(video_url)


btn = Button(
    text='p_i_z_z_a', font=('Impact', 13), bg='white', pady=-1, width=20, foreground='white',
    activebackground='black', activeforeground='white', command=chaos)
btn.pack()

my_entry = Entry(
    tk,
    font=('Impact', 18),
    background='#FFF8DC',
    foreground='#800080'
)
my_entry.pack(pady=10)

for item in task_list:
    list_box.insert(END, item)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)


def new_task():
    task = my_entry.get()
    if task != "":
        list_box.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('WARNING WARNING WARNING', 'You must enter something!')


def delete_task():
    list_box.delete(ANCHOR)


button_frame = Frame(tk)
button_frame.pack(pady=5)

addTask_btn = Button(button_frame, text='add', font=('Ink free', 14), bg='#c5f776', padx=20, pady=10,
                     activebackground='black', activeforeground='white', command=new_task)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


delTask_btn = Button(button_frame, text='destroy task', font=('Ink free', 14), bg='#ff8b61', padx=20,  pady=10,
                     activebackground='#FA8072', command=delete_task)

delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


tk.mainloop()
turtle.mainloop()
