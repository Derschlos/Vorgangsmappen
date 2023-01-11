import tkinter as tk
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
        self.pfList

        
        # Grid
        self.editPageBut.pack()

    def onRaise(self):
        self.controller.root.title('This is CreateProcessPage')
        self.controller.root.geometry(self.controller.configVars['CreateProcessPageDimensions'])
        self.config(bg = self.controller.configVars['CreateProcessPageColor'])

    def update(self, textId,*args):
        pass
    def showEditFrame(self):
        self.controller.showFrame('ProcessFolderEditPage')
        self.controller.setLastFrame('CreateProcessPage')
