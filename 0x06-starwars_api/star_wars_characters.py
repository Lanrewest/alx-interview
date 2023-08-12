import requests
import sys

def get_movie_characters(movie_id):
    url = "https://swapi.dev/api/films/{}/".format(movie_id)
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        character_urls = movie_data["characters"]

        for character_url in character_urls:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                print(character_data["name"])
            else:
                print(f"Error fetching character data for URL: {character_url}")
    else:
        print(f"Error fetching movie data for Movie ID: {movie_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie ID>")
        sys.exit(1)

    movie_id = sys.argv[1]
