import os
import glob

# 2026/02/02 リネーム処理と判定を分割(リネーム処理を行う関数)
def rename( video_dir ):
    
    #全ての動画ファイルのパスからリネームが必要なファイルを判定してリネームを行う
    folders = sorted(glob.glob(f"{video_dir}\\*月"))
    for folder in folders:      #ソートしたフォルダを順番に読み込む
        #ファイル名を取得
        print(folder)
        #print(os.path.basename(file))

        files = sorted(glob.glob(f"{folder}\\*.mp4"))       #フォルダ内のファイルを順番に読み込む
        max_len = 0
        for file in files:
            print(file)
                
            if len(file) > max_len:
                max_len = len(file)

        print(max_len)

        for file in files:
            #print(file)
            #print(len(file))
            if len(file) < max_len:
                print(f"{file[:(max_len - 9 + 1 )]}0{file[(max_len - 9 + 1):len(file)]}")
                newname = (f"{file[:(max_len - 9 + 1 )]}0{file[(max_len - 9 + 1):len(file)]}")
                try:
                    os.rename(file,newname)
                except:
                    pass