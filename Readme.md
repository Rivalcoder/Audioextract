# 🎶 YouTube Audio Extractor API

This project provides a simple Flask-based API to extract audio from YouTube videos using **yt-dlp**. It serves a web interface where users can input a YouTube URL and download the extracted audio in MP3 format. 🚀

## 🛠️ Features

- Extracts high-quality audio 🎵 from YouTube videos.
- Returns the extracted audio as an MP3 file. 🎧
- Simple web interface built with Flask. 🌐
- Efficient audio extraction using `yt-dlp`. ⚡

## 📂 Project Structure

```bash
├── api
│   └── main.py         # Main Flask app
├── static              # Folder to store extracted audio
├── templates
│   └── index.html      # HTML for the web interface
└── README.md           # Project documentation
```

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have the following installed:

- 🐍 Python 3.x
- 📦 Flask (`pip install Flask`)
- 🎬 yt-dlp (`pip install yt-dlp`)
- 🎛️ FFmpeg (for audio extraction)

### 2️⃣ Running the Application

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/youtube-audio-extractor.git
   cd youtube-audio-extractor

2. To install the required Python packages, run the following command:

    ```bash
    pip install -r requirements.txt
    ```

### 3️⃣ Start the Flask Application

1. Run the following command to start the Flask app:

    ```bash
    python api/main.py

### 4️⃣ Open in Browser
- Once the app is running, open your browser and go to:
    ```bash 
    http://127.0.0.1:5000

### 5️⃣ Using the API
    - Endpoint: /extract_audio

    - Method: POST

   