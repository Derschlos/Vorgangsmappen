import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Models
import re


class CreateProcessPage(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.pageName = 'CreateProcessPage'
        self.controller = controller
        self.bg = self.controller.configVars['CreateProcessPageColor']
        self.pFolderTitleToId = {}
        self.addInfoVars = {}
        self.mandates = {}
        self.addInfoFields = {}
        self.currentMdt = Models.Mdt()
        
        
        self.editPageBut = tk.Button(self,
                                     text='Vorgangsmappen bearbeiten',
                                     command = self.showEditFrame)
        # Process Folder Selection Frame
        self.pFSelectionFrame = tk.Frame(self,bg=self.bg)
        self.pFSelectionVar = tk.StringVar()
        self.pFSelectionCombo = ttk.Combobox(self.pFSelectionFrame,
                                              textvariable = self.pFSelectionVar)
        self.pFSelectionCombo.bind('<<ComboboxSelected>>', self.createAddInfoFields)
        self.pFSelectionLab = tk.Label(self.pFSelectionFrame,
                                       text = "Vorgangsmappe:",
                                       bg = self.bg)     
        self.addProcessFolderBut = tk.Button(self.pFSelectionFrame,
                                   text = "Vorgangsmappe zur Liste Hinzufügen",
                                   command = self.addPFToLbox)

        # Process Folder Listbox Frame
        # this need to be renamed to something more descriptive
        # since these are the PF to be added to the DATEV system
        self.pFListboxFrame = tk.Frame(self,bg=self.bg)
        self.pFListboxLab = tk.Label(self.pFListboxFrame,
                                     text = "Ausgewählte Vorgangsmappe",
                                     bg = self.bg)
        self.pFListboxVar = tk.StringVar(value = list(self.currentMdt.processes))
        self.pFListbox = tk.Listbox(self.pFListboxFrame,
                                    listvariable = self.pFListboxVar,
                                    width = 20, height = 5)
        self.pFListbox.bind("<<ListboxSelect>>",
                            lambda e: self.showPFAddInfo(
                                self.pFListbox.curselection()))
        
        
        # Additional Info Entry
        self.addInfoFrame = tk.Frame(self,bg=self.bg)
        for field in self.controller.placeholderChoices.values():
            self.addInfoVars[field] = tk.StringVar()
       
        # Mdt Listbox
        self.mdtListboxFrame = tk.Frame(self,bg=self.bg)
        self.mdtListboxLab = tk.Label(self.mdtListboxFrame,
                                     text = "Ausgewählte Mandanten",
                                     bg = self.bg)
        self.mdtListboxVar = tk.StringVar(value = list(self.mandates))
        self.mdtListbox = tk.Listbox(self.mdtListboxFrame,
                                     listvariable = self.mdtListboxVar,
                                     width = 20, height = 5,
                                     exportselection = False)
        self.addMdtEntVar = tk.StringVar()
        validateMdtWrapper = (self.controller.root.register(self.validateMdtEntry),
                           '%P')
        self.addMdtEnt = tk.Entry (self.mdtListboxFrame,
                                   textvariable = self.addMdtEntVar,
                                   validate = 'key',
                                   validatecommand = validateMdtWrapper)
        self.addMdtBut = tk.Button(self.mdtListboxFrame,
                                   text = "Mandanten hinzufügen",
                                   command = self.addMdt)
        self.deleteMdtBut = tk.Button(self.mdtListboxFrame,
                                   text = "Mandanten löschen",
                                   command = self.deleteMdt)

        
        
        # Grid
        self.editPageBut.pack()
        #
        self.pFSelectionFrame.pack()#
        self.pFSelectionLab.pack()
        self.pFSelectionCombo.pack()
        
        self.pFListboxFrame.pack()#
        self.pFListboxLab.pack()
        self.pFListbox.pack()

        self.mdtListboxFrame.pack()#
        self.mdtListboxLab.pack()
        self.mdtListbox.pack()
        self.addMdtEnt.pack()
        self.addMdtBut.pack()
        self.deleteMdtBut.pack()
        
        self.addInfoFrame.pack()#
        # Fields are added in the createAddInfoFields method
        
        self.addProcessFolderBut.pack()
        #
        
        

    def onRaise(self):
        self.updatePFSelectionBox()
        self.controller.root.title('This is CreateProcessPage')
        self.controller.root.geometry(self.controller.configVars['CreateProcessPageDimensions'])
        self.config(bg = self.controller.configVars['CreateProcessPageColor'])

    def update(self, textId,*args):
        pass
    def showEditFrame(self):
        self.controller.showFrame('ProcessFolderEditPage')
        self.controller.setLastFrame('CreateProcessPage')

    def updatePFSelectionBox(self):
        # Updates the Selectioncombo
        self.pFolderTitleToId = {}
        for folder in self.controller.processFolders.values():
            self.pFolderTitleToId[
                f'{folder.idNum}: {folder.title}'] = folder.idNum
        self.pFSelectionCombo['values'] = list(self.pFolderTitleToId)

    def createAddInfoFields(self,event):
        i = 0
        for label,entry in self.addInfoFields.values():
            label.destroy()
            entry.destroy()
        self.addInfoFields = {}
        selectedPFTitle = self.pFSelectionVar.get()
        selectedPFID = self.pFolderTitleToId[selectedPFTitle]
        selectedPF = self.controller.processFolders[selectedPFID]                
        for field,stringvar in self.addInfoVars.items():
            if "{"+field+"}" in selectedPF.title:
                i += 1
                label = tk.Label(self.addInfoFrame,
                                 text = f'{self.controller.placeholders.__dict__[field]}:',
                                 bg = self.bg)
                
                entry = tk.Entry(self.addInfoFrame,
                                 textvariable = stringvar)
                label.grid(row = i, column = 1)
                entry.grid(row = i, column = 2)
                self.addInfoFields[field] = [label,entry]
            
    def addPFToLbox(self):
        if len(self.mandates) < 1:
            return
        mdtSelection = self.mdtListbox.curselection()
        mdt = self.mdtListbox.get(mdtSelection)
        self.currentMdt = self.mandates[mdt]
        print(self.currentMdt.mdtNr)
        
    def showPFAddInfo(self, selection):
        print(selection)
##        if len(self.mandates) < 1:
##            return
        
        
    def validateMdtEntry(self, newval):
        return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5
    
    def addMdt(self):
        mdt = self.addMdtEnt.get()
        if mdt == "" or len(mdt)< 5:
            return
        newMdt = Models.Mdt()
        newMdt.mdtNr = mdt
        self.mandates[mdt] = newMdt
        self.mdtListboxVar.set(value = list(self.mandates))
##        self.mdtListbox['exportselection'] = True
        self.mdtListbox.selection_clear(0,tk.END)
        self.mdtListbox.selection_set(len(self.mandates)-1)
##        self.mdtListbox['exportselection'] = False

    def deleteMdt(self):
        selectedIndex = self.mdtListbox.curselection()
        if len(selectedIndex) < 1:
            return
        selectedMdt = self.mdtListbox.get(selectedIndex)
        del self.mandates[selectedMdt]
        self.mdtListboxVar.set(value = list(self.mandates))


        
