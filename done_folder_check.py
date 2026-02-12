# UserDir/Videos/record.txtから連結済みの月を確認する
import os
from pathlib import Path

def done_folder_check():
    home = Path.home()
    video_dir = f"{home}\\Videos"
    done_folders = []
    if os.path.exists(f"{video_dir}\\record.txt"):
        with open(f"{video_dir}\\record.txt",mode="r",encoding="utf_8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                done_folders.append(line)
    return done_folders

# UserDir/Videos/record.txtに連結済みの月を追記する
def done_folder_add(folder_name):
    home = Path.home()
    video_dir = f"{home}\\Videos"
    with open(f"{video_dir}\\record.txt",mode="a",encoding="utf_8") as f:
        f.writelines(f"{folder_name}\n")
    return

#テスト
if __name__ == "__main__":
    pass
    #done_folders = done_folder_check()
    #print(done_folders)
    #done_folder_add("2023年05月")