import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/umari/PycharmProjects/InspireAutomation/src/Configurations/config.ini")


class ReadData:
    @staticmethod
    def getURL():
        url = config.get("login_details", "url")
        return url

    @staticmethod
    def getEmail():
        username = config.get("login_details", "email")
        return username

    @staticmethod
    def getPassword():
        password = config.get("login_details", "password")
        return password

