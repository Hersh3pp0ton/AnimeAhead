import tkinter as tk
import requests
import json

window = tk.Tk()

window.geometry("600x600")
window.title("AnimeAhead!")
window.resizable(False, False)

animeInput = input("Inserisci l'anime di cui vuoi avere informazioni: ")

url = f"https://api.jikan.moe/v4/anime?q={animeInput}"

try:
  response = requests.get(url)
  animeInfo = response.json()

  nomeAnime = animeInfo["data"][0]["title_english"]
  nEpisodi = animeInfo["data"][0]["episodes"]
  studio = animeInfo["data"][0]["studios"][0]["name"]
  voto = animeInfo["data"][0]["score"]
  trama = animeInfo["data"][0]["synopsis"]

  if nomeAnime == None:
    print(f"\nNome: {animeInput}")
  else:
    print(f"\nNome: {nomeAnime}")
  print(f"N. episodi: {nEpisodi}")
  print(f"Studio: {studio}")
  print(f"Voto: {voto}")
  print(f"Trama:\n{trama}\n")
except:
  print(f'Non abbiamo trovato niente inerente a "{animeInput}" :(')