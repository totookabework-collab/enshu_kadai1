import sqlite3
import os

class DATACONFIRMATION1:
    def __init__(self,classroom):
        self.classroom=classroom
    

    def dataconfirmaition1(self):
        if os.path.exists(self.classroom):
            conn=sqlite3.connect(self.classroom)
            c=conn.cursor()
            print("一覧表を表示します。")
            print("(No,名前,点数)")
            itr=c.execute("SELECT * FROM product ORDER BY No")
            for row in itr:
                print(row)
            print("----------------------------------------------------------------")
            print()
            conn.commit()
            conn.close()
                
        else:
            print(self.classroom,"のデータはありません。")
            print("----------------------------------------------------------------")
            print()
            