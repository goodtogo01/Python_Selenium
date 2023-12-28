import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\zaman\\PycharmProjects\\PythonSelenium\\Configurations\\config.ini")


class ReadProperties:
    @staticmethod
    def getURL():
        url = config.get('common properties', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        userName = config.get('common properties', 'username')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('common properties', 'password')
        return password
