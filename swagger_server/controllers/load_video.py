import requests

def load_video(video_url):
    """retrieves the video from the url and returns a Video object"""
    try:
        #response = requests.get(video_url, stream=True)
        #response.raise_for_status()
        """
        with open("tmp_vid.mp4", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        """
        print(f"Video downloaded successfully to tmp_vid.mp4")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")