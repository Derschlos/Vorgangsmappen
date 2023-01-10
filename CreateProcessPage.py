import tkinter as tk
from tkinter import messagebox
import Models


class CreateProcessPage(tk.Frame):
    def __init__(self,parent, controller):
##        tk.Frame.__init__(self, parent)
        super().__init__(parent)
        self.pageName = 'CreateProcessPage'
        self.controller = controller
##        self.bg = self.controller.configString['EditPageColor']


    def onRaise(self):
        self.controller.root.title('This is Page 2')
        self.controller.root.geometry(self.controller.configVars['page2Dimensions'])
        self.config(bg = self.controller.configVars['page2Color'])

    def update(self, textId,*args):
        pass
