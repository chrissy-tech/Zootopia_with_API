import json
import requests

# NOTE: Replace 'YOUR_API_KEY' with your actual key from the API provider (e.g., API-Ninjas)
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "Anu6EgZVogeKQsg9+UDPIg==f8eKjpMoxZdwTjJl"

def fetch_animal_data(animal_name):
	"""
	Fetches animal data from the external API for a given animal name.

	Args:
		animal_name (str): The name of the animal to search for (e.g., "Fox").

	Returns:
		list: A list of dictionaries containing
		animal information, or an empty list on failure.
	"""
	try:
		headers = {'X-Api-Key': API_KEY}
		params = {'name': animal_name}

		response = requests.get(API_URL, headers=headers, params=params, timeout=10)
		response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

		# The API returns a list of dictionaries directly
		return response.json()

	except requests.exceptions.RequestException as e:
		print(f"Error fetching data from API: {e}")
		return []
	except json.JSONDecodeError:
		print("Error: Could not decode JSON response from API.")
		return []