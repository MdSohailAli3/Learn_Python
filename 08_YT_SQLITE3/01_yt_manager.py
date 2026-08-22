import sqlite3
import time as tm

conn = sqlite3.connect("youtube_database.db")

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print()
    print("*" * 70)
    for row in cursor.fetchall():
        print(row)
    print("*" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    print("Video Added Successfully.")
    conn.commit()
    
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name,new_time,video_id))
    print("Video Updated Successfully.")
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    print("Video Deleted Successfully.")
    conn.commit()

def main():
    
    while True:
        print("\nYoutuber Manager-")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit Manager")
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter video time: ")
                add_video(name,time)
            case '3':
                list_videos()
                video_id = input("Enter video id to update: ")
                name = input("Enter the video name: ")
                time = input("Enter video time: ")
                update_video(video_id,name,time)
            case '4':
                list_videos()
                video_id = int(input("Enter video id to delete: "))
                delete_video(video_id)
            case '5':
                print("\nEXITING THE PROGRAM",end="")
                for i in range(3):
                    print(".",end="")
                    tm.sleep(.5)

                break
            case _:
                print("Invalid Choice!!!")
    
    conn.close()


if __name__ == "__main__":
    main()

