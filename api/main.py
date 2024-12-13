# api/main.py

import yt_dlp
from flask import Flask, render_template, request, jsonify
import os

# Create the Flask app
app = Flask(__name__)

# Route to serve the index.html page
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html page from the templates folder

# Endpoint for extracting audio from YouTube
@app.route('/extract_audio', methods=['POST'])
def extract_audio():
    try:
        # Get the YouTube URL from the request
        youtube_url = request.json['url']
        
        # Define where to save the audio file
        output_audio_file = './static/extracted_audio'  # Store audio in the static folder
        
        # yt-dlp options for downloading audio
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
    
    except Exception as e:
        # If something goes wrong, return the error message
        return jsonify({"error": str(e)})

# The following line is not needed in serverless functions on Vercel
# if __name__ == '__main__':
#     app.run(debug=True)
