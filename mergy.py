import requests

def upload_reel(access_token, caption, video_url):
    # Step 1: Upload the video file to Facebook
    video_upload_url = f"https://graph-video.facebook.com/v12.0/me/videos?access_token={access_token}"
    video_data = {
        "title": "Reel Title",
        "description": caption,
        "source": open(video_url, 'rb')
    }
    video_response = requests.post(video_upload_url, files=video_data)
    video_id = video_response.json()['id']

    # Step 2: Create an Instagram media container
    container_url = f"https://graph.facebook.com/v12.0/{video_id}/media?access_token={access_token}"
    container_response = requests.post(container_url)
    container_id = container_response.json()['id']

    # Step 3: Publish the reel to Instagram
    publish_url = f"https://graph.facebook.com/v12.0/{container_id}/publish?access_token={access_token}"
    publish_data = {
        "caption": caption
    }
    publish_response = requests.post(publish_url, data=publish_data)

    if publish_response.status_code == 200:
        print("Reel uploaded successfully to Instagram!")
    else:
        print("Failed to upload reel to Instagram.")

# Replace with your actual access token, reel caption, and video URL
access_token = "EAAyZB57dwiyUBAPq6pHpmBPqUYWKF3ZCJAyBL7oGcffD9ilBoj8vMgfrTJ5zq1QRhAK0gDm2pFEzq8y9WCjpkE3ZBTHFDJBfCoCap74spzk54ZA5oWVDGjFXZA1z84CxpbZAjuIYpkgzY5PbZCKoJIlnr5rZCO2en3Nys5ZAbRBcOVEDW0qgcS8MPCScV9lQjSYn9GFgMlZCf5bZCTEBOWjrnNP"
caption = "This is my awesome reel!"
video_url = r"C:\Users\adity\Music\hello\secy ready\merged_merged_0C46B34BA450DA6BD37C81B9900C16B8_video_dashinit_46.mp4"

upload_reel(access_token, caption, video_url)