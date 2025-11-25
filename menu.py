import DataEntry
import sqlite3
import os

while True:
    print("成績表:どの操作を行いますか？")
    print("数字を入力してください。(1~4)")
    print("1.データ確認 / 2.データ入力 / 3.データ削除 / 4.終了")
    menu=int(input())

    #1.データ確認
    if menu==1:
        print("表示したいクラス名を入力してください。(例：1-A)")
        classroom1=input("")
        classroom1=classroom1+".db"
        if os.path.exists(classroom1):
            conn=sqlite3.connect(classroom1)
            c=conn.cursor()
            print("一覧表を表示します。")
            print("(No,名前,点数)")
            itr=c.execute("SELECT * FROM product")
            for row in itr:
                print(row)
            print()
            conn.commit()
            conn.close()
            
        else:
            print(classroom1,"のデータはありません。")
            print()
    #2.データ入力
    elif menu==2:
        print("クラス名を選択してください。(例：1-A)")
        classroom2=input()
        classroom2=classroom2+".db"
        de1=DataEntry.DATAENTRY1(classroom2)
        de1.existstrue()
        de1.existsfalse()
        print()
    
    #3.データ削除    
    elif menu==3:
        print("削除方法を選択してください。(1~2)")
        print("1.選択削除 / 2.全クラスデータ削除")
        delno=int(input())
        if delno==1:
            print("どのクラスデータを削除しますか？(例：1-A)")
            classdel1=input("")
            print(classdel1,"のデータを削除して本当に良いですか?(YES=yを入力/NO=nを入力)")
            classdel2=input()
            if classdel2=="y":
                curdir=os.listdir(".")
                for cd1 in curdir:
                    if cd1==classdel1+".db":                    
                        os.remove(cd1)
                print(classdel1,"のクラスデータを削除しました。")
                print()
            elif classdel2=="n":
                print("メニューに戻ります。")
                print()

            else:
                print("入力された文字が間違っています。")
                print("メニューに戻ります。")
                print()
        
        elif delno==2:
            print("すべてのクラスデータを削除します。")
            print("本当によろしいですか?(YES=yを入力/NO=nを入力)")
            classdel=input()
            if classdel=="y":
                curdir=os.listdir(".")
                for cd1 in curdir:
                    cd2=cd1.endswith(".db")
                    if cd2 is True:
                        os.remove(cd1)
                print("すべてのクラスデータを削除しました。")
                print()
            elif classdel=="n":
                print("メニューに戻ります。")
                print()

            else:
                print("入力された文字が間違っています。")
                print("メニューに戻ります。")
                print()
        else:
            print("入力された文字が間違っています。")
            print("メニューに戻ります。")
            print()

    #4.終了
    elif menu==4:
        print("プログラムを終了します。")
        break
    
    else:
        print("入力した数字が間違っています。")
        print()