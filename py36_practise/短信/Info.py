class Submit(object):
    # def __init__(self,apId,ecName,mobiles,content,sign,addSerial,mac):
    #     self.__apId=apId
    #     self.__ecName=ecName
    #     self.__mobiles=mobiles
    #     self.__content=content
    #     self.__sign=sign
    #     self.__addSerial=addSerial
    #     self.__mac=mac

    @property
    def apId(self):
        return self.__apId

    @apId.setter
    def apId(self, value):
        self.__apId = value

    @property
    def ecName(self):
        return self.__ecName

    @ecName.setter
    def ecName(self, value):
        self.__ecName = value

    @property
    def mobiles(self):
        return self.__mobiles

    @mobiles.setter
    def mobiles(self, value):
        self.__mobiles = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, value):
        self.__sign = value

    @property
    def addSerial(self):
        return self.__addSerial

    @addSerial.setter
    def addSerial(self, value):
        self.__addSerial = value

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, value):
        self.__mac = value

    # @property
    # def secretKey(self):
    #     return self.__secretKey
    #
    # @secretKey.setter
    # def secretKey(self, value):
    #     self.__secretKey = value



