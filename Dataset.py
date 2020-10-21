import numpy as np
from PIL import Image 
import os 
import cv2 
import matplotlib.pyplot as plt 

def D():
    # 画像保存用リスト
    fileName = []
    # 画像ファイルの名前
    cnt = 0
    # 画像ファイル保存用の名前
    i = 0
    
    # 画像のディレクトリを指定
    print("保存されている画像のディレクトリ(相対パス):",end="")
    orgDir = input()

    # 画像保存用ディレクトリの指定
    print("画像を保存するディレクトリ(相対パス):",end="")
    saveDir = input()

    # 画像を保存する名前(例：2020-10-21) 後で+".jpg"するので名前だけ
    print("画像を保存する名前(例: D1,D2,D3,D4,...,Dn)",end="")
    saveName = input()

    while True:
        # 画像を読み込み
        try:
            img = Image.open(orgDir+str(cnt)+".jpg")
            fileName = os.listdir(orgDir)
        except FileNotFoundError:
            pass

        # 画像を表示
        plt.imshow(img)
        plt.show()

        # yes no で指定して画像を保存するかどうかを決める
        print("この画像は保存するかしないか")
        print("yes or no (xで終了):",end="")
        isYes = input()

        # 画像を保存
        if isYes == "yes":
            img.save(saveDir+saveName+"-"+fileName[i]+".jpg")
            print("保存しました。")
            i += 1
        else:
            pass 
        # カウントアップ
        cnt += 1


        if isYes == "x":
            break



if __name__ == "__main__":
    D()