import os
import glob
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import threading
import glob
from pathlib import Path

import done_folder_check
import rename
import files_check
import subprocess

flag = False

def hevyprocess(dirPath,flag):

    #月のフォルダのパスを指定すると、その中の日付フォルダを連結する処理
    
    #「実行ボタン」を非表示にする
    button1.pack_forget()

    #連結した映像の出力先,隠しファイルで連結済みの月を記録する

    #出力先のVideosフォルダを指定
    home = Path.home()
    output_dir = f"{home}\\Videos"

    #record.txtが無ければ作成
    if not os.path.exists(f"{output_dir}\\record.txt"):
        with open(f"{output_dir}\\record.txt",mode="w",encoding="utf_8") as f:
            #隠しファイルに設定
            os.system(f'attrib +h {output_dir}\\record.txt')
        
        done_folders = []

    #record.txtがあれば、連結済みの月を確認する
    else:
        done_folders = done_folder_check.done_folder_check()
    

    #指定されたディレクトリを判定する

    for folder in folders:
        year = os.path.basename(os.path.dirname(folder))
        month = os.path.basename(folder)

        #print(f"year {year} , month {month}")
        
        if flag == True:
            window_close()

        #南の映像を連結
        files = sorted(glob.glob(f"{folder}//*南.mp4"))
        out_path = Path(f"{video_dir}//{year}{month}南.mp4")
        print(out_path)
        print(files)
        
        print(f"{os.getcwd()}//.North.txt")

        with open(f"{os.getcwd()}//.North.txt",mode="w",encoding="utf_8") as f:
            for file in files:
                tofowerdslash = str(Path(file))
                tofowerdslash = tofowerdslash.replace("\\","/")
                f.writelines(f"file {tofowerdslash}\n")

        command = f' ffmpeg -f concat -safe 0 -i .North.txt -c:v h264_qsv {out_path}'
        print(f"\n{command}")
        subprocess.call(command, shell=True)

        #movie_combine.comb_movie(files,out_path)

        #北の映像を連結
        files = sorted(glob.glob(f"{folder}//*北.mp4"))        
        out_path = f"{video_dir}//{year}{month}北.mp4"
        #movie_combine.comb_movie(files,out_path)

        print(out_path)
        
        print(f"{os.getcwd()}//.South.txt")

        with open(f"{os.getcwd()}//.South.txt",mode="w",encoding="utf_8") as f:
            for file in files:
                tofowerdslash = str(Path(file))
                tofowerdslash = tofowerdslash.replace("\\","/")
                f.writelines(f"file {tofowerdslash}\n")

        command = f' ffmpeg -f concat -safe 0 -i South.txt -c:v h264_qsv {out_path}'
        print(f"\n{command}")
        subprocess.call(command, shell=True)

    try:
        os.remove( ".South.txt" )
    except:
        pass

    try:
        os.remove( ".North.txt" )
    except:
        pass

    button1.pack()
    
    messagebox.showinfo('連結完了', '処理が終了しました')
    exit()

# フォルダ指定の関数
def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""
    
    dirPath = entry1.get()
    if dirPath:
        text += "フォルダパス：" + dirPath + "\n"

    if text:
        messagebox.showinfo("処理が終わるまで止められません", text)
        #print(text)

        #フォルダの階層を判定
        flag_check = files_check.check_files(dirPath)
        #flagcheckの内容に応じて処理を分岐させる
        print(flag_check)
        if flag_check[0] == "error":
            messagebox.showerror("error", "指定されたフォルダが不正、または動画はありませんでした。")
            return -1
        #その他返り値の場合、2番目の要素を変数に格納
        all_folders = flag_check[2]
        print(all_folders)
        #all_foldersには動画ファイルのパスが格納されている
        
        rename_paths = files_check.check_rename(all_folders)
        print(rename_paths)

        #リネームが必要なフォルダがある場合、リネーム処理を実行
        for video_dir in rename_paths:
            rename.rename(video_dir)
            print("リネーム処理が完了しました")

        if flag_check[0] == "year":
            #年のフォルダが指定された場合、年のフォルダがいくつかあるかを確認
            year_folders = sorted(glob.glob(f"{dirPath}\\????年"))
            print(year_folders)
            if len(year_folders) > 1:
                #年のフォルダが複数ある場合、年のフォルダごとに処理を分ける
                for year_folder in year_folders:
                    folders = sorted(glob.glob(f"{year_folder}\\*月*日[南北].mp4"))
                    #UIをフリーズさせない為に別スレッドで実行
                    thread = threading.Thread(target=hevyprocess,args=(folders,flag))
                    thread.start()

                    #スレッドを起動したら、record.txtに連結済みの月を追記する
                    month_name = os.path.basename(year_folder)
                    done_folder_check.done_folder_add(month_name)
            else:
                #年のフォルダが1つだけの場合、そのまま処理を進める
                folders = sorted(glob.glob(f"{dirPath}\\*月*日[南北].mp4"))
                #UIをフリーズさせない為に別スレッドで実行
                thread = threading.Thread(target=hevyprocess,args=(all_folders,flag))
                thread.start()
                return
            
        elif flag_check[0] == "month":
            #月のフォルダが指定された場合、そのまま処理を進める
            folders = sorted(glob.glob(f"{dirPath}\\*月*日[南北].mp4"))
        else:
            folders = all_folders

        #UIをフリーズさせない為に別スレッドで実行
        thread = threading.Thread(target=hevyprocess,args=(all_folders,flag))
        thread.start()
    
    else:
        messagebox.showerror("error", "パスの指定がありません。")

def window_close():
    global flag
    try:
        flag = True
        root.destroy()
    except:
        root.destroy()

if __name__ == "__main__":

    # rootの作成
    root = Tk()
    root.title("サンプル")

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame1, text="動画フォルダを指定(例:2025年)", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame1, text="参照", command=dirdialog_clicked)
    IDirButton.pack(side=LEFT)

    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=5,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    """
    # キャンセルボタンの設置
    button2 = ttk.Button(frame3, text=("ウィンドウを閉じる"), command=window_close)
    button2.pack(fill = "x", padx=30, side = "left")
    """
    
    root.mainloop()
