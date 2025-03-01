from pytube import YouTube
from sys import argv
from tkinter import *


''' Ver 0.1 '''
def main():
    try:
        tipo = argv[1]
    except IndexError:
        print('python main.py "consola/ventana"')
        return 0

    if tipo == "consola":
        consola()
    elif tipo == "ventana":
        ventana()


def consola():
    # python main.py "link"
    link = input("Link: ")
    yt = YouTube(link)

    print(f"Título: {yt.title}")
    print(f"Visitas: {yt.views}")

    yd = yt.streams.get_highest_resolution()
    # yd = yt.streams.get_lowest_resolution()

    opcion = input("¿Descargar video? ")
    if opcion.upper() == "S" or opcion.upper() == "SI":
        print("Cargando...")
        yd.download("/Users/user/Documents/Descargas de videos")
        print("Descarga completada")
    else:
        print("Adios")


def ventana():
    # Create Display Window
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('500x450')
    root.configure(bg='red')
    root.title('Youtube Downloader')

    # Label which displays text on the GUI
    Label(
        root,
        text='Youtube Video Downloader\n Enter Link to download video below...',
        font='arial 15 bold',
        bg='red',
        fg='black'
    ).pack()

    # Background Image to be displayed on created GUI
    photo = PhotoImage(file="Youtube.png")
    photo = photo.subsample(2)
    photo.transparency_set(0, 0, True)

    lbl = Label(image=photo)
    lbl.pack()

    # Variable to store user entered link
    link = StringVar()

    # Create an entry field which accepts link from user
    enter_link = Entry(root, width=70, textvariable=link)
    enter_link.place(x=50, y=100)

    # Create a field to write the title and views of the video
    lbl_width = 52
    title_lbl = Label(root, width=lbl_width, text="Title info", font="arial 10 bold", bg="blue", fg="white")
    title_lbl.place(x=50, y=125)

    views_lbl = Label(root, width=lbl_width, text="Views info", font="arial 10 bold", bg="blue", fg="white")
    views_lbl.place(x=50, y=150)

    # Function to get the title and views of the video
    def get_info():
        # Getting the user entered link and assigning it to YouTube class ini pytube
        yt = YouTube(str(link.get()))
        # Getting title and views of the video
        title = yt.title
        views = yt.views
        # Changing the title and views labels
        title_lbl.config(text=f"Title: {title}", anchor='w')
        views_lbl.config(text=f"Views: {views}")

    # Function to download the user entered link
    def downloader():
        # Restart the display label
        display = Label(root, text='')
        display.place(x=215, y=390)
        # Getting the user entered link and assigning it to YouTube class ini pytube
        url = YouTube(str(link.get()))
        # Returns the highest definition element in list of video formats
        video = url.streams.get_highest_resolution()
        # This is the directory where the video will be downloaded
        directory_for_download = "/Users/user/Documents/Descargas de videos"
        # The download starts here
        video.download(directory_for_download)
        # To acknowledge user that the video has downloaded after it's completion
        display.config(text='Downloaded')

    # Button to get the info of the video
    get_info_btn = Button(root, text='Get Info', command=get_info, fg='white', bg='black')
    get_info_btn.place(x=250, y=360)

    # Button to start the downloading the video of provided url
    download_btn = Button(root, text='Download', command=downloader, fg='white', bg='black')
    download_btn.place(x=150, y=360)

    # To start the interface and display the properties in it
    mainloop()


if __name__ == "__main__":
    main()
