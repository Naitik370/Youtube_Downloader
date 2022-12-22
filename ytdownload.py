import pytube as Youtube

def vidDownload(link):
    Video = Youtube.YouTube(link)
    Resolution = input("resolution:")
    Video = Video.streams.get_by_resolution(Resolution)
    try:
        Video.download()
        print("This download has completed! Yahooooo!")
    except:
        print("There has been an error in downloading your youtube video")
def audDownload(link):
    Audio = Youtube.YouTube(link)
    Audio = Audio.streams.get_audio_only()
    try:
        Audio.download()
        print("This download has completed! Yahooooo!")
    except:
        print("There has been an error in downloading your youtube audio")
def main():
    link = input("Put your youtube link here!! URL: ")
    case = int(input("What Do You Want to Do\n(1)Download a Video-\n(2)Download a Video as audio: "))
    if(case == 2):
        audDownload(link)
    else:
        vidDownload(link)
main()