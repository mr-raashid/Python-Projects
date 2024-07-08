import json

def load_data():
  try:
    with open("youtube.txt", 'r') as file:
      return json.load(file)
  except:
    return []
  
def save_data_helper(videos):
  with open("youtube.txt", 'w') as file:
    json.dump(videos, file)

def list_all_videos(videos):
  print("\n")
  print("*" * 60)
  for index, video in enumerate(videos, start=1):
    print(f"{index}. {video['name']}, Duration is {video['time']}")

  print("\n")
  print("*" * 60)

def add_video(videos):
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  videos.append({"name" : name, "time" : time})
  save_data_helper(videos)

def update_video(videos):
  list_all_videos(videos)
  update_video = int(input("Enter video number to update: "))
  if 1 <= update_video <= len(videos):
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[update_video-1] = {"name" : name, "time" : time}
    save_data_helper(videos)
  else:
    print("Invalid number")

def delete_video(videos):
  list_all_videos(videos)
  delete_video = int(input("Enter video number to delete: "))
  if 1 <= delete_video <= len(videos):
    del videos[delete_video - 1]
    save_data_helper(videos)
    print(f"Deleted video {delete_video} successfully")
  else:
    print("Enter a valid number")

def main():
  while True:
    videos = load_data()
    print("\n")
    print("YouTube Manager || Choose an option")
    print("1.List all YouTube videos")
    print("2.Add a YouTube video")
    print("3.Update a YouTube video details")
    print("4.Delete a YouTube video")
    print("5.Exit the app")
    print("-" * 60)
    choice = int(input("Enter your choice: "))

    match choice:
      case 1:
        list_all_videos(videos)

      case 2:
        add_video(videos)

      case 3:
        update_video(videos)

      case 4:
        delete_video(videos)

      case 5:
        break

      case _:
        print("Enter a valid choice")

if __name__ == "__main__":
  main()