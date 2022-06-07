import requests
from tkinter import * 

base_url = "https://api.openweathermap.org/data/2.5/weather?"   
api_key = ''

def HavaDurumu(sehir):
    URL = base_url + "appid=" + api_key + "&q=" + sehir
    data = requests.get(URL)
    data = data.json()
    aciklama = data["weather"][0]["description"]
    sehir_ismi = data["name"]
    ulke = data["sys"]["country"]
    sicaklik = data["main"]["temp"]
    sicaklik = round((float(sicaklik)-273.15),1)

    return (sehir_ismi,ulke,sicaklik,aciklama)

def main():
    sehir = giris.get()
    havaDurumu = HavaDurumu(sehir)
    KonumL["text"] = havaDurumu[0],",",havaDurumu[1]
    SicaklıkL["text"] = havaDurumu[2] , "°C"
    AciklamaL["text"] = havaDurumu[3] 

app = Tk()
app.geometry("400x400")
app.configure(background='light yellow')
app.title("Hava Durumu")
giris = Entry(app,justify='center')
giris.pack(fill=BOTH,ipady=10,padx=50,pady=10)
giris.focus()

enterButon = Button(text="ENTER",font="Arial 10 bold",background="light cyan",command=main)
enterButon.pack()

KonumL = Label(app,font="Arial 20")
KonumL.pack()
SicaklıkL = Label(app,font="Arial 20")
SicaklıkL.pack()
AciklamaL = Label(app,font="Arial 20")
AciklamaL.pack()

app.mainloop()
