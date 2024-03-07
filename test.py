class Cls:
    NickName="How How"
    def __init__(self,str) -> None:
        self.Name=str
    def StaticFunc():
        return "123456"
    def DynamicFunc(self):
        return "789"
    

print(Cls.StaticFunc())
# print(Cls.DynamicFunc())

newCls1=Cls("Jack")
newCls2=Cls("Ken")
newCls3=Cls("Amy")

print(newCls1.DynamicFunc())
