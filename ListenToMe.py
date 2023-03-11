from gtts import gTTS
from playsound import playsound

def ListenToMe(ListenToMe):
    ListenToMe= gTTS(text=ListenToMe, lang="es", slow=False)
    ListenToMe.save("ListenToMe.mp3")
    
def run():
	Text="Analizando"
	ListenToMe(Text)
	print(Text)
	playsound("ListenToMe.mp3")
	Text="Ejecucion terminada"
	ListenToMe(Text)
	print(Text)
	playsound("ListenToMe.mp3")


if __name__ == "__main__":
    run()
