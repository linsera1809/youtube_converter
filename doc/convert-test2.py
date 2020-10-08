#importing the module 
import os
# import subprocess

from pytube import YouTube


#GLOBALS
SAVE_PATH = "C:/Users/blins/dev/projects/youtube_converter/"
link="https://www.youtube.com/watch?v=xWOoBJUqlbI" #link of the video to be downloaded 
output_name = 'test'
full_path_mp4 = '{}{}'.format(SAVE_PATH, output_name)
  
def get_mp4_file_from_link(link, output_name):
    try: 
        #object creation using YouTube which was imported in the beginning 
        yt = YouTube(link) 
    except: 
        print("Connection Error") #to handle exception 

    try: 
        yt.streams.filter(file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH, output_name)
        print('Task Completed!')   
    except: 
        print("Some Error!") 

def convert_to_mp3(filename):
    mp4_filename = '{}.mp4'.format(filename)
    mp3_filename = '{}.mp3'.format(filename)

    print(filename)
    print(mp4_filename)
    print(mp3_filename)

    try:
        # file, extension = os.path.splitext(mp4_filename)
        os.system('ffmpeg -i {file}.mp4 {file}.mp3'.format(file=filename))
        print('completed')

    except OSError as err:
        print(err.reason)
        exit(1)
    # mp4_file = r'{}'.format(mp4_filename)
    # mp3_file = r'{}'.format(mp3_filename)

    # AudioSegment.from_file(mp4_filename).export(mp3_filename, format="mp3")
    # video = VideoFileClip(mp4_filename)
    # print(video)
    # audio = video.audio
    # print(audio)
    # # video.audio.write_audiofile(os.path.join(mp3_filename))
    # video.close() 


#filters out all the files with "mp4" extension 
# mp4files = yt.streams.filter(subtype='mp4') 
# yt.set_filename('GeeksforGeeks Video') #to set the name of the file 
  
#get the video with the extension and resolution passed in the get() function 
# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 


get_mp4_file_from_link(link, output_name)
convert_to_mp3(full_path_mp4)