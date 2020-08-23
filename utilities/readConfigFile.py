import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getAppUrl():
        appUrl = config.get("common Info","baseUrl")
        return appUrl
    @staticmethod
    def getUsername():
        username = config.get("common Info","username")
        return username
    @staticmethod
    def getPwd():
        pwd = config.get("common Info","password")
        return pwd