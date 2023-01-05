class Mdt:
    # Not Mapped in DB
    def __init__(self):
        self.mdtNr = 0
        self.vorgaMaps = []
        self.addInfo = ""
    def fill(self,mdtNr,vorgaMaps, addInfo):
        self.mdtNr = mdtNr
        self.vorgaMap = vorgaMaps
        self.addInfo = addInfo
##    def saveToDb(self, connection):
##        cursor = connection.cursor()
##        if self.idNum == '':
##             cursor.execute(
##                "Insert into table1(idNum,title) VALUES (:idNum,:title)",
##                {'idNum':str(self.idNum),
##                 'title':self.title
##                    })
##            idNum = cursor.execute('SELECT MAX(id) from Kontakte').fetchone()[0]
##            self.idNum = idNum
##            connection.commit()
##            return idNum
##         else:
##            idExist = cursor.execute('SELECT * FROM table1 WHERE idNum=:idNum',{'idNum':str(self.idNum)})
##            if idExist:
##                cursor.execute(
##                    "UPDATE table1 SET title = :title WHERE idNum = :idNum",
##                    {'title':self.title,
##                     'idNum':str(self.idNum)
##                        })
##                connection.commit()
##    def delete(self, connection):
##        cursor = connection.cursor()
##        if self.idNum:
##            cursor.execute("DELETE FROM table1 WHERE idNum= :idNum",{"idNum": str(self.idNum)})
##        connection.commit()

class VorgaMappe:
    def __init__(self):
        self.idNum = ''
        self.sourceNr = 0
        self.title = ""
        self.year = 2023
        self.dokDat = "01.01.2022"
        self.user = "kreller"
        self.status = "erledigt"
        self.folder = "03"
        self.register = ""
    def fill(self,idNum,sourceNr,title,year,dokDat,user,status,folder,register):
        self.idNum = idNum
        self.sourceNr = sourceNr
        self.title = title
        self.year = year
        self.dokDat = dokDat
        self.user = user
        self.status = status
        self.folder = folder
        self.register = register
##    def saveToDb(self, connection):
##        cursor = connection.cursor()
##        if self.idNum == '':
##             cursor.execute(
##                """Insert into VorgaMap(
##                    sourceNr,
##                    title,
##                    year,
##                    "dokDat",
##                    user,
##                    status,
##                    folder,
##                    register)
##                VALUES(
##                    :sourceNr,
##                    :title,
##                    :year,
##                    :dokDat,
##                    :user,
##                    :status,
##                    :folder,
##                    :register)""",
##                {"sourceNr":str(self.sourceNr),
##                    "title":self.title,
##                    "year":str(self.year),
##                    "dokDat" : str(self.dokDat),
##                    "user":self.user,
##                    "status":self.status,
##                    "folder":str(self.folder),
##                    "register":self.register
##                    })
##            idNum = cursor.execute('SELECT MAX(id) from VorgaMap').fetchone()[0]
##            self.idNum = idNum
##            connection.commit()
##            return idNum
##         else:
##            idExist = cursor.execute('SELECT * FROM VorgaMap WHERE idNum=:idNum',{'idNum':str(self.idNum)})
##            if idExist:
##                cursor.execute(
##                    """UPDATE VorgaMap SET
##                        sourceNr = :sourceNr,
##                        title = :title,
##                        year = :year,
##                        dokDat = :dokDat,
##                        user = :user,
##                        status = :status,
##                        folder = :folder,
##                        register = :register
##                        WHERE idNum = :idNum""",
##                    {
##                    "sourceNr":str(self.sourceNr),
##                    "title":self.title,
##                    "year":str(self.year),
##                    "dokDat" : str(self.dokDat),
##                    "user":self.user,
##                    "status":self.status,
##                    "folder":str(self.folder),
##                    "register":self.register
##                     'idNum':str(self.idNum)
##                        })
##                connection.commit()
##    def delete(self, connection):
##        cursor = connection.cursor()
##        if self.idNum:
##            cursor.execute("DELETE FROM VorgaMap WHERE idNum= :idNum",{"idNum": str(self.idNum)})
##        connection.commit()


class Placeholders:
    def __init__(self):
        self.mdtNr = "Mdt. Nr."
        self.addInfo = "Additional Info"
    def fill(mdt, voga):
        self.mdtNr = mdt.mdtNr
        self.addInfo = mdt.addInfo





        
