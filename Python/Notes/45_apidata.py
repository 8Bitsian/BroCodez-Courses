# Requesting API Data
# How to connect to an API using Python

# Import the requests library to make an API request
# You will have to install this via the terminal using `pip install requests`
import requests 

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response) Prints "<Response [200]>" (an HTTP code that means the request succeeded)

    if (response.status_code == 200):
        print("Pokemon found!")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"ERROR: {status_code} - Failed to retrieve data")

def main():
    pokemon_name = "squirtle"
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"  Name: {pokemon_info['name'].capitalize()}")
        print(f"    ID: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']} ft")
        print(f"Weight: {pokemon_info['weight']} lbs")

if __name__ == "__main__":
    main()