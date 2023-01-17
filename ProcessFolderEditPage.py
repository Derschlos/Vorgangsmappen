import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Models
import sqlite3 as sql
from contextlib import closing

class ProcessFolderEditPage(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.pageName = 'ProcessFolderEditPage'
        self.controller = controller
        self.bg = self.controller.configVars['ProcessFolderEditPageColor']
        self.selectedProcessFolder = Models.ProcessFolder()
        self.pFolderTitleToId = {}
        self.savedChanges = True
        
        # Frame For Selection Combo
        self.selectionFrame = tk.Frame(self, bg=self.bg)
        self.selectionLab = tk.Label(self.selectionFrame,
                                          text ="Vorgangsmappe wählen:",
                                          bg = self.bg)
        self.selectionComboVar = tk.StringVar()
        self.selectionCombo = ttk.Combobox(self.selectionFrame,
                                              textvariable =self.selectionComboVar,
                                              width = 49)
        self.selectionCombo.bind('<<ComboboxSelected>>', self.displayFolder)
        self.returnBut = tk.Button(self.selectionFrame, text = "Zurück", command =
                                   lambda:self.controller.
                                   returnToPrev(self.savedChanges,
                                                self.pageName))
        self.newPFolderBut = tk.Button(self.selectionFrame, text = "Neue Vorgangsmappe", command =
                                 self.newFolder)
        
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
        self.placeholderFrame=tk.Frame(self, bg=self.bg)
        self.placeholderLab = tk.Label(self.placeholderFrame,
                                          text ='Platzhalter im Titel einfügen:',
                                          bg = self.bg)
        self.placeholderLBoxVar = tk.StringVar(value=list(self.
                                                          controller.
                                                          placeholderChoices))
        self.placeholderLBox = tk.Listbox(self.placeholderFrame,
                                          listvariable = self.placeholderLBoxVar,
                                          width = 20, height = 5)
        self.placeholderLBox.bind('<Double-Button-1>', self.insertPlaceholder)
##        self.insertLBoxVals()


        # Additional Buttons
        self.saveBut = tk.Button(self, text = "Speichern", command =
                                 self.saveChanges)        
        self.deleteBut = tk.Button(self, text = "Vorgangsmappe löschen", command =
                                 self.delete)
        
        
        # Grid Config
            # Selection Combo
        self.selectionLab.grid(row =0, column = 0)
        self.selectionCombo.grid(row =0, column = 1)
        self.returnBut.grid(row =1, column = 0, pady = 2)
        self.newPFolderBut.grid(row =1, column = 1, pady = 2)
            # Entry Frame
        for i in range(len(self.entryFieldsNames)):
            self.entryLabels[list(self.entryLabels)[i]].grid(
                row =i, column = 0, sticky = 'w', padx = 5)
            self.entryFields[list(self.entryLabels)[i]].grid(
                row =i, column = 1, pady = 2)
            # Placeholder Frame
        self.placeholderLab.pack()
        self.placeholderLBox.pack()

        
        self.selectionFrame.grid(row =0, column = 0, pady = 5, columnspan = 2)
        self.entryFieldsFrame.grid(row =1, column = 0)
        self.placeholderFrame.grid(row =1, column = 1)
        
        
        self.saveBut.grid(row =2, column = 0)
        self.deleteBut.grid(row =2, column = 1)
        

    def onRaise(self):
        self.updateSelectionBox()
        self.controller.root.title('This is ProcessFolderEditPage')
        self.controller.root.geometry(self.controller.configVars['ProcessFolderEditPageDimensions'])
        self.config(bg = self.controller.configVars['ProcessFolderEditPageColor'])

                                                                   
    def update(self, procId,*args):
        pass

    def updateSelectionBox(self):
        # Updates the Selectioncombo
        self.folderTitleToId = {}
        for folder in self.controller.processFolders.values():
            self.pFolderTitleToId[
                f'{folder.idNum}: {folder.title}'] = folder.idNum
        self.selectionCombo['values'] = list(self.pFolderTitleToId)

##    def insertLBoxVals(self):
##        for key in self.controller.placeholderLBoxChoices:
##            self.placeholderLBox.insert('end', key)
####            self.placeholderLBox.itemconfig('end', background = "red")

    def displayFolder(self, event):
        # Fills the Enty-fields with the data of the selected Folder
##        if type(eventOrNum) == "<class 'tkinter.Event'>":
        self.savedChanges = False
        idOfSelected = self.pFolderTitleToId[self.selectionCombo.get()]
        self.selectedProcessFolder = self.controller.processFolders[idOfSelected]
        for field in self.entryFields:
            self.entryFieldsVars[field].set(self.selectedProcessFolder.__dict__[field])

    def insertPlaceholder(self, event):
        self.savedChanges = False
        selectedIndex = self.placeholderLBox.curselection()
        selection = self.placeholderLBox.get(selectedIndex)
        selection = '{' + str(self.controller.placeholderChoices[selection])+'}'
        titleEntry = self.entryFieldsVars['title']
        titleEntry.set(titleEntry.get()+str(selection))
        
    def saveChanges(self):
        changes = {name:entry.get() for
                   name, entry in
                   self.entryFields.items()}
        self.selectedProcessFolder.fillFromDict(changes)
        if self.selectedProcessFolder.title == "":
            messagebox.showwarning(message='Bitte geben Sie einen Titel ein')
            return
        with closing(sql.connect(
            self.controller.configVars["DataBase"])) as con:
            self.selectedProcessFolder.saveToDb(con)
        self.controller.processFolders[
            self.selectedProcessFolder.idNum]= self.selectedProcessFolder
        self.updateSelectionBox()
        self.savedChanges = True


    def delete(self):
        if self.selectedProcessFolder.idNum == "":
            return
        message = messagebox.askyesno(message = 'Sind Sie sicher, dass Sie diese Vorgangsmappe LÖSCHEN WOLLEN?')
        if message == True:
            with closing(sql.connect(self.controller.configVars["DataBase"])) as con:
                self.selectedProcessFolder.delete(con)
            del self.controller.processFolders[self.selectedProcessFolder.idNum]
            for field in self.entryFields:
                self.entryFieldsVars[field].set('')
            self.selectionComboVar.set('')
            self.updateSelectionBox()
            self.savedChanges=True
        else:
            return
            
    
    def newFolder(self):
        self.savedChanges = False
        self.selectionCombo.set("Neue Vorgangsmappe")
        self.selectedProcessFolder = Models.ProcessFolder()
        for field in self.entryFields:
            self.entryFieldsVars[field].set(self.selectedProcessFolder.__dict__[field])
        
