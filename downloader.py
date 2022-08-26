# Download Youtube Videos with python

from pytube import YouTube

link = input("Enter Url - "'')
youtube_1 = YouTube(link)

# Get video title
print(youtube_1.title)

# Get video thumbnail
print(youtube_1.thumbnail_url)

# Get the stream 
videos = youtube_1.streams.all()
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
