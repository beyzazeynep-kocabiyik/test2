import tkinter as tk
import json
import wikipedia

class ŞehirRehberi():
    def __init__(self):
        with open("bilgiler.json", "r", encoding="utf-8") as dosya:
            self.veriler = json.load(dosya)

        self.pencere = tk.Tk()
        self.pencere.title("Şehir Rehberi")

        self.şehir_etiketi = tk.Label(self.pencere, text="Şehir:")
        self.şehir_etiketi.pack()

        self.şehir_girdisi = tk.Entry(self.pencere)
        self.şehir_girdisi.pack()

        self.bilgi_butonu = tk.Button(self.pencere, text="Bilgi Getir", command=self.bilgi_getir)
        self.bilgi_butonu.pack()

        self.bilgi_alani = tk.Text(self.pencere, wrap=tk.WORD)
        self.bilgi_alani.pack()

    def bilgi_getir(self):
        şehir = self.şehir_girdisi.get().strip().title()
        self.bilgi_alani.delete("1.0", tk.END)
        try:
            şehir_verisi = self.veriler[şehir]
            self.bilgi_alani.insert(tk.END, f"{şehir} şehrinde gidilebilecek yerler:\n")
            for i, yer in enumerate(şehir_verisi.get('attractions', []), 1):
                self.bilgi_alani.insert(tk.END, f"\t{i}. {yer}\n")
            if 'foods' in şehir_verisi:
                self.bilgi_alani.insert(tk.END, "\nYenilecekler:\n")
                for i, yemek in enumerate(şehir_verisi['foods'], 1):
                    self.bilgi_alani.insert(tk.END, f"\t{i}. {yemek}\n")
        except KeyError:
            self.bilgi_alani.insert(tk.END, "Şehir bulunamadı.\n")
            
        try:
            wikipedia.set_lang("tr")
            wiki_info = wikipedia.page(şehir).content[:1000]
            self.bilgi_alani.insert(tk.END, "\nWikipedia Bilgisi:\n")
            self.bilgi_alani.insert(tk.END, wiki_info)
        except wikipedia.exceptions.PageError:
            self.bilgi_alani.insert(tk.END, "Wikipedia'da bu şehir hakkında bilgi bulunamadı.")

    def çalıştır(self):
        self.pencere.mainloop()

if __name__ == "__main__":
    rehber = ŞehirRehberi()
    rehber.çalıştır()