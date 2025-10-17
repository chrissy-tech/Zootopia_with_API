import json
import requests
from dotenv import load_dotenv  # Import the loading function
import os

#Loads environment variables from the .env file
load_dotenv()

#Reads the API key from the environment variable
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")

if not API_KEY:
	raise ValueError("API_KEY not found. Please check your .env file"
					 " and ensure it is structured correctly.")


def fetch_animal_data(animal_name):
	"""
	Fetches the animals data for the animal 'animal_name' from the API.
	Returns: a list of animals, each animal is a dictionary.
	"""
	try:
		headers = {'X-Api-Key': API_KEY}
		params = {'name': animal_name}

		response = requests.get(API_URL, headers=headers,
								params=params, timeout=10)
		response.raise_for_status()  # Raise HTTPError for bad responses

		# The API returns a list of dictionaries directly
		return response.json()

	except requests.exceptions.RequestException as e:
		print(f"Error fetching data from API: {e}")
		return []
	except json.JSONDecodeError:
		print("Error: Could not decode JSON response from API.")
		return []
