
import sqlite3


def printList(txt):
    for i in txt:
        print(i)
        
def getTxtList():
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    txt = []
    for i in fileList:
        if i.split(".")[1] == "txt":
            txt.append(i)

    return txt

def dbInput():
    
    txt = getTxtList()

    conn = sqlite3.connect('drill2.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS file_tbl( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, FILE_COL TEXT)")
        conn.commit()
        
        for i in txt:
            cur.execute("INSERT INTO file_tbl(FILE_COL) VALUES(?)", (i,))
            conn.commit()
    conn.close()

    printList(txt)


if __name__ == "__main__":
    dbInput()
