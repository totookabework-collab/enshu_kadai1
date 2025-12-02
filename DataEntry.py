import sqlite3
import os

class DATAENTRY1:
    def __init__(self,classroom):
        self.classroom=classroom
    
    #学級データが存在しているとき
    def existstrue(self):
        if os.path.exists(self.classroom):
            print("データが存在しています。")
            print("以下のどの操作を行いますか？(数字を入力)")
            print("1.データの追加 / 2.データの変更 / 3.メニューへ戻る(1~3を入力)")
            num1=int(input("入力:"))
            print("----------------------------------------------------------------")
            cr1=self.classroom
            conn=sqlite3.connect(cr1)
            c=conn.cursor()
            #1.データの追加
            if num1==1:
                print("一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product ORDER BY No")
                for row in itr:
                    print(row) 
                print("----------------------------------------------------------------")
                print()
                print("何人のデータを追加しますか?(数字を入力)")  
                num12=int(input("入力:"))
                print()
                print("----------------------------------------------------------------")
                for i in range(1,num12+1):
                    try:
                        print("追加する生徒のNoを入力してください。")
                        number1=int(input("No:"))
                        class_no=c.execute("SELECT * FROM product")
                        for j in class_no:                                           
                            if number1==j[0]:
                                print("そのNoは存在します。")
                                print("メニューに戻ります。")
                                print("----------------------------------------------------------------")                         
                                    
                            else:
                                print("追加する",i,"人目の名前を入力してください。")
                                name1=input("名前:")
                                print("追加する",i,"人目の点数を入力してください。")
                                score1=(input("点数:"))
                                c.execute("INSERT INTO product VALUES(?,?,?)",(number1,name1,score1))
                            
                    except ValueError:
                        print("入力した文字が間違っています。処理を飛ばします。")
                        print("----------------------------------------------------------------")
                        print()
                        continue
                
                print("----------------------------------------------------------------")
                print("一覧表を表示します。")
                print("(No,名前,点数)")
                
                itr=c.execute("SELECT * FROM product ORDER BY No")
                for row in itr:
                    print(row)  
                print("----------------------------------------------------------------")
                print()
                     
            #2.データの変更    
            elif num1==2:
                print("一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product")
                for row in itr:
                    print(row) 
                print("----------------------------------------------------------------")
                print()  
                
                print("変更する生徒のNoを入力してください。")
                number2=int(input("No:"))
                print("変更する生徒の名前を入力してください。")
                name2=input("名前:")
                print("変更する生徒の点数を入力してください。")
                score2=(input("点数:"))
                c.execute("UPDATE product SET name=?,score=? where No=?",(name2,score2,number2))
                print("----------------------------------------------------------------")
                
                print("変更された一覧表を表示します。")
                print("(No,名前,点数)")
                itr=c.execute("SELECT * FROM product ORDER BY No")
                for row in itr:
                    print(row) 
                print("----------------------------------------------------------------")
                print()
                          
            #3.メニューへ戻る
            elif num1==3:
                print("メニューに戻ります。")
                print("----------------------------------------------------------------")
                print()
                    
            else:
                print("入力した数字が間違っています。")
                print("メニューに戻ります。")
                print("----------------------------------------------------------------")
                print()
            
            conn.commit()
            conn.close()
            
            
    #学級データが存在していないとき
    def existsfalse(self):
        if os.path.exists(self.classroom)==False:
            print("データが存在しません。新しいデータを作成します。")
            cr2=self.classroom
            conn=sqlite3.connect(cr2)
            c=conn.cursor()
            c.execute("CREATE TABLE product(No INT,name CHAR(20),score CHAR(20))")
            
            print("何人のデータを追加しますか？(数字を入力)")        
            num2=int(input("入力:"))
            print("----------------------------------------------------------------")
            for i in range(1,num2+1):
                try:
                    number=i
                    print(i,"人目の名前を入力してください。")
                    name=input("名前:")
                    print(i,"人目の点数を入力してください。")
                    score=(input("点数:"))
                    c.execute("INSERT INTO product VALUES(?,?,?)",(number,name,score))
                except ValueError:
                    print("入力した文字が間違っています。処理を飛ばします。")
                    print()
                    continue
                          
            conn.commit()
           
            print("----------------------------------------------------------------")
            print("一覧表を表示します。")
            print("(No,名前,点数)")
            itr=c.execute("SELECT * FROM product ORDER BY No")
            for row in itr:
                print(row)
            print("----------------------------------------------------------------")
            print()
            
            conn.close()