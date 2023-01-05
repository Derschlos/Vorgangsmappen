import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\davidleonschmidt\Desktop\Progs\OCR_Scanner\tesseract-oc\tesseract.exe'

def allConturesMinMax(image, sizeMin, sizeMax):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    boxes = []
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        size = w*h
        if sizeMin<size<sizeMax:
            boxes.append((x,y,w,h))
    return set(boxes)

def returnFields(cvImage):
    heigth,width,channels = cvImage.shape
    inputFields = allConturesMinMax(cvImage, 600, 20*width)
    posFieldNames = ['Kenntnisnehmer',
                         'Bearbeiter',
                         'Arbeitnehmer',
                         'Jahr',
                         'Dokumentdatum',
                         'Dokumentklasse',
                         'Ordner',
                         'Register',
                         'Ablage-Knigge',
                         'Status',
                         'Monat',
                         'Bereich',
                         ]
        
    fieldsByName = {}
    for field in inputFields:
        (x,y,w,h) = field
        xoffset = max(x-120,0)
        nameField = readImage[y:y+h, xoffset:x]
        cv2.rectangle(readImage,(xoffset,y), (x,y+h),(36,255,12),3)
        name = pytesseract.image_to_string(nameField, lang = 'deu')
        name = re.search('\w+(-)?(\w+)?', name)
        if not name:
            continue
        if name[0] in posFieldNames:
            fieldsByName[name[0]] =(x, y+5)

    return fieldsByName
