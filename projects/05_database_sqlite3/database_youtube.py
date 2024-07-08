import sqlite3

conn = sqlite3.connect("youtube.db")

cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
            ''')

def list_all_videos():
  cur.execute("SELECT * FROM videos")
  for row in cur.fetchall():
    print(row)

def add_video(name, time):
  cur.execute("INSERT INTO videos(name, time) Values (?, ?)", (name, time))
  conn.commit()

def update_video(video_id, new_name, new_time):
  cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
  conn.commit()

def delete_video(video_id):
  cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  conn.commit()

def main():
  while True:
    print("\n")
    print("YouTube Manager with database || Choose an option")
    print("1.List all YouTube videos")
    print("2.Add a YouTube video")
    print("3.Update a YouTube video details")
    print("4.Delete a YouTube video")
    print("5.Exit the app")
    print("-" * 60)
    choice = int(input("Enter your choice: "))

    if choice == 1:
      list_all_videos()
    
    elif choice == 2:
      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      add_video(name, time)

    elif choice == 3:
      video_id = input("Enter video ID to update: ")
      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      update_video(video_id, name, time)

    elif choice == 4:
      video_id = input("Enter video ID to delete: ")
      delete_video(video_id)

    elif choice == 5:
      break

    else:
      print("Invalid choice")

  conn.close()

if __name__ == "__main__":
  main()