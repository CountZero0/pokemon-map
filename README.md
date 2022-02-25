# Pokemon map 

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/) 

### Subject area 

Site is maid to help with game [Pokemon GO](https://www.pokemongo.com/ en-us/). This is a game about catching [Pokemon] 

The essence of the game is that Pokémon periodically appear on the map for a certain period of time. Each player can catch a Pokémon and add to their personal collection. 

There can be several individuals of the same Pokémon on the map at once: for example, 3 Bulbasaur. Each individual can be caught by several players at once. If a player has caught a Pokémon specimen, it disappears for him, but remains for others.

The game has an evolution mechanic. Pokémon of one kind can "evolve" into another. So, for example, Bulbasaur turns into Ivysaur, and he turns into Venusaur. 

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/) 

### How to run 

To run the site you need Python 3. 

Download the code from GitHub. Then install dependencies 

```sh 
pip install -r requirements.txt 
``` 

Run the development server 

```sh 
python3 manage.py runserver 
``` 

### Environment Variables

Part of the project settings are taken from the environment variables. To define them, create a `.env` file next to `manage.py` and write data there in the following format: `VARIABLE=value`. 

2 variables are available: 
- `DEBUG` — debug mode. Set to True to see debug information in case of an error. 
- `SECRET_KEY` is the secret key of the project 
