import tkinter as tk
from tkinter import messagebox
import Models


class MapEditPage(tk.Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.pageName = 'MapEditPage'
        self.controller = controller
        self.bg = self.controller.configVars['MapEditPageColor']
        self.placeholders = Models.Placeholders()

        ####  entriyFieldsFrame ###
        self.entryFieldsFrame = tk.Frame(self, bg=self.bg)
        self.entryFieldsNames = {'sourceNr':"Vorlagen Nummer",
                          'title':"Vorgangsmappen Titel",
                          'dokDat':"Dokument Datum",
                          'year': "Veranlagungsjahr",
                          'folder':"Ablage Ordner",
                          'register':"Ablage Register",
                           "user": "Verantwortlicher"}
        self.entryFieldsVars = {name:tk.StringVar() for name in self.entryFieldsNames}
        self.entryFields = {
                    name:tk.Entry(self.entryFieldsFrame,
                                textvariable = self.entryFieldsVars[name],
                                width = 49)
                    for name in self.entryFieldsNames}
        self.entryLabels = {
                    name:tk.Label(self.entryFieldsFrame,
                                  text =self.entryFieldsNames[name],
                                  bg = self.bg)
                    for name in self.entryFieldsNames}
        ####

        ### Design
        self.entryFieldsFrame.pack()
        for entry in self.entryFieldsNames:
            self.entryLabels[entry].pack()
            self.entryFields[entry].pack()




    def onRaise(self):
        self.controller.root.title('This is MapEditPage')
        self.controller.root.geometry(self.controller.configVars['MapEditPageDimensions'])
        self.config(bg = self.controller.configVars['MapEditPageColor'])

                                                                   
    def update(self, textId,*args):
        pass
