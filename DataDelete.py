import os

class DATADELETE1:
    def __init__(self,delno):
        self.delno=delno
    
    def datadelete1(self):
        if self.delno==1:
            print("どのクラスデータを削除しますか？(例：1-A)")
            classdel1=input("入力:")
            print("----------------------------------------------------------------")
            print(classdel1,"のデータを削除して本当に良いですか?(YES=yを入力/NO=nを入力)")
            classdel2=input("入力:")
            if classdel2=="y":
                curdir=os.listdir(".")
                for cd1 in curdir:
                    if cd1==classdel1+".db":                    
                        os.remove(cd1)
                print(classdel1,"のクラスデータを削除しました。")
                print("----------------------------------------------------------------")
                print()
                    
            elif classdel2=="n":
                print("メニューに戻ります。")
                print("----------------------------------------------------------------")
                print()

            else:
                print("入力された文字が間違っています。")
                print("メニューに戻ります。")
                print("----------------------------------------------------------------")
                print()
            
        elif self.delno==2:
            print("すべてのクラスデータを削除します。")
            print("本当によろしいですか?(YES=yを入力/NO=nを入力)")
            classdel=input("入力:")
            if classdel=="y":
                curdir=os.listdir(".")
                for cd3 in curdir:
                    cd4=cd3.endswith(".db")
                    if cd4 is True:
                        os.remove(cd3)
                print("すべてのクラスデータを削除しました。")
                print("----------------------------------------------------------------")
                print()
                    
            elif classdel=="n":
                print("メニューに戻ります。")
                print("----------------------------------------------------------------")
                print()

            else:
                print("入力された文字が間違っています。")
                print("メニューに戻ります。")
                print("----------------------------------------------------------------")
                print()
        else:
            print("入力された文字が間違っています。")
            print("メニューに戻ります。")
            print("----------------------------------------------------------------")
            print()