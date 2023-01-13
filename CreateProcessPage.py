import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Models


class CreateProcessPage(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.pageName = 'CreateProcessPage'
        self.controller = controller
        self.bg = self.controller.configVars['CreateProcessPageColor']
        
        self.editPageBut = tk.Button(self,
                                     text='Vorgangsmappen bearbeiten',
                                     command = self.showEditFrame)
        # Process Folder Selection Frame
        self.pFSelectionFrame = tk.Frame(self,bg=self.bg)
        self.pFSelectionVar = tk.StringVar()
        self.pFSelectionCombo = ttk.Combobox(self.pFSelectionFrame,
                                              textvariable =self.pFSelectionVar)
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
        
        self.pFListboxVar = tk.StringVar()
        self.pFListbox = tk.Listbox(self.pFListboxFrame,
                                    width = 20, height = 5)
        

        self.addInfoVar = tk.StringVar()
        self.addInfoEnt = tk.Entry(self,
                                    textvariable =self.addInfoVar)
        self.addInfoLab = tk.Label(self,
                                   text = "Zusätzliche Titel Info",
                                   bg = self.bg)
        # Grid
        self.editPageBut.pack()
        #
        self.pFSelectionFrame.pack()
        self.pFSelectionLab.pack()
        self.pFSelectionCombo.pack()
        self.addInfoLab.pack()
        self.addInfoEnt.pack()
        self.addProcessFolderBut.pack()
        #

        

    def onRaise(self):
        self.controller.root.title('This is CreateProcessPage')
        self.controller.root.geometry(self.controller.configVars['CreateProcessPageDimensions'])
        self.config(bg = self.controller.configVars['CreateProcessPageColor'])

    def update(self, textId,*args):
        pass
    def showEditFrame(self):
        self.controller.showFrame('ProcessFolderEditPage')
        self.controller.setLastFrame('CreateProcessPage')

    def addPFToLbox(self):
        pass
