class Bank:
    __saving = 15000
    def returnSaving(self):
        print(self.__saving)
    def changeSaving(self,saving):
        self.__saving = saving

b = Bank()
# print(b.__saving)
print("Before Update")
b.returnSaving()
print("After update")
# b.__saving = 150000
b.changeSaving(1500000)
b.returnSaving()