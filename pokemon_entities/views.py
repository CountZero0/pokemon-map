from django.http import HttpResponseNotFound
from django.shortcuts import render

import folium

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').all()
    all_pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        try:
            image_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        except ValueError:
            image_url = DEFAULT_IMAGE_URL
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            image_url
        )

    pokemons_on_page = []
    for pokemon in all_pokemons:
        try:
            image_url = request.build_absolute_uri(pokemon.image.url)
        except ValueError:
            image_url = DEFAULT_IMAGE_URL

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    requested_pokemon_entities = requested_pokemon.pokemons.all()

    for pokemon_entity in requested_pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(requested_pokemon.image.url)
        )

    pokemon = {
        'pokemon_id': requested_pokemon.id,
        'title_ru': requested_pokemon.title,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'img_url': request.build_absolute_uri(requested_pokemon.image.url),
        'description': requested_pokemon.description
    }

    if requested_pokemon.evolution_from:
        pokemon['previous_evolution'] = {
            'title_ru': requested_pokemon.evolution_from.title,
            'pokemon_id': requested_pokemon.evolution_from.id,
            'img_url': requested_pokemon.evolution_from.image.url
        }

    next_evolution = requested_pokemon.next_evolutions.first()
    if next_evolution:
        pokemon['next_evolution'] = {
            'title_ru': next_evolution.title,
            'pokemon_id': next_evolution.id,
            'img_url': next_evolution.image.url
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
