import os
import datetime


def getFileNames():
    dirPath = "C:\\pythonDrill"
    files = os.listdir(dirPath)

    findTxt(files,dirPath)


def findTxt(files=[],dirPath=""):
    lst = []
    for file in files:
        if file.split(".")[1] == "txt":
            lst.append(file)

    mkFilePath(lst,dirPath)   
    


def mkFilePath(files,dirPath):
    filePaths = []
    for file in files:
        filePaths.append(os.path.join(dirPath,file))
        
    printFiles(filePaths,files)  

def printFiles(filePaths,files):
    i = 0 
    for file in files:         #convert from epoch time to datetime stamp becuse epoch is hard to read
        print(file + ": " + datetime.datetime.fromtimestamp(os.path.getmtime(filePaths[i])).strftime('%c'))
                               #copy paste from stackoverflow hope thats ok
        i = i + 1
            




if __name__ == "__main__":
    getFileNames()
    
