###
# Helper methods for API Client
# API sample client for OMDB API: http://omdbapi.com/
###

import requests
import json
apiKey=''
# Helper method to parse the different critic ratings input
def parse_critic_scores(critic_scores: list[str]) -> float:
  num_of_ratings = len(critic_scores)
  total_score = 0.0

  for critic_rating in critic_scores:
    source = critic_rating['Source']
    value = critic_rating['Value']
    score = 0.0
    if source == 'Internet Movie Database':
      value = float(value.split("/")[0])
      score = value * 10
    elif source == 'Rotten Tomatoes':
      score = float(value.split("%")[0])
    elif source == 'Metacritic':
      score = float(value.split("/")[0])
    total_score += round(score / num_of_ratings, 1)
    
  return total_score
  
# Helper method to print the values of our results in a readable format
def print_results(responseBody: dict) -> None:
  """
  Prints the contents of an omdbapi response
  """
  # print (responseBody)
  print("\nTitle of the movie: ", responseBody['Title'])
  print("Year: ", responseBody['Year'])
  print("Rating: ", responseBody['Rated'])
  print("Genres: ", responseBody['Genre'])
  print("Critic Scores", responseBody['Ratings'], "\n")


# Helper method to call API
def get_info_from_api(title: str, year: str) -> dict:
  """
  Return a dictionary containing the API response from an omdbapi search for a title and year
  Raises Exception if there is no response
  """
  url = 'http://www.omdbapi.com/'
  headers = {
    'Accept': 'application/json'
  }
  single_search_payload = {'i': 'tt3896198', 'apikey': apiKey}
  # multiple_search_payload = {'s': title, 'type': media_type, 'apiKey': apiKey}
  
  r = requests.get(url=url, params=single_search_payload, headers=headers)
  responseBody = json.loads(r.text)
  if responseBody['Response'] == "False":
    print(responseBody['Error'])
    raise Exception("Error in the search")
  else:
    print_results(responseBody)
    return responseBody
    
# ******************************************************