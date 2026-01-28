import webbrowser
import os

BASE_DIR = r"C:\Users\tribu\PyCharmMiscProject"
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

class Videos:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False

    def open(self):
        webbrowser.open(self.link)
        self.seen = True

class Playlists:
    def __init__(self, name, info, rate, clips):
        self.name = name
        self.info = info
        self.rate = rate
        self.clips = clips








################################



#############################


def video_input(i):
    title = input(f"Enter video {i + 1} title: ")
    link  = input(f"Enter video {i + 1} link : ")
    video = Videos(title, link)
    return video

def videos_input(i):
    videos = []
    total = choose(f"Enter playlist {i + 1} videos amount:  ", 1, float('inf'))
    for i in range(total):
        video = video_input(i)
        videos.append(video)
    return videos


def playlist_input(i):
    name = input(f"Enter playlist {i + 1} name: ")
    info = input(f"Enter playlist {i + 1} info: ")
    rate = input(f"Enter playlist {i + 1} rate: ")
    clips = videos_input(i)
    playlist = Playlists(name, info, rate, clips)
    return playlist


def playlists_input():
    playlists = []
    total = choose(f"Enter amount of playlists:  ", 1, float('inf'))
    for i in range(total):
        playlist = playlist_input(i)
        playlists.append(playlist)
    return playlists

def choose(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        print(f"'{choice}' is not an option!")
        print(f"Please re-enter again!")
        choice = input(prompt)
    else:
        return int(choice)

def write_playlists(list):
    total = len(list)
    with open("playlists.txt", "w") as f:
        f.write(str(total) + "\n")
        for i in range(total):
            f.write(str(list[i].name) + "\n")
            f.write(str(list[i].info) + "\n")
            f.write(str(list[i].rate) + "\n")
            f.write(str(len(list[i].clips)) + "\n")
            write_videos(list, i)
    while True:
        total += 1
        file = f"video{total-1}.txt"
        try:
            os.remove(file)
        except FileNotFoundError:
            break


def write_videos(list, i):
    videos = list[i].clips
    total = len(videos)
    with open(f"video{i}.txt", "w") as f:
        f.write(str(total) + "\n")
        for j in range(total):
            f.write(str(videos[j].title) + "\n")
            f.write(str(videos[j].link) + "\n")

def read_playlists():
    playlists = []
    with open("playlists.txt", "r") as f:
        total = int(f.readline().strip())
        for i in range(total):
            name = f.readline().strip()
            info = f.readline().strip()
            rate = f.readline().strip()
            clips = f.readline().strip()
            playlist = Playlists(name, info, rate, clips)
            playlists.append(playlist)
            videos = read_videos(i)
            playlist.clips = videos

    return playlists

def read_videos(i):
    videos = []
    with open(f"video{i}.txt", "r") as f:
        total = f.readline().strip()
        for i in range(int(total)):
            title = f.readline().strip()
            link = f.readline().strip()
            video = Videos(title, link)
            videos.append(video)
    return videos

def playlist_print(list, i):
    print(f"- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(f"")
    print(f"Playlist {i + 1} Name : {list[i].name}")
    print(f"Playlist {i + 1} Info : {list[i].info}")
    print(f"Playlist {i + 1} Rate : {list[i].rate}")
    print(f"Playlist {i + 1} Videos amount : {len(list[i].clips)}")

def videos_print(lists):
    total = len(lists)
    for i in range(total):
        print(f"            |")
        print(f"            |__Video {i + 1} Title : {lists[i].title}")
        print(f"            |__Video {i + 1} Link  : {lists[i].link}")

def playlists_print(lists):
    total = len(lists)
    for i in range(total):
        playlist_print(lists, i)
        videos_print(lists[i].clips)

def show_menu():
    print("")
    print("---------- Playlist Launcher ----------")
    print("Option 1 : Create Playlist")
    print("Option 2 : Show Playlist")
    print("Option 3 : Play Video")
    print("Option 4 : Edit Playlist")
    print("Option 5 : Edit Video")
    print("Option 6 : Save")
    print("Option 7 : Exit")


def menu_1():
    playlists = playlists_input()
    return playlists
def ask_(playlists):
    while True:
        ask = input(f"Do you want to save your playlists? (Y-N) : ")
        if ask in ("y", "Y", "yes", "Yes"):
            write_playlists(playlists)
            break
        elif ask in ("n", "N", "no", "No"):
            break
        else:
            print(f"'{ask}' is not an option. Please Re-Enter!")


def menu_2():
    lists = read_playlists()
    playlists_print(lists)

def menu_3():
    lists = read_playlists()
    playlists_print(lists)
    total = len(lists)
    choice = choose(f"Enter Playlist (1-{total}) : ", 1, total)
    videos = lists[choice-1].clips
    total2 = len(videos)
    choice2 = choose(f"Enter Video (1-{total2}) : ", 1, total2)
    videos[choice2 - 1].open()


def main():
    #playlists = playlists_input()
    ##write_playlists(playlists)
    #lists = read_playlists()
    #print(lists[1].clips)
    #playlists_print(lists)

    show_menu()
    while True:
        print(f"'0' to show menu")
        choice = choose(f"Enter option (1-7) :  ", 0, 7)
        if choice == 1:
            playlists = menu_1()
            ask_(playlists)
        elif choice == 2:
            menu_2()
        elif choice == 3:
            menu_3()
        elif choice == 4:
            menu_4()
        elif choice == 5:
            menu_5()
        elif choice == 6:
            write_playlists(playlists)
            print(f"Playlists saved!")
        elif choice == 7:
            menu_7()
        else:
            main()


main()