import tkinter
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import ttk
from tkinter.ttk import *

window = tkinter.Tk()
window.geometry("600x600+350+100")
window.title("Youtube Video Downloader")
window.resizable(False,False)

window.config(bg="#28282B")

direct = ""
def open_path():
    download_out.config(text = "Wait a bit if system doesn't respond", font=("Times",25,"bold"))
    download_name.config(text="")
    download_size.config(text="")
    download_loc.config(text="")

    global direct
    direct = filedialog.askdirectory()
    path_holder.config(text = str(direct))

def Download():
    url = link_ent.get()
    Selected = types.get()

    if len(url) < 1:
        link_error.config(text="Please insert url")
    
    if len(str(direct)) < 1:
        path_error.config(text="Please insert path")

    else:
        link_error.config(text="")
        path_error.config(text="")

        try:
            Yt = YouTube(url)
            try:
                if (Selected == options[0]):
                    typ = Yt.streams.get_highest_resolution()

                elif (Selected == options[1]):
                    typ = Yt.streams.filter(progressive=True, file_extension="mp4").first()

                elif (Selected == options[2]):
                    typ = Yt.streams.filter(only_audio=True).first()

                try:
                    typ.download(str(direct))
                    link_ent.delete(0, "end")
                    path_holder.config(text="\t\t\t                      ")
                    download_out.config(text="Downloaded", font=(12))

                    name = typ.title
                    size = typ.filesize/1024000
                    size = round(size, 1)
                    download_name.config(text="Name: "+name)
                    download_size.config(text="Size: "+str(size)+"MB")
                    download_loc.config(text="Path: "+direct)

                except:
                    download_out.config(text="Download Failed", font=(15))

            except:
                download_out.config(text="Having Error", font=(15))

        except:
            path_error.config(text="Please insert Valid url")



heading = Label(window, text="Youtube Video Downloader", background="#28282B", foreground="#007CC7", font=("Times",30,"bold"))
heading.pack(anchor="center", pady=10)

link = Label(window, text="Link", background="#28282B", foreground="#007CC7", font=("Times",20))
link.pack(anchor="nw", padx=20, pady=8)

entry_url = StringVar()
link_ent = Entry(window, width=75, textvariable=entry_url)
link_ent.place(x=90, y=83)

link_error = Label(window, background="#28282B", foreground="#007CC7", font=("Times",15))
link_error.place(x=300, y=110)

path = Label(window, text="Path", background="#28282B", foreground="#007CC7", font=("Times",20))
path.pack(anchor="nw", padx=20, pady=19)

path_holder = Label(window, text="\t\t\t                      ", background="#3F3F3F", foreground="#28282B", font=("Times",15))
path_holder.place(x=90, y=140)

path_style = ttk.Style()
path_style.configure("PT.TButton", background="#007CC7", foreground="#007CC7", font=("Times",12))

path_btn = Button(window, width=10, text="Select Path", style="PT.TButton", command=open_path)
path_btn.place(x=455, y=138)

path_error = Label(window, background="#28282B", foreground="#007CC7", font=("Times",15))
path_error.place(x=300, y=180)

download_type = Label(window, text="Download Type", background="#28282B", foreground="#007CC7", font=("Times",20))
download_type.pack(anchor="w", padx=20, pady=25)

options = ["High Quality", "Low Quality", "Audio"]

types = ttk.Combobox(window, values=options, width=23)
types.current(0)
types.place(x=220, y=228)

choose_type =  Label(window, text="Choose Type", background="#28282B", foreground="#007CC7", font=("Times",20))
choose_type.place(x=400, y=220)

download_style = ttk.Style()
download_style.configure("DD.TButton", background="#007CC7", foreground="#007CC7", font=("Times",20))

download_btn = Button(window, width=10, text="Download", style="DD.TButton", command=Download)
download_btn.pack(anchor="center", pady=30)

download_out = Label(window, text="Wait if system doesn't respond", background="#28282B", foreground="#007CC7", font=("Times",20))
download_out.pack(anchor="center", padx=20, pady=25)

download_name = Label(window, background="#28282B", foreground="#007CC7", font=("Times",15))
download_name.pack(anchor="nw", padx=10, pady=5)

download_size = Label(window, background="#28282B", foreground="#007CC7", font=("Times",15))
download_size.pack(anchor="nw", padx=10, pady=5)

download_loc = Label(window, background="#28282B", foreground="#007CC7", font=("Times",15))
download_loc.pack(anchor="nw", padx=10, pady=5)

window.mainloop()