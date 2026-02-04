# 2026/02/02 リネーム処理と判定を分割(判定を行う関数)

import glob
import re
import os
import rename

#リネームが必要かどうかを判定し、リネームするパスを返す関数
def check_rename( video_paths ):
    rename_paths = []
    
    for video_path in video_paths:
        #ファイル名を取得
        #print(video_paths)
        filename = os.path.splitext(os.path.basename(video_path))[0]
        print(filename)

        #数字部分を抽出してリスト化
        numbers = re.findall(r'\d+', filename)
        print(numbers)

        #数字部分の長さを確認
        need_rename = False
        for number in numbers:
            if len(number) < 2:
                need_rename = True
                break
        
        if need_rename:
            rename_paths.append(video_path)
    
    #print(len(rename_paths))

    return rename_paths

#どの階層のフォルダが指定されているかを判定する関数
def check_files( video_dir ):
    print("ファイルチェック処理開始")
    print(f"video_dir : {video_dir}")
    
    #指定されたディレクトリを判定する
    #年のフォルダの場合
    year_folders = sorted(glob.glob(f"{video_dir}\\????年"))
    print(year_folders)

    #月のフォルダの場合
    month_folders = sorted(glob.glob(f"{video_dir}\\[0-9]*月"))
    print(month_folders)

    #日付のフォルダの場合(1月1日でも01月01日でも対応)
    date_folders = sorted(glob.glob(f"{video_dir}\\*月*日[南北].mp4"))
    print(date_folders)

    all_folders = sorted(glob.glob(f"{video_dir}\\*月*日[南北].mp4"))
    print(all_folders)


    if len(year_folders) > 0:
        
        print("年のフォルダが指定されました")
        
        all_folders = sorted(glob.glob(f"{video_dir}\\*月*日[南北].mp4",recursive=True))
        #print(all_folders)
        
        return "year"
    
    elif len(month_folders) > 0:
        
        print("月のフォルダが指定されました")
        
        all_folders = sorted(glob.glob(f"{video_dir}\\*月*日[南北].mp4",recursive=True))
        #print(all_folders)
        
        return ["month",all_folders]
    
    
    elif len(date_folders) > 0:
        print("動画ファイルが指定されました")
        return ["date",date_folders]
    
    else:
        print("指定されたフォルダが不正、または動画はありませんでした。")
        return ["error",None]

#テストデータ
check_files("C:\\Users\\TSU8033\\Videos\\original")
check_files("C:\\Users\\TSU8033\\Videos\\original\\2025年")
check_files("C:\\Users\\TSU8033\\Videos\\original\\2025年\\10月")


#files = check_files("C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月")
#paths = check_rename(files[1])

#rename.rename( paths )

#files = check_files("C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月 - コピー")
#paths = check_rename(files[1])

#rename.rename( paths )