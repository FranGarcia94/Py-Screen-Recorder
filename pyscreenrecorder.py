#============================= PyScreenRecorder =============================#
#                                                                            #
#                              Screen Recorder                               #
#                                                                            #
#                                                     @FranGarcia94          #
#============================================================================#


import pyscreenrec
from tkinter import *


# Rec, Pause and Play Function

def start_func():

    global aux

    if aux == 0:

        root.wm_state('iconic')
        root.attributes('-alpha',0.3)
        recorder.start_recording("recording.mp4", 30)
        stop_button['state'] = 'normal'
        start_button['text'] = 'Pause'
        start_button['image'] = pause
        aux = 1
    elif aux == 1:

        recorder.pause_recording()
        root.attributes('-alpha',1)
        start_button['text'] = 'Play'
        start_button['image'] = play
        stop_button['state'] = 'disabled'
        aux = 2
    elif aux == 2:

        root.wm_state('iconic')
        root.attributes('-alpha',0.3)
        recorder.resume_recording()
        start_button['text'] = 'Pause'
        start_button['image'] = pause
        stop_button['state'] = 'normal'
        aux = 1        


# Stop Function

def stop_func():

    global aux

    recorder.stop_recording()
    root.attributes('-alpha',1)
    stop_button['state'] = 'disabled'
    start_button['image'] = rec
    start_button['text'] = 'Start'
    aux = 0


# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #

if __name__ == '__main__':

    recorder = pyscreenrec.ScreenRecorder()


    aux = 0 # Variable to know the state of start_func
    title_bg = '#dbfb9c'


    root = Tk()

    # To know the size of the screen
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    root.title('Py Screen Recorder')
    root.geometry(f'420x150+{ws - 420}+{hs - 200}') # The interface will appear on the bottom right
    root.resizable(False, False)
    root.config(background=title_bg)


    # Insert the icons. If there is any problem, check the names, insert the full path or insert the full path with double backslash.
    # Either way the program will work, with or without icons.
    try:

        root.iconbitmap('video-player.ico')
        rec = PhotoImage(file = "rec.png")
        stop = PhotoImage(file = "stop2.png") 
        pause = PhotoImage(file = "pause2.png") 
        play = PhotoImage(file = "play2.png") 
    except:

        root.iconbitmap(None)
        rec = None
        stop = None
        pause = None
        play = None


    title_lb = Label(root, text='Screen Recorder', font= ('Pristina 19 bold'), background=title_bg)
    title_lb.pack()

    mf1 = Frame(root)
    mf1.pack(fill = 'both', expand = 1)


    start_button = Button(mf1, text= 'Start', cursor='hand2', image=rec, relief='flat', command= start_func)
    start_button.place(relx=0.35, rely=0.5, anchor=CENTER)

    stop_button = Button(mf1, text='Stop', cursor='hand2',state='disabled', image=stop, relief='flat',command=stop_func)
    stop_button.place(relx=0.65, rely=0.5, anchor=CENTER)


    root.mainloop()

