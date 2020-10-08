# youtube_converter
_Status: WIP - Building APIs_
_Last Updated: 10/08/20_  
_Date Created: 10/07/20_  
_Author: Bobby Linse_
______________________________________________
## General Notes

### Description
* This application will build an executable that will allow the user to add multiple songs/artists into a GUI,
where the application will then query YouTube, download all of the .mp4s into .mp3s at a destination requested by the user


### Requirements
* **Input**: a list of artists/songs/titles to search Youtube
* **Output**: an .mp3 file converted from a Youtube link
* **Additional Requirements**:
    * Must be easy to use; potentially an .exe file run from a desktop
    * No command line calls should be run
    * The user should be able to quickly verify that the song is the correct choice
    * The user is able to use multiple inputs
* **User Story**: Steven should be able to open up a shortcut from his desktop, and add in artists and songs, verify that they
are the correct videos that he wanted, and download them into his external hard-drive.

______________________________________________
## Dev Notes

### Restrictions:
* API Restrictions per Quota Limits
    * 10,000 queries per day
    * 3,000,000 queries per 100 seconds
    * 1,800,000 queries per minute
    * 300,000 queries per 100 seconds per user
    * 180,000 queries per minute per user

### Tools Used
* Google Cloud Platform
    * [Google Developers Console](https://console.developers.google.com)
    * [YouTube-Data-API-v3](https://console.developers.google.com)
* Youtube_dl: lightweight video downloading library for python
* PyQT5: Python GUI 

### Getting Started - Integrations
1. Create a Google APIs account in https://console.developers.google.com
    * _Note: you'll need a gmail account to do so_
2. Activate your Google Cloud account 
    * _Note: This requires a CC, but for this we'll be using the 90-day free trial_
3. Add the YouTube Data API v3 from the Library tab.
4. Create an environment file within `/src/sec` called `env.json`
    * Add your API Key to it
    ```json
    {
    "data_api_search_uri": "https://www.googleapis.com/youtube/v3/search",
    "api_name": "yt-converter-key_local",
    "api_key": "YOUR-KEY-HERE",
    "api_scope": "https://www.googleapis.com/auth/youtube.force-ssl"
    }
    ```

### Getting Started - Local Environment
1. Get your virtual-environment running:
    * `pip install virtualenv`
    * `python -m venv ./src/venv`
    * `source ./src/venv/Scripts/activate`

2. Download your depenedencies:
    * `pip install --upgrade google-api-python-client google-auth-oauthlib google-auth-httplib2 pyqt5 pyinstaller`
    * `pip install youtube-dl`
    * Download [ffmpeg](https://www.ffmpeg.org/download.html)
        * **Note this is currently already in the ./src/bin folder**
    * Set the ffmpeg binary to your path
        * For Windows: Set the bin folder to your path
            * WIN key > Environment Variables > `Path` > Paste the location
        * Other Option with git & `venv`: Add this line to your venv/Scripts/activate file
            * `export PATH=$PATH:="~\youtube_converter\src\bin\ffmpeg-windows"`
            * Here's an example of where to put it in the activate file:
            ```sh
            VIRTUAL_ENV="C:\Users\blins\dev\projects\youtube_converter\src\venv"
            export VIRTUAL_ENV

            ######################################
            # ADD CUSTOM PATHS HERE
            export PATH=$PATH:="C:\Users\blins\dev\projects\youtube_converter\src\bin\ffmpeg-windows"
            ######################################

            _OLD_VIRTUAL_PATH="$PATH"
            PATH="$VIRTUAL_ENV/Scripts:$PATH"
            export PATH
            ```

### Build the App
* `pyinstaller build.py`
    * Creates a mess of .dll files
* `pyinstaller --onefile build.py -w --name YouTube-Converter`
    * TODO: This is going to require a shell command to capture all of the dependencies

### Developer Snippets
* To test out the entry-point locally:
    * `python build.py`
* To test out FFMPEG:
    * `ffmpeg -i [.mp4 file] [.avi file]`
* To test out youtube-dl (via cli):
    * `youtube-dl --restrict-filenames -i -x --audio-format mp3 https://www.youtube.com/watch?v=xWOoBJUqlbI -o '%(title)s.%(ext)s'`


### References
* [YouTube Data API Overview](https://developers.google.com/youtube/v3/getting-started)
* [Google API Python Client](https://github.com/googleapis/google-api-python-client)
* [YouTube Search API](https://developers.google.com/youtube/v3/docs/search/list)
* [PyQt Sample App](https://www.zeolearn.com/magazine/10-steps-for-getting-started-guis-with-python)
* [Pyinstaller Sample App](https://datatofish.com/executable-pyinstaller/)
* [Complex Pyinstaller Builds](https://realpython.com/pyinstaller-python/)
* [Pyinstaller Usage](https://pyinstaller.readthedocs.io/en/stable/usage.html)
* [YouTube-DL Python App](https://spapas.github.io/2018/03/06/easy-youtube-mp3-downloading/)