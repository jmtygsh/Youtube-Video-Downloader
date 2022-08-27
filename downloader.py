# Download Youtube Videos with python

from pytube import YouTube

link = input("Enter Url - "'')
youtube_main = YouTube(link)

# Get video title
print(youtube_main.title)

# Get video thumbnail
print(youtube_main.thumbnail_url)

# Get the stream 
videos = youtube_main.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

print()
strm = int(input("Enter : "))

# Downloading Massage ....
print("Downloading.....")
videos[strm].download()

#Download Complete Massage
print("Complete")
