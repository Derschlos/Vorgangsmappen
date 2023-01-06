import pyautogui as ag
import pyperclip
import time
import re
import win32gui
import DatevAblageFieldsSucher as DAFS
from numpy import array
import cv2
from PIL import Image

def down(times = 1,extra = ''):
    ag.hotkey('numlock')
    for i in range(times):
        ag.hotkey('down', extra)
    ag.hotkey('numlock')

def tab(times):
    for i in range(times):
        ag.hotkey('tab')
    return
def switch(name):
    windows =[]
    def window_enumeration_handler(hwnd, windows):
        """Add window title and ID to array."""
        windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(window_enumeration_handler, windows)
    for window in windows:
        winNum, winName = window
        if re.search(name,str(winName)) is not None:
            win32gui.SetForegroundWindow(winNum)
            time.sleep(1)
            return winNum

def ablageFields(winNum):
    x,y,w,h = win32gui.GetWindowRect(winNum)
    screen = ag.screenshot()
    screen = screen.crop((x,y,w,h))
    cvImage = cv2.cvtColor(array(crop), cv2.COLOR_RGB2BGR)
    fields=DAFS.getInputFields(cvImage)
    fields = {key:(value[0]+x, value[1]+y) for (key,value) in fields.items()}
    return fields

def inputIntoFields(data,fields):
    for dataKey,dataVal in data.items():
        ag.click(fields[dataKey])
        tab(dataVal[0])
        paste(dataVal[1])
        time.sleep(0.2)
    
def paste(text):
    pyperclip.copy(text)
    ag.hotkey('ctrl','v')
    time.sleep(0.2)

def createMap(mdt,title,fields = None):
    switch('DATEV Arbeitsplatz')
    ag.hotkey('ctrl','g')
    time.sleep(1)
    switch('827055')
    ag.keyDown('shift')
    down(times = 7)
    ag.keyUp('shift')
    ag.hotkey('alt')
    ag.typewrite('bk')
    switch('Vorgangsmappe anlegen')
    ag.hotkey('alt')
    ag.typewrite('bi')
    ag.hotkey('alt')
    ag.typewrite('sh')
    time.sleep(5)
    try:
        if not fields:
            ablage= switch('Dokumentenmanagement ablegen')
            fields = ablageFields(ablage)
        inputData={
            # first value is amount of tabs, second is the value to be filled
            'Ablage-Knigge':(0,'Vorgangsmappe'),
            'Ablage-Knigge':(1,f'Vorgangsmappe EW-Erklärung 01.01.2022 für {title}'),
            'Bereich':(1,mdt),
            'Dokumentdatum':(0,'11.08.2022'),
            'Jahr':(0,'2022'),
            'Ordner':(0,'03 Steuer-Akte'),
            'Register':(0,'A Arbeitsunterlagen')
            }
            
        inputIntoFields(inputData, fields)
    except Exception as e:
        print(e)
        input()
##    ag.hotkey('tab')
##    ag.typewrite('Vorgangsmappe')
##    time.sleep(0.4)
##    ag.hotkey('tab')
##    paste(f'Vorgangsmappe EW-Erklärung 01.01.2022 für {title}')
##    tab(2)
##    ag.typewrite(mdt, interval = 0.1)
##    tab(4)
##    time.sleep(0.3)
##    paste('11.08.2022')
##    tab(1)
##    paste('2022')
##    tab(3)
##    ag.hotkey('enter')
##    tab(3)
##    paste('03 Steuer-Akte')
##    tab(1)
##    paste('A Arbeitsunterlagen')
    ag.hotkey('enter')
    ag.hotkey('enter')
    time.sleep(1)
    return fields
    
input()
time.sleep(3)
fields = createMap('11016','testmappe1')
createMap('11016','testmappe2',fields)
createMap('11016','testmappe3',fields)
##
##time.sleep(2)
##winsound.Beep(440,500)
##createMap('11016','testmappe')
####ag.hotkey('ctrl','c')
##x = pyperclip.paste()
####pyperclip.copy('x')
##ag.hotkey('alt','tab','tab', interval = 0.5)
####ag.hotkey('alt','tab', interval = 0.5)
####print(pyperclip.paste())
##pyperclip.copy(x)
##ag.hotkey('ctrl','v')

##print(sys._current_frames())
##sys._getframe(2)


##
##time.sleep(2)
##print(win32gui.EnumWindows(window_enumeration_handler, top))
##for w in top:
##    print(w)

