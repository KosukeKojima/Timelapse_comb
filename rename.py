import os
import re

# 2026/02/02 リネーム処理と判定を分割(リネーム処理を行う関数)

#リネーム処理を行う関数(パスのリストを受け取ってリネームを実行)
def rename( files ):
    
    try:
        dirname = os.path.dirname(files[0])
    except IndexError:
        print("No files to rename.")
        return

    #拡張子を除いたファイル名がXX月XX日南 となるように X月X日南 -> 0X月0X日南 にリネームする
    #XX月X日南 でも X月XX日南 でも対応するようにする
    
    #例:1月1日南.mp4 -> 01月01日南.mp4
    #例:1月10日南.mp4 -> 01月10日南.mp4
    #例:10月1日南.mp4 -> 10月01日南.mp4となるようにリネームする

    for file in files:

        filename = os.path.splitext(os.path.basename(file))[0]
        extension = os.path.splitext(os.path.basename(file))[1]

        #数字部分を抽出してリスト化
        numbers = []
        matches = re.findall(r'\d+', filename)
        for match in matches:
            numbers.append(match)

        print(f"Before rename: {filename}{extension}")

        #リネーム後のファイル名を作成
        if len(numbers) >= 2:
            month = numbers[0].zfill(2)
            day = numbers[1].zfill(2)
            suffix = filename[-1]  # '南' or '北'
            new_filename = f"{month}月{day}日{suffix}{extension}"
            new_filepath = os.path.join(dirname, new_filename)

            #リネーム実行
            os.rename(file, new_filepath)
            #print(f"Renamed to: {new_filename}")
        else:
            pass
            #print(f"Skipping file (not enough number parts): {filename}{extension}")