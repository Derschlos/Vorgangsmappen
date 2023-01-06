import tkinter as tk
from tkinter import messagebox
import Models


class ProcessFolderEditPage(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.pageName = 'ProcessFolderEditPage'
        self.controller = controller
        self.bg = self.controller.configVars['ProcessFolderEditPageColor']
        self.placeholders = Models.Placeholders()
        self.selectedProcessFolder = Models.ProcessFolder()
        
            # Frame For Selection Combo
        self.selectionFrame = tk.Frame(self, bg=self.bg)
##        self.selectionCombo =
        
            # Frame for main Entry-Fields
        self.entryFieldsFrame = tk.Frame(self, bg=self.bg)
        self.entryFieldsNames = Models.ProcessFolder.fieldNamesVerboseDict()
        self.entryFieldsVars = {name:tk.StringVar() for name in self.entryFieldsNames}
        self.entryFields = {name:tk.Entry(self.entryFieldsFrame,
                                          textvariable = self.entryFieldsVars[name],
                                          width = 49)
                            for name in self.entryFieldsNames}
        self.entryLabels = {name:tk.Label(self.entryFieldsFrame,
                                          text =self.entryFieldsNames[name],
                                          bg = self.bg)
                            for name in self.entryFieldsNames}


            # Listbox for Placeholders
        self.placeholderLBoxChoices = self.placeholders.__dict__
        self.placeholderLBoxVar = tk.StringVar(value=self.placeholderLBoxChoices)
        self.placeholderLBox = tk.Listbox(self, listvariable = self.placeholderLBoxChoices, width = 30)
##        self.textLBox.bind('<Double-Button-1>', self.insertTextBlock)
        self.insertLBoxVals()



        self.saveBut = tk.Button(self, text = "Speichern", command =
                                 self.saveChanges)
        self.returnBut = tk.Button(self, text = "Zurück", command =
                                   lambda:self.controller.
                                   returnToPrev(self.saveChanges,
                                                self.pageName))
        self.deleteBut = tk.Button(self, text = "Vorgangsmappe löschen", command =
                                 self.delete)

            # Grid Config
        self.entryFieldsFrame.pack()
        for entry in self.entryFieldsNames:
            self.entryLabels[entry].pack()
            self.entryFields[entry].pack()
        self.placeholderLBox.pack()
        self.saveBut.pack()


    def onRaise(self):
        self.controller.root.title('This is ProcessFolderEditPage')
        self.controller.root.geometry(self.controller.configVars['ProcessFolderEditPageDimensions'])
        self.config(bg = self.controller.configVars['ProcessFolderEditPageColor'])

                                                                   
    def update(self, procId,*args):
        pass

    def insertLBoxVals(self):
        for key,val in self.placeholderLBoxChoices.items():
            self.placeholderLBox.insert('end', val)
##            self.placeholderLBox.itemconfig('end', background = key)
    def saveChanges(self):
        changes = {name:entry.get() for
                   name, entry in
                   self.entryFields.items()}
        self.selectedProcessFolder.fillFromDict(changes)
        self.selectedProcessFolder.saveToDb
        print("saved")

    def delete(self):
        pass
