import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests
from io import BytesIO
from PIL import Image

class AnimeFinder(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AnimeAhead!")
        self.setGeometry(100, 100, 800, 600)

        self.main_layout = QVBoxLayout()

        self.label = QLabel("Inserisci qui sotto l'anime di cui vuoi avere informazioni")
        self.main_layout.addWidget(self.label)

        self.animeInputEntry = QLineEdit(self)
        self.animeInputEntry.setPlaceholderText("Nome dell'anime")
        self.main_layout.addWidget(self.animeInputEntry)

        self.button = QPushButton("Invio", self)
        self.button.clicked.connect(self.find_anime)
        self.main_layout.addWidget(self.button)

        self.result_layout = QHBoxLayout()

        self.image_label = QLabel(self)
        self.result_layout.addWidget(self.image_label)

        self.text_layout = QVBoxLayout()
        self.result_layout.addLayout(self.text_layout)

        self.nomeAnimeLabel = QLabel("")
        self.text_layout.addWidget(self.nomeAnimeLabel)

        self.nEpisodiLabel = QLabel("")
        self.text_layout.addWidget(self.nEpisodiLabel)

        self.studioLabel = QLabel("")
        self.text_layout.addWidget(self.studioLabel)

        self.votoLabel = QLabel("")
        self.text_layout.addWidget(self.votoLabel)

        self.tramaText = QTextEdit(self)
        self.tramaText.setReadOnly(True)
        self.text_layout.addWidget(self.tramaText)

        self.main_layout.addLayout(self.result_layout)

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.clicked.connect(self.clear_labels)
        self.main_layout.addWidget(self.clearButton)

        self.setLayout(self.main_layout)

    def find_anime(self):
        animeInput = self.animeInputEntry.text()
        self.get_anime_info(animeInput)

    def get_anime_info(self, animeInput):
        try:
            url = f"https://api.jikan.moe/v4/anime?q={animeInput}"
            response = requests.get(url)
            animeInfo = response.json()

            imageUrl = animeInfo["data"][0]["images"]["jpg"]["large_image_url"]
            nomeAnime = animeInfo["data"][0]["title_english"]
            nEpisodi = animeInfo["data"][0]["episodes"]
            studio = animeInfo["data"][0]["studios"][0]["name"]
            voto = animeInfo["data"][0]["score"]
            trama = animeInfo["data"][0]["synopsis"]

            img_data = requests.get(imageUrl).content
            img = Image.open(BytesIO(img_data))
            img = img.resize((200, 300))
            img.save("temp_image.jpg")

            pixmap = QPixmap("temp_image.jpg")
            self.image_label.setPixmap(pixmap)

            self.nomeAnimeLabel.setText(f"Nome Anime: {nomeAnime}")
            self.nEpisodiLabel.setText(f"N. Episodi: {nEpisodi}")
            self.studioLabel.setText(f"Studio: {studio}")
            self.votoLabel.setText(f"Voto: {voto}")
            self.tramaText.setText(trama)

        except Exception as e:
            print(e)

    def clear_labels(self):
        self.image_label.clear()
        self.nomeAnimeLabel.setText("")
        self.nEpisodiLabel.setText("")
        self.studioLabel.setText("")
        self.votoLabel.setText("")
        self.tramaText.clear()
        self.animeInputEntry.clear()

def main():
    app = QApplication(sys.argv)
    window = AnimeFinder()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
