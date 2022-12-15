from pytube import YouTube

def Downlaod(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.downlaod()
    except:
        print("There has been an error in downloading your youtube video")
    print("This download has completed!")

link = input("Put your youtube link here!! URL: ")
Downlaod(link)
