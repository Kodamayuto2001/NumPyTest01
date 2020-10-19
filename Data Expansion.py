import numpy as np 
from PIL import Image 
import os 

class DataExpansion:
    def __init__(self,orgDir,saveDir):
        self.fileName(orgDir)
        self.Rotate(orgDir,saveDir)
    def fileName(self,orgDir):
        self.data = os.listdir(orgDir)
        for p in self.data:
            self.filename = os.path.splitext(os.path.basename(orgDir+p))[0]
            # print(self.filename)    
    def Rotate(self,orgDir,saveDir):
        for i in enumerate(self.data):
            img = np.array(Image.open(orgDir+self.data[i]))
            Image.fromarray(np.rot90(img)).save(saveDir+self.filename+"-r90.jpg")
            Image.fromarray(np.rot90(img,2)).save(saveDir+self.filename+"-r180.jpg")
            Image.fromarray(np.rot90(img,3)).save(saveDir+self.filename+"-r270.jpg")
        

DataExpansion("NumPyImg/","NumPyImg/")