#11/26の宮田講師報告時から追加した機能
#例外処理:入力文字が間違っているとメッセージを出しメニューへ
#データ追加時に順番が変わってしまう可能性を考え、ソート機能を各所に追加

#データの追加時、既存のNoと重複している場合、メッセージを出し入力できないようにする
#メッセージの修正
#ループ中に間違った文字を入力すると、その処理を飛ばし、継続して入力可能にした
#「データ確認」と「データ削除」を別ファイルに分割(データ入力は元々分割していた)
#「平均点グラフ作成」の欄を追加

import DataEntry
import DataConfirmation
import DataDelete
import DataGraph

while True:
    try:
        #ビュー?
        print("成績表:どの操作を行いますか？")
        print("数字を入力してください。(1~4)")
        print("1.データ確認 / 2.データ入力 / 3.データ削除 / 4.平均点グラフ(test) / 5.終了")
        menu=int(input("入力："))
        print("----------------------------------------------------------------")

        #コントローラー?
        #1.データ確認
        if menu==1:
            print("表示したいクラス名を入力してください。(例：1-A)")
            classroom1=input("入力:")
            print("----------------------------------------------------------------")
            classroom1=classroom1+".db"
            dc1=DataConfirmation.DATACONFIRMATION1(classroom1)
            dc1.dataconfirmaition1()
            print()
                
        #2.データ入力
        elif menu==2:
            print("クラス名を選択してください。(例：1-A)")
            classroom2=input("入力:")
            print("----------------------------------------------------------------")
            classroom2=classroom2+".db"
            de1=DataEntry.DATAENTRY1(classroom2)
            de1.existstrue()
            de1.existsfalse()
            print()
        
        #3.データ削除    
        elif menu==3:
            print("削除方法を選択してください。(数字を入力)")
            print("1.選択削除 / 2.全クラスデータ削除 (1~2を入力)")
            delno=int(input("入力:"))
            print("----------------------------------------------------------------")
            dd1=DataDelete.DATADELETE1(delno)
            dd1.datadelete1()
            print()
            
        #4.平均点グラフの作成
        elif menu==4:
            print("表示したい学年を入力してください。(数字を入力)")
            sy0=input("入力:")
            dg0=DataGraph.DATAGRAPH1(sy0)
            dg0.datagraph1()
            print()
            
        #5.終了
        elif menu==5:
            print("プログラムを終了します。")
            break
        
        else:
            print("入力した数字が間違っています。")
            print("----------------------------------------------------------------")
            print()
    
    except ValueError:
        print("入力した文字が間違っています。")
        print("メニュー画面に戻ります。")
        print("----------------------------------------------------------------")
        print()
        print()