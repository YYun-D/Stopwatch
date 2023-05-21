import tkinter as tk

def startTimer():
    if (running):
        global timer
        global sec
        global minute
        global visit
        timer += 1
        timeText.configure(text= f'{minute:02d}:'f'{sec:02d}''.')
        miliTime.configure(text= f'{timer%100:02d}', font=("Helvetica", 40))
        if timer%100==0:
            sec+=1
        if sec>0 and sec%60==0 and not sec in visit:
            visit.append(sec)
            minute+=1
            sec-=60
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def initial():
    global running
    global sec
    global minute
    global timer
    running = False
    timer = 0
    sec = 0
    minute=0
    timeText.configure(text= f'{minute:02d}:'f'{sec:02d}''.')
    miliTime.configure(text= f'{timer:02d}', font=("Helvetica", 40))

def inputTime():
    global sec
    global minute
    global timer
    global running
    
    mintimenum=minutetime.get("1.0", tk.END)
    mintimenum= mintimenum.replace("\n", "")
    sectimenum=sectime.get("1.0", tk.END)
    sectimenum=sectimenum.replace("\n", "")
    
    if str.isdigit(mintimenum) and str.isdigit(sectimenum):
        minute=int(mintimenum)
        sec=int(sectimenum)
        if minute<100 and sec<60:
            timer=0
            timeText.configure(text= f'{minute:02d}:'f'{sec:02d}''.')
            miliTime.configure(text= f'{timer:02d}', font=("Helvetica", 40))
            running = False
        
    minutetime.delete("1.0", tk.END)
    sectime.delete("1.0", tk.END)

running = False
window = tk.Tk()
window.title("Stopwatch")
window.geometry('450x225')
timer = 0
sec=0
minute=0
visit=[]

FrameTime = tk.Frame(window)
FrameTime.pack(side="top")

timeText = tk.Label(FrameTime, text= f'{minute:02d}:'f'{sec:02d}''.', font=("Helvetica", 80))
miliTime = tk.Label(FrameTime, text= f'{timer:02d}', font=("Helvetica", 40))
timeText.pack(side=tk.LEFT)
miliTime.pack(side=tk.LEFT)

FrameButton = tk.Frame(window)
FrameButton.pack(side="top")

startButton = tk.Button(FrameButton, text = 'Start', command=start, width=10)
startButton.pack(side=tk.LEFT)

FrameEmpty = tk.Frame(FrameButton, width=10)
FrameEmpty.pack(side=tk.LEFT)

stopButton = tk.Button(FrameButton, text = 'Stop', command=stop, width=10)
stopButton.pack(side=tk.LEFT)

FrameEmpty = tk.Frame(FrameButton, width=10)
FrameEmpty.pack(side=tk.LEFT)

initialButton = tk.Button(FrameButton, text = 'Reset', command=initial, width=10)
initialButton.pack(side=tk.LEFT)

FrameEmpty = tk.Frame(window, height=10)
FrameEmpty.pack(side="top")

FrameSet = tk.Frame(window)
FrameSet.pack(side="top")

minutetime = tk.Text(FrameSet, width=2, height=1, font=("Helvetica", 30))
minutetime.pack(side=tk.LEFT)
minuteText = tk.Label(FrameSet, text=':')
minuteText.pack(side=tk.LEFT)

sectime = tk.Text(FrameSet, width=2, height=1, font=("Helvetica", 30))
sectime.pack(side=tk.LEFT)

FrameEmpty = tk.Frame(FrameSet, width=10)
FrameEmpty.pack(side=tk.LEFT)

inputButton = tk.Button(FrameSet, text = 'Set', command=inputTime, width=10)
inputButton.pack(side=tk.LEFT)

startTimer()

window.mainloop()