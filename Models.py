class Mdt:
    # Not Mapped in DB
    def __init__(self):
        self.mdtNr = 0
        self.processes = {}
    def fill(self,mdtNr,processes):
        self.mdtNr = mdtNr
        self.processes = processes

class ProcessFolder:
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
    def fillByHand(self,idNum,sourceNr,title,year,dokDat,user,status,folder,register):
        self.idNum = idNum
        self.sourceNr = sourceNr
        self.title = title
        self.year = year
        self.dokDat = dokDat
        self.user = user
        self.status = status
        self.folder = folder
        self.register = register
    def fillFromDict(self,dataDict):
        for field in dataDict:
            if field == "" or field == None:
                # only update fields with values
                continue
            self.__dict__[field] = dataDict[field]
            
    def fieldNamesVerboseDict():
        return {'sourceNr':"Vorlagen Nummer",
                'title':"Vorgangsmappen Titel",
                'year': "Veranlagungsjahr",
                'dokDat':"Dokument Datum",
                "user": "Verantwortlicher",
                "status":"Bearbeitungsstatus",
                'folder':"Ablage Ordner",
                'register':"Ablage Register",
                }
    def test(self):
        self.__dict__["user"] = "david"
    def saveToDb(self, connection):
        cursor = connection.cursor()
        fieldNamesAndDoublePointDict = {
            name:f':{name}' for name in self.__dict__.keys()}
        storageDict = {"sourceNr":str(self.sourceNr),
                    "title":self.title,
                    "year":str(self.year),
                    "dokDat" : str(self.dokDat),
                    "user":self.user,
                    "status":self.status,
                    "folder":str(self.folder),
                    "register":self.register,
                     'idNum':self.idNum}
        if self.idNum == '':
            del fieldNamesAndDoublePointDict['idNum']
##            print()
            cursor.execute(
                f"""Insert into ProcessFolder({",".join(
                                            fieldNamesAndDoublePointDict.keys())})
                VALUES({",".join(
                            fieldNamesAndDoublePointDict.values())})""",
                storageDict)
            idNum = cursor.execute('SELECT MAX(idNum) from ProcessFolder').fetchone()[0]
            self.idNum = idNum
            connection.commit()
            return idNum
        else:
            idExist = cursor.execute('SELECT * FROM ProcessFolder WHERE idNum=:idNum',{'idNum':str(self.idNum)})
            if idExist:
                
                cursor.execute(
                    f"""UPDATE ProcessFolder SET
                        {",".join([f'{name} = {doublePoint}'
                                    for name,doublePoint in
                                    fieldNamesAndDoublePointDict.items()])}
                        WHERE idNum = :idNum""",
                    storageDict)
                connection.commit()
                
    def delete(self, connection):
        cursor = connection.cursor()
        if self.idNum:
            cursor.execute("DELETE FROM ProcessFolder WHERE idNum= :idNum",{"idNum": str(self.idNum)})
        connection.commit()


class Placeholders:
    # these are the placeholders that can be added to titles in MapEdit
    def __init__(self):
        self.mdtNr = "Mdt. Nr."
        self.addInfo = "Zusätzliche Info"
    def fill(mdt, voga):
        self.mdtNr = mdt.mdtNr
        self.addInfo = mdt.addInfo





        
