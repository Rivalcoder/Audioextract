# api/extract_audio.py

import yt_dlp
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/extract_audio', methods=['POST'])
def extract_audio():
    youtube_url = request.json['url']
    output_audio_file = './static/extracted_audio'  # Store audio in the static folder
    
    # YouTube-dl options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_audio_file}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    # Download the audio using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    # Return the path of the MP3 file to the frontend
    return jsonify({"audio_file": '/static/extracted_audio.mp3'})

if __name__ == '__main__':
    app.run(debug=True)
