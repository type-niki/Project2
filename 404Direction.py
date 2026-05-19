import webbrowser
from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Back.BLACK + Fore.CYAN + "\n 404Direction AI Study Companion \n" + Style.RESET_ALL)

name = input(Fore.YELLOW + "What's your name? ")
topic = input(Fore.YELLOW + "What are you learning today? ")
mood = input(Fore.YELLOW + "How are you feeling (confused/motivated/tired)? ").lower()

print("\n" + Fore.CYAN + " AI RESPONSE \n")

songs = {
    "confused": {
        "title": "MARINA - Late Bloomer",
        "link": "https://www.youtube.com/results?search_query=MARINA+Late+Bloomer"
    },
    "tired": {
        "title": "Lo-fi study beats",
        "link": "https://www.youtube.com/results?search_query=lofi+study+beats+live"
    },
    "motivated": {
        "title": "Coding motivation music",
        "link": "https://www.youtube.com/results?search_query=coding+motivation+music"
    }
}

if mood == "confused":
    print(Fore.BLUE + f"{name}, confusion means you're actively learning {topic}.")
    print(Fore.BLUE + "Break it into small 20-minute sessions.")

elif mood == "tired":
    print(Fore.MAGENTA + "Low energy detected. Switch to light revision or watch a short tutorial.")

elif mood == "motivated":
    print(Fore.GREEN + "Perfect energy. Build something small using what you're learning.")

else:
    print(Fore.WHITE + "Keep going. Progress doesn’t depend on perfect mood.")

# Song feature
if mood in songs:
    song = songs[mood]
    print(Fore.CYAN + f"\nSuggested song: {song['title']} 🎧")

    play = input(Fore.YELLOW + "Do you want me to play it? (yes/no): ").lower()

    if play == "yes":
        webbrowser.open(song["link"])
        print(Fore.GREEN + "Opening your focus sound... 🎵")
    else:
        print(Fore.WHITE + "Alright. Stay in your rhythm.")

# Micro plan
print(Fore.CYAN + "\nToday's micro-task:")
print(Fore.WHITE + f"- 20 mins learning {topic}")
print(Fore.WHITE + "- 10 mins practice")
print(Fore.WHITE + "- 5 mins recap")

print(Fore.CYAN + "\nStay consistent. Not perfect. Just consistent.")