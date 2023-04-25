import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Inaudible command')
root.geometry('600x400+50+50')

def freqUp():
    f = entry.get()
    try:
        _ = int(f)
    except:
        showinfo(
            message="not integer"
        )
        return
    f = str(_ + 1)
    entry.delete(0, tk.END)
    entry.insert(0, f)
    freq.set(f)

def freqDown():
    f = entry.get()
    try:
        _ = int(f)
    except:
        showinfo(
            message="not integer"
        )
        return
    f = str(_ - 1)
    entry.delete(0, tk.END)
    entry.insert(0, f)
    freq.set(f)


def playAudio():
    f = entry.get()
    try:
        _ = int(f)
    except:
        showinfo(
            message="not integer"
        )
        return
    freq.set(f)


label = tk.Label(text='Frequency:')
label.grid(column=0, row=0, padx=10, pady=10,  sticky='w')

freq = tk.StringVar()
freq.set("")

# entry
entry = tk.Entry()
entry.grid(column=1, row=0, padx=10, pady=10,  sticky='w')

# button

volup = tk.Button(text='+', command=freqUp)
volup.grid(column=3, row=0, padx=10, pady=10,  sticky='w')

voldown = tk.Button(text='-', command=freqDown)
voldown.grid(column=4, row=0, padx=10, pady=10,  sticky='w')

play = tk.Button(root, text='Play', command=playAudio)
play.grid(column=0, row=1, padx=10, pady=10,  sticky='w')

pause = tk.Button(text='Pause')
pause.grid(column=1, row=1, padx=10, pady=10,  sticky='w')

message = tk.Label(text='Command played in (Hz):')
message.grid(column=0, row=2, padx=10, pady=10,  sticky='w')

hertz = tk.Label(textvariable=freq)
hertz.grid(column=1, row=2, padx=10, pady=10,  sticky='w')


root.mainloop()