''' Keep for future reference.
import os
import tweepy

# Load credentials from environment variables
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

# Authenticate with Tweepy (OAuth 1.0a)
auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_SECRET
)

api = tweepy.API(auth)


def post_tweet(text, media_id=None):
    """
    Sends a tweet with optional media.
    """
    try:
        if media_id:
            response = api.update_status(status=text, media_ids=[media_id])
        else:
            response = api.update_status(status=text)
        return response
    except Exception as e:
        print("Error posting tweet:", e)
        return None


def upload_media(image_path):
    """
    Uploads an image to X (Twitter) using Tweepy.

    This helper function uploads an image file and returns the
    media ID, which can be attached to a tweet via post_tweet.

    Parameters:
        image_path (str): The file path to the image being uploaded.

    Returns:
        str or None: The media ID string if upload succeeds,
                     or None if the upload fails.
    """
    try:
        media = api.media_upload(image_path)
        return media.media_id_string
    except Exception as e:
        print("Error uploading media:", e)
        return None
'''
