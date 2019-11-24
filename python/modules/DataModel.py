import cv2

class DataModel:
    def __init__(self):
        self.currentPosition = [0, 0, 0]
        self.currentSpeed = [0, 0, 0]
        self.currentRotation = 0
        self.ParcelPosition = [0,0,0]
        self.TargetPosition = [0,0,0]
        self.regSquare = 0
        self.frame = 0
        self.filteredFrame = False
        self.carryParcel = False
        self.grapclosed = False
        self.closegrap = False
        self.running = True
        self.state = 0
        self.ResivedCoordinates = False
        self.nextCoordinates = [0,0,0]
        self.onCoordinates = False
        self.exitcam = False

    def getexitcam(self):
        return self.exitcam

    def setexitcam(self, Boolean):
        self.exitcam = Boolean



    def getstate(self):
        return self.state

    def setstate(self, float):
        self.state = float

    def getResivedCoordinates(self):
        return self.ResivedCoordinates

    def setResivedCoordinates(self, Boolean):
        self.ResivedCoordinates = Boolean

    def getRunning(self):
        return self.running

    def setRunning(self,Boolean):
        self.running = Boolean


    def getonCoordinates(self):
        return self.onCoordinates

    def setonCoordinates(self,Boolean):
        self.onCoordinates = Boolean


    def getgrapclosed(self):
        return self.grapclosed

    def setgrapclosed(self,Boolean):
        self.grapclosed = Boolean


    def getclosegrap(self):
        return self.closegrap

    def setclosegrap(self,Boolean):
        self.closegrap = Boolean




    def getRegSquare(self):
        return self.regSquare

    def setRegSquare(self, float):
        self.regSquare = float

    def getTargetPosition(self):
        return self.TargetPosition

    def setTargetPosition(self, array):
        self.TargetPosition = array

    def getParcelPosition(self):
        return self.ParcelPosition

    def setParcelPosition(self, array):
        self.ParcelPosition = array

    def getCurrentPosition(self):
        return self.currentPosition

    def setnextCoordinates(self, array):
        self.nextCoordinates = array

    def getnextCoordinates(self):
        return self.nextCoordinates

    def setCurrentPosition(self, array):
        self.currentPosition = array

    def getCurrentSpeed(self):
        return self.currentSpeed

    def setCurrentSpeed(self, array):
        self.currentSpeed = array