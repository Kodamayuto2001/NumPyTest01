import numpy as np
from PIL import Image 
import os 
import cv2 
import matplotlib.pyplot as plt 

def D(orgDir,saveDir,saveName):
    # 画像保存用リスト
    fileName = []
    # 画像ファイルの名前
    cnt = 0
    
    # # 画像のディレクトリを指定
    # print("保存されている画像のディレクトリ(相対パス):",end="")
    # orgDir = input()

    # # 画像保存用ディレクトリの指定
    # print("画像を保存するディレクトリ(相対パス):",end="")
    # saveDir = input()

    # 画像を保存する名前(例：2020-10-21) 後で+".jpg"するので名前だけ
    # print("画像を保存する名前(例: D1,D2,D3,D4,...,Dn)",end="")
    # saveName = input()

    while True:
        # 画像を読み込み
        try:
            img = Image.open(orgDir+str(cnt)+".jpg")
            fileName = os.listdir(orgDir)
        except FileNotFoundError:
            break


        # 画像を保存
        img.save(saveDir+saveName+"-"+fileName[cnt]+".jpg")
        print(saveDir+saveName+"-"+fileName[cnt]+".jpg")

        # カウントアップ
        cnt += 1


def ReName(orgDir,saveDir):
    # print(os.listdir(orgDir))
    # print(os.listdir(orgDir)[0])
    # print(os.listdir(orgDir)[1])
    # print(os.listdir(orgDir)[2])

    with open("log") as f:
        cnt = int(f.read())

    while True:
        # 画像を読み込み
        try:
            img = Image.open(orgDir+os.listdir(orgDir)[cnt])
        except IndexError:
            with open("log",mode="w") as f:
                f.write(str(cnt)+"\n")
                print("画像保存合計枚数："+str(cnt))
            break 

        # 画像を保存
        img.save(saveDir+str(cnt)+".jpg")

        # カウントアップ
        cnt += 1

if __name__ == "__main__":
    Dir = "Resources4"
    sDir = "CustomizedData4"
    name = "suetomo2"
    Sname = "suetomo"
    SaveName = "D4-3"

    # D(orgDir="../総合制作14/"+Dir+"/train/"+name+"/",saveDir=sDir+"/train/"+Sname+"/",saveName=SaveName)

    ReName(orgDir="CustomizedData2/train/ando/",saveDir="Dataset/train/ando/")
    
