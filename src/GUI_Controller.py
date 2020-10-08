import os
import requests

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


#Button Maybe?
def download_from_id(video_id, output_location):
    try:
        # file, extension = os.path.splitext(mp4_filename)
        os.system("youtube-dl --restrict-filenames -i -x --audio-format mp3 {video} -o {output}%(title)s.%(ext)s".format(video=video_id, output=output_location))
        print('completed')

    except OSError as err:
        print(err.reason)
        exit(1)

#-----------------------------------#
# download_from_id('dQw4w9WgXcQ', output_location)