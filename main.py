from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.pegar_tempo("USD")
        self.root.ids["tempo1"]. text = "São Paulo - Chuva"
        self.root.ids["tempo2"]. text = "Rio de Janeiro - Nublado"
        self.root.ids["tempo3"]. text = "Santa Catarina - Ensolarado"
        self.root.ids["tempo4"]. text = "Acre - Chuva intensa"

def pegar_tempo(self, tempo):
    link = f"https://economia.awesomeapi.com.br/last/{tempo}-BRL"
    requisicao = requests.get(link)
    print(requisicao.json())
    


MeuAplicativo().run()

