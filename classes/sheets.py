import pandas as pd
import pygsheets

class Parser():
    def __init__(self,sheetName):
        self.gc = pygsheets.authorize(service_file='garebear-382519-ca75277f19dc.json')
        self.sheet = self.gc.open(sheetName)

    def readCell(self,sheetTabName,rowNum, colNum):
        self.wks = self.sheet.worksheet('title',sheetTabName)
        return wks.get_value(str(colNum)+str(rowNum))
    
    def updateCell(self,sheetTabName,rowNum, colNum, updatedValue):
        self.wks = self.sheet.worksheet('title',sheetTabName)
        return wks.update_value(str(colNum)+str(rowNum), updatedValue)