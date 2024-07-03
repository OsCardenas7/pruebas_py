import moviepy.editor

video = moviepy.editor.VideoFileClip('teamradio.mp4')

audio = video.audio

audio.write_audiofile('Team_Radio.wav')