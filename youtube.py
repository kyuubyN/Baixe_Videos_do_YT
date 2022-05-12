import pytube

youtube_url = 'https://www.youtube.com/watch?v=BiERAq5oe3c' #Coloque a URL do video

ytvid = pytube.YouTube(youtube_url)
video = ytvid.streams.get_lowest_resolution() #Resolução do video
video.download()
#Para maior facilidade utilize o pycharm
