import os
import sqlite3
import statistics
import matplotlib.pyplot as plt

class DATAGRAPH1:
    def __init__(self,sy0):
        self.sy0=sy0
        
    def datagraph1(self):
        try:
            #空リスト
            dbfile=[]
            schoolyearfile=[]
            classname=[]
            scorefile=[]
            comparisonfile=[]
            
            #フォルダの.db選別
            dg1=os.listdir(".")
            for db1 in dg1:
                db2=db1.endswith(".db")
                if db2 is True:
                    dbfile.append(db1)
                
            #学年ごとの.db選別
            for db3 in dbfile:
                db4=db3.startswith(self.sy0)
                if db4 is True:
                    schoolyearfile.append(db3)
            
            #学年のデータが存在するときグラフ作成
            if schoolyearfile[0].startswith(self.sy0)==True:
                for i in schoolyearfile:
                    conn=sqlite3.connect(i)
                    c=conn.cursor()
                    itr=c.execute("SELECT * FROM product")
                    for score1 in itr:
                        try:
                            scorefile.append(int(score1[2]))
                        
                        except ValueError:
                            continue
                            
                    average1=round(statistics.mean(scorefile),1)
                    comparisonfile.append(average1)
                                
                    del scorefile[:]

                print("----------------------------------------------------------------")
                #平均点の一覧表を表示
                for data1 in zip(schoolyearfile,comparisonfile):
                    d1=str(data1[0])
                    d2=d1.replace(".db","")
                    classname.append(d2)
                    print(d2,"の平均点は",data1[1],"です。")
                print("----------------------------------------------------------------")
                #グラフを作成
                plt.rcParams["font.family"]="MS GOTHIC"
                plt.bar(classname,comparisonfile)
                plt.xlabel("クラス")
                plt.ylabel("平均点")
                plt.title("各クラス平均点比較")
                for index_y,values_y in enumerate(comparisonfile):
                    plt.text(index_y,values_y,str(values_y),ha="center",va="bottom")
                plt.ylim(0,100)
                plt.show()

                conn.commit()
                conn.close()
        
        except IndexError:
            print("入力した学年のデータがありません。")
            print("メニューに戻ります。")
            print("----------------------------------------------------------------")
            print()