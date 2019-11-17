import numpy as np
import logging


class ConfigMan:
    def __init__(self):
        self.config = dict()
        self.loadConf()


    def getDict(self):
        return self.config


    def loadConf(self):
        f = open('../conf.ini', 'r+')
        lines = f.read().splitlines()
        f.close()
        i = 0
        while i < len(lines):
            if '[' not in lines[i + 1]:
                self.config.update({lines[i]: int(lines[i + 1])})
            else:
                lines[i + 1] = lines[i + 1].replace("[", "")
                lines[i + 1] = lines[i + 1].replace("]", "")
                liste = lines[i + 1].split(" ")
                list = []
                for eintrag in liste:
                    if not eintrag == "":
                        list.append(int(eintrag))
                self.config.update({lines[i]: np.asarray(list)})
            i = i + 2
        #logging.info("Thread %s: Flight-Config initialisiert", name)


    def saveConf(self):
        file = open('conf.ini', 'w')
        for var in self.config:
            file.write(var + "\n")
            file.write(str(self.config[var]) + "\n")


