import json
from data_fetch import fetch_animal_data


def animals_information(animals_data):
    """
        Prints essential information (Name, Diet, Location, Type)
        for each fetched animal.
        """
    if not animals_data:
        print("No animal data available to display.")
        return

    for animal in animals_data:
        name_animal = animal.get("name")
        characteristics_animal = animal.get("characteristics", {})
        diet_animal = characteristics_animal.get("diet")
        location_animal = animal.get("locations", [])
        first_location = location_animal[0] if location_animal else "N/A"
        type_animal = characteristics_animal.get("type")

        print(f"Name: {name_animal}")
        print(f"Diet: {diet_animal}")
        print(f"Location: {first_location}")
        if type_animal:
            print(f"Type: {type_animal}")
        print("-" * 20)

def generate_html_output(animals_data,
						 template_path="animals_template.html",
						 output_path="animals.html"):
	"""
	Fetches animals, serializes them into HTML, and writes the output to a file.

	Args:
		animals_data (list): A list of animal data fetched from the API.
		template_path (str): Path to the HTML template file.
		output_path (str): Path where the final HTML should be written.
	"""
	try:
		# Read the HTML template
		with open(template_path, "r", encoding="utf-8") as file:
			template = file.read()
	except FileNotFoundError:
		print(f"Error: HTML template not found at {template_path}")
		return

	output_html = serialize_animals_to_html(animals_data)
	final_html = template.replace("__REPLACE_ANIMALS_INFO__",
								  output_html)

	with open(output_path, "w", encoding="utf-8") as file:
		file.write(final_html)
	print(f"Successfully generated website: {output_path}")


def serialize_animals_to_html(animals_data):
	"""Serializes a list of animal dictionaries into HTML list items."""
	output = ""
	if not animals_data:
		return '<li class="cards__item"><div class="card__title">No animals found via API.</div></li>'

	for animal in animals_data:
		# (complete logic for extracting animal data)
		name_animal = animal.get("name")
		characteristics_animal = animal.get("characteristics", {})
		diet_animal = characteristics_animal.get("diet")
		type_animal = characteristics_animal.get("type")
		location_animal = animal.get("locations", [])
		first_location = location_animal[
			0] if location_animal else "N/A"
		weight_animal = characteristics_animal.get("weight")
		length_animal = characteristics_animal.get("length")

		output += '<li class="cards__item">\n'
		output += f'    <div class="card__title">{name_animal}</div>\n'
		output += '         <div class="card__text">\n'
		output += '             <ul class="card__list">\n'
		output += f'    <li class="card__list-item"><strong>Diet:</strong> {diet_animal}</li>\n'
		output += f'    <li class="card__list-item"><strong>Location:</strong> {first_location}</li>\n'

		if type_animal:
			output += f'    <li class="card__list-item"><strong>Type:</strong> {type_animal}</li>\n'
		if weight_animal:
			output += f'    <li class="card__list-item"><strong>Weight:</strong> {weight_animal}</li>\n'
		if length_animal:
			output += f'    <li class="card__list-item"><strong>Length:</strong> {length_animal}</li>\n'
		output += '             </ul>\n'
		output += '         </div>\n'
		output += '     </li>\n'
	return output


# --- MAIN EXECUTION BLOCK ---

if __name__ == "__main__":
	SEARCH_TERM = "Fox"

	# 1. Retrieve data (one-time)
	print(f"Fetching data for: {SEARCH_TERM}...")
	all_animals_data = fetch_animal_data(SEARCH_TERM)

	# 2. Generate console output
	print("\n--- Console Output ---")
	animals_information(all_animals_data)

	# 3. Generate HTML output
	print("\n--- HTML Generation ---")
	generate_html_output(all_animals_data)
