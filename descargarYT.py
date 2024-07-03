import pytube

link = input("Ingresar URL del video de YouTube: ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)
