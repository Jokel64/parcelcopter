import numpy as np
import logging


class ConfigMan:


    def __init__(self):
        self.config = dict()
        self.loadConf()


    def loadConf(self):
        f = open('conf.ini', 'r+')
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
        return self.config

        #logging.info("Thread %s: Flight-Config initialisiert", name)

    def updateConf(name, value):
        self.config[name] = value

    def saveConf(self, config):
        file = open('conf.ini', 'w')
        for var in config:
            file.write(var + "\n")
            file.write(str(self.config[var]) + "\n")


    def getConfig(self):
            return self.config