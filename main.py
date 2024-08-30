from PIL import Image, ImageTk
import tkinter as tk
import requests
import json

def cerca_anime(animeInputEntry):
  animeInput = animeInputEntry.get()
  get_anime_info(animeInput=animeInput)

def get_anime_info(animeInput):
  try:
    url = f"https://api.jikan.moe/v4/anime?q={animeInput}"

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
  
def main():
  window = tk.Tk()

  window.geometry("600x600")
  window.title("AnimeAhead!")
  window.resizable(False, False)
  tk.Label(window, text="Inserisci qui sotto l'anime di cui vuoi avere informazioni").pack(pady=20)

  animeInputEntry = tk.Entry(window, width=40)
  animeInputEntry.pack(pady=5)

  button = tk.Button(window, text="Invio", command=lambda: cerca_anime(animeInputEntry)).pack(pady=5)

  window.mainloop()


if __name__ == "__main__":
  main()
