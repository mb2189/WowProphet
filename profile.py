import os
import requests
from requests.auth import HTTPBasicAuth


class Blizz():


  def create_access_token(self, region = 'us'):
    url = f"https://{region}.battle.net/oauth/token"
    params = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(os.getenv("client_id"), os.getenv("client_secret"))

    resp = requests.post(url, data=params, auth=auth)
    blizz_token = resp.json()
    return blizz_token['access_token']


  def get_character_image(self, characterName, realmSlug, region = 'us'):
    token = self.create_access_token()
    url = f"https://{region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/character-media?namespace=profile-us&locale=en_US&access_token={token}"

    try:
      resp = requests.get(url)
      par = resp.json()
      image = par['assets'][2]['value']
      return image 
    
    except KeyError:
      return "Character not found"
