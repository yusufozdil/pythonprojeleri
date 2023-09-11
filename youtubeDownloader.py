from pytube import YouTube


url=input("Enter the url of the video: ")
video=YouTube(url)

path=""
YouTube(url).streams.get_highest_resolution().download(path)
print( video.title +"Downloaded successfully")
