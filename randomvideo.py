import urllib.request
from random import randrange
import json

api_key = "{API_KEY}"

def random_video():
  # Uses the Youtube API to get a list of the 50 most recent videos uploaded
  # to the two selected channels, using their upload IDs as the playlist ID.
  # Selects a random number and returns the lucky video to the calling
  # function.

  response = (urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails%2Cstatus&maxResults=50&playlistId=UUzCWehBejA23yEz3zp7jlcg&key=" + api_key).read()).decode("utf-8")
  decoded = json.loads(response)
  videolist = decoded['items']
  response = (urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails%2Cstatus&maxResults=50&playlistId=UUDLkzWN1rHY4eYkGnVruHVw&key=" + api_key).read()).decode("utf-8")
  decoded = json.loads(response)
  videolist += decoded['items']
  chosen_one = randrange(len(videolist))
  return("https://youtu.be/" + videolist[chosen_one]['contentDetails']['videoId'])
