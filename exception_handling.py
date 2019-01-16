"""
When these exceptions occur, it causes the current process to stop and passes it to the calling process until it is handled. If not handled, our program will crash.
 
syntax:
   . try:
        [suspicious code]
    except([exception]):
        [handling code]
    finally:
        [is to be executed]
"""
class Bank:
    __saving = 15000
    def returnSaving(self):
        print(self.__saving)
    def changeSaving(self,saving):
        self.__saving = saving

b = Bank()
try:
    print(b.__saving)
except Exception:
    print("there is no such attribute")
finally:
    print("Sorry for troubles just let it slide")
print("Before Update")
b.returnSaving()
print("After update")
# b.__saving = 150000
b.changeSaving(1500000)
b.returnSaving()