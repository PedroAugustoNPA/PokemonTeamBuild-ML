
import requests as rs
import pandas as pd
import time

dados_pokemon = []
url = "https://pokeapi.co/api/v2/pokemon/"

for i in range(1, 152):
    answer  = rs.get(f"{url}{i}")
    if answer.status_code == 200:
        poke = answer.json()

        try:
            tipo_2 = poke["types"][1]["type"]["name"]
        except(IndexError, KeyError):
            tipo_2 = None

        info = {
            "id": poke["id"],
            "name": poke["name"],
            "hp": poke["stats"][0]["base_stat"],
            "attack": poke["stats"][1]["base_stat"],
            "defense": poke["stats"][2]["base_stat"],
            "speed": poke["stats"][5]["base_stat"],
            "special": poke["past_stats"][0]["stats"][0]["base_stat"],
            "type_1": poke["types"][0]["type"]["name"],
            "type_2": tipo_2
        }
        dados_pokemon.append(info)
    time.sleep(0.5)

df = pd.DataFrame(dados_pokemon)

df.to_csv("data/raw/pokemon_raw.csv", index = False) 

print(df)        



        



