import pytube

youtube_url = 'https://www.youtube.com/watch?v=BiERAq5oe3c'

ytvid = pytube.YouTube(youtube_url)
video = ytvid.streams.get_lowest_resolution()
video.download()