# Building music player with python 

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMT"] = "hide"        #optional just to hide the support prompt 
import pygame 

#DEFINING FUNCTION OF play_music 
def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)

    if not os.path.exists(file_path):
        print("File not found")
        return    

    #TO LOAD THE FILE 
    pygame.mixer.music.load(file_path)
    #TO PLAY THE MUSIC 
    pygame.mixer.music.play() 

    print(f"\nNow playing {song_name}")

    #COMMANDS 
    print("Commands: [p]ause, [R]esume, [S]top")
    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stoped")
            return 
        else: 
            print("Invalid command")

def main():

    try:
        #initialize pygames audio mixer 
        pygame.mixer.init()

    except pygame.error as e:                     #with e, youll know the reason of the error
        print("audio initialization failed", e)
        return 

    folder = "Music"

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found")
        return
    
    #LIST OF MP3 FILES
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    if not mp3_files: 
        print("No .mp3 files found")

    while True:
        print("##### MP3 PLAYER #####")
        print("My song list: ")

        for index, song in enumerate(mp3_files, start=1):     #NOTE: enumerate() is a Python function that gives you two things at once when looping: the index number and the value
            print(f"{index}.{song}")
        
        #INPUT
        choice_input = input("\nEnter the song # to play (or 'q' to quite): ")
            
        if choice_input.lower() == "q":
            print("see ya later")
            break 

        if not choice_input.isdigit():
            print("Enter valid number")
            continue 
        
        #typecasting to integer         
        choice = int(choice_input) - 1        # subtracting 1 to match the song number with the index number (cause index number starts with 0)


        if 0 <= choice < len(mp3_files):      # if my choice falls between 0 and 4 then well play a song 
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main() 



