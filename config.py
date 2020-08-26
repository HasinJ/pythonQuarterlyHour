
class config():
    def __init__(self):
        import MySQLdb
        self.__radUser = StringVar()
        self.__radPass = StringVar()
        self.__directory = StringVar()

        self.__RDSHost = StringVar()
        self.__RDSUser = StringVar()
        self.__RDSPass = StringVar()
        self.__RDSDb = StringVar()

        self.MySQLdb = MySQLdb
        self.mydb = self.MySQLdb.connect(host = self.__RDSHost,
            user = self.__RDSUser,
            passwd = self.__RDSPass,
            db = self.__RDSDb)

    def getDirectory(self):
        return self.__directory

    def getRadUser(self):
        return self.__radUser

    def getRadPass(self):
        return self.__radPass
