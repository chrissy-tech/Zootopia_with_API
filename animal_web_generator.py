import json

def load_data(file_path):
     """Loads a JSON file and returns it as a dictionary."""
     with open(file_path, "r") as handle:
         return json.load(handle)

animals_data = load_data("animals_data.json")


def animals_information():
    for animal in animals_data:
        name_animal = animal.get("name")
        print(f"Name: {name_animal}")

        characteristics_animal = animal.get("characteristics")
        diet_animal = characteristics_animal.get("diet")
        print(f"Diet: {diet_animal}")

        location_animal = animal.get("locations", [])
        first_location = location_animal[0]
        print(f"Location: {first_location}")

        type_animal = characteristics_animal.get("type")
        if type_animal:  # Only print if type exists and is not empty
            print(f"Type: {type_animal}")

        print()
animals_information()