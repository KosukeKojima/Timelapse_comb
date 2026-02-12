import glob
import os

from pathlib import Path

import subprocess

import done_folder_check

#受け取った配列内のパスから北のパスと南のパスを分割する
def split_NorS( path ):

    south_path = sorted(glob.glob(f"{path}//*南.mp4"))
    north_path = sorted(glob.glob(f"{path}//*北.mp4"))

    return north_path , south_path


#南のファイルを結合
def combine_south( south_paths , output_path ):

    #出力ファイル名
    output_path = output_path + "南.mp4"

    if os.path.exists( f"{os.getcwd()}//South.txt" ):
        os.remove( f"{os.getcwd()}//South.txt" )

    print(os.getcwd())
    with open(f"{os.getcwd()}//South.txt",mode="w",encoding="utf_8") as f:
            for file in south_paths:
                tofowerdslash = str(Path(file))
                tofowerdslash = tofowerdslash.replace("\\","/")
                f.writelines(f"file {tofowerdslash}\n")

    command = f' ffmpeg -f concat -safe 0 -i South.txt -c:v h264_qsv {output_path}'
    print(f"\n{command}")
    try:
        ret = subprocess.run(command, shell=True ,check=True )

    except subprocess.CalledProcessError as e:
        print(e)
        print("動画の連結に失敗しました。\n指定したパスを確認してください。")
        exit(0)
    try:
        os.remove( "South.txt" )
    except:
        pass

    
#北のファイルを結合
def combine_north( north_paths , output_path ):

    #出力ファイル名
    output_path = output_path + "北.mp4"

    if os.path.exists( f"{os.getcwd()}//North.txt" ):
        os.remove( f"{os.getcwd()}//North.txt" )

    #print(os.getcwd())
    with open(f"{os.getcwd()}//North.txt",mode="w",encoding="utf_8") as f:
            for file in north_paths:
                tofowerdslash = str(Path(file))
                tofowerdslash = tofowerdslash.replace("\\","/")
                f.writelines(f"file {tofowerdslash}\n")

    command = f' ffmpeg -f concat -safe 0 -i North.txt -c:v h264_qsv {output_path}'
    print(f"\n{command}")
    try:
        ret = subprocess.run(command, shell=True ,check=True)

    except subprocess.CalledProcessError as e:
        print(e)
        print("動画の連結に失敗しました。\n指定したパスを確認してください。")
        exit(0)
    try:
        os.remove( "North.txt" )
    except:
        pass


#combine_movies( ["パス1","パス2",...] , "year,month,dateのいづれか" , [再帰的に取得した全てのパス] )
def combine_movies( array , flag , all_path ):

    if flag == "year":

        #月のフォルダが指定された場合UserディレクトリのVideoフォルダに出力
        output_path = f"{Path.home()}\\Videos"

    elif flag == "month":

        for path in array:
        #月のフォルダが指定された場合親ディレクトリに出力
        #(パスは確認済みなので、拡張子を付け足すのみでOK)

            #record.txtの配列にパスがふくまれ、00月.mp4のフォルダが存在する場合処理を抜ける
            if path in done_folder_check.done_folder_check():
                print( "already combined !!!" )
                exit

            else:
                try:
                    north , south = split_NorS( path )
                    combine_north( north , path )
                    combine_south( south , path )
                    
                    #記録する処理を書く
                    done_folder_check.done_folder_add(path)
                
                except:
                    #print("パスが不正か、フォルダ内にファイルが存在しませんでした。")
                    pass

    elif flag == "date":

        output_path = "test"

combine_movies(['C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\2月'], "month" , {} )