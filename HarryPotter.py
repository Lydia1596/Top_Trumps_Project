import random
import requests

def random_character():
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)
    characters = response.json()
    character = random.choice(characters)
    return character
def run():
    my_character = random_character()
    print('You were given {}'.format(my_character['name']))

# if __name__ == "__main__":
run()