class ConfigMan:
    @staticmethod
    def intDict():
        f = open('conf.ini', 'r+')
        lines = f.read().splitlines()
        f.close()
        i = 0
        while i < len(lines):
            if '[' not in lines[i + 1]:
                confic.update({lines[i]: int(lines[i + 1])})
            else:
                lines[i + 1] = lines[i + 1].replace("[", "")
                lines[i + 1] = lines[i + 1].replace("]", "")
                liste = lines[i + 1].split(" ")
                list = []
                for eintrag in liste:
                    if not eintrag == "":
                        list.append(int(eintrag))
                confic.update({lines[i]: np.asarray(list)})
            i = i + 2
        logging.info("Thread %s: Flight-Config initialisiert", name)
        return config
    def getDict():
        return config

    config = intDict

