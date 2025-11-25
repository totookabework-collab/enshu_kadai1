import sqlite3
import os

class DATAENTRY1:
    def __init__(self,classroom):
        self.classroom=classroom
    
    #学級データが存在しているとき
    def existstrue(self):
        if os.path.exists(self.classroom):
            print("データが存在しています。")
            print("以下の操作を行いますか？")
            print("1.データの追加 / 2.データの変更 / 3.メニューへ戻る(1~3)")
            num1=int(input())
            cr1=self.classroom
            conn=sqlite3.connect(cr1)
            c=conn.cursor()
            #1.データの追加
            if num1==1:
                print("一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product")
                for row in itr:
                    print(row) 
                print()  
                num12=int(input("何人のデータを追加しますか？(数字を入力)"))
                for i in range(1,num12+1):
                    print("追加する生徒のNoを入力してください。")
                    number1=int(input(""))
                    print("追加する",i,"人目の名前を入力してください。")
                    name1=input("")
                    print("追加する",i,"人目の点数を入力してください。")
                    score1=int(input(""))
                    c.execute("INSERT INTO product VALUES(?,?,?)",(number1,name1,score1))
                
                print("一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product")
                for row in itr:
                    print(row)   
            #2.データの変更    
            elif num1==2:
                print("一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product")
                for row in itr:
                    print(row) 
                print()  
                print("変更する生徒のNoを入力してください。")
                number2=int(input(""))
                print("変更する生徒の名前を入力してください。")
                name2=input("")
                print("変更する生徒の点数を入力してください。")
                score2=int(input(""))
                c.execute("UPDATE product SET name=?,score=? where No=?",(name2,score2,number2))
                print("変更された一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product")
                for row in itr:
                    print(row) 
                          
            #3.メニューへ戻る
            elif num1==3:
                print("メニューに戻ります。")    
            else:
                print("入力した数字が間違っています。")
                print("メニューに戻ります。")
            
            conn.commit()
            conn.close()
            
            
    #学級データが存在していないとき
    def existsfalse(self):
        if os.path.exists(self.classroom)==False:
            print("データが存在しません。新しいデータを作成します。")
            cr2=self.classroom
            conn=sqlite3.connect(cr2)
            c=conn.cursor()
            c.execute("CREATE TABLE product(No CHAR(20),name CHAR(20),score INT)")
                    
            num2=int(input("何人のデータを追加しますか？(数字を入力)"))
            for i in range(1,num2+1):
                number=i
                print(i,"人目の名前を入力してください。")
                name=input("")
                print(i,"人目の点数を入力してください。")
                score=int(input(""))
                c.execute("INSERT INTO product VALUES(?,?,?)",(number,name,score))
            
            conn.commit()
           
            print("一覧表を表示します。")
            print("(No,名前,点数)")
            itr=c.execute("SELECT * FROM product")
            for row in itr:
                print(row)
            
            conn.close()