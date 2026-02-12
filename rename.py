import os
import re

# 2026/02/02 リネーム処理と判定を分割(リネーム処理を行う関数)

#リネーム処理を行う関数(パスのリストを受け取ってリネームを実行)
def rename( files ):

    #拡張子を除いたファイル名がXX月XX日南 となるように X月X日南 -> 0X月0X日南 にリネームする
    #XX月X日南 でも X月XX日南 でも対応するようにする
    
    #例:1月1日南.mp4 -> 01月01日南.mp4
    #例:1月10日南.mp4 -> 01月10日南.mp4
    #例:10月1日南.mp4 -> 10月01日南.mp4となるようにリネームする

    for file in files:

        try:
            dirname = os.path.dirname(file)
        except IndexError:
            print("No files to rename.")
            return

        filename , extension = os.path.splitext(os.path.basename(file))
        
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


            try:
                #リネーム実行
                os.rename(file, new_filepath)
                #print(f"Renamed to: {new_filename}")

            #リネーム処理に失敗した場合
            except:
                #既に「00月00日」という形式のファイルがあれば、「0月00日」、「00月0日」という形式のファイルを削除する。
                if os.path.exists(new_filepath):
                    try:
                        print(f"{file} を削除します")
                        os.remove(file)

                    except:
                        print("「0月00日」、「00月0日」という形式のファイルは削除済みです。")
                        pass
                
                #エラーの場合の処理
                else:
                    print(new_filepath)
                    print("リネーム処理に失敗したか、存在しないファイルをリネームしようとしました。")
                    return -1
                
        else:
            pass
            #print(f"Skipping file (not enough number parts): {filename}{extension}")


#test data
#rename(['C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月01日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月01日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月02日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月02日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月03日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月03日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月04日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月04日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月05日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月05日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月06日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月06日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月07日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月07日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月08日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月08日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月09日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月09日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月10日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月10日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月11日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月11日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月12日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月12日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月13日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月13日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月14日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月14日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月15日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月15日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月16日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月16日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月17日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月17日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月18日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月18日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月19日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月19日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月1日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月1日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月20日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月20日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月21日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月21日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月22日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月22日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月23日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月23日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月24日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月24日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月25日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月25日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月26日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月26日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月27日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月27日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月28日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月28日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月29日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月29日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月2日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月2日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月30日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月30日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月31日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月31日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月3日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月3日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月4日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月4日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月5日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月5日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月6日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月6日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月7日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月7日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月8日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月8日南.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月9日北.mp4', 'C:\\Users\\TSU8033\\Videos\\original\\2026年\\1月\\1月9日南.mp4'])