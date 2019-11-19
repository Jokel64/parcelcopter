class DataModel:
    def __init__(self):
        self.__currentAltitude
        self.__currentPosition = []
        self.__currentRotation
        self.__TargetPosition = []
        self.__frame
        self.__filteredFrame
        self.__carryParcel = False
        self.__grapclosed = False


    def getCurrentAltitude(self):
        return self.__currentAltitude

    def setCurrentAltitude(self, float):
        self.__currentAltitude = float


    def getTargetPosition(self):
        return self.__TargetPosition

    def setTargetPosition(self, float):
        self.__TargetPosition = float

    def getTargetPosition(self):
        return self.__TargetPosition

    def setTargetPosition(self, float):
        self.__TargetPosition = float

