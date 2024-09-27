#method vs @classmethod vs @staticmethod
#method - self, método de INSTÂNCIA
#@classmethod - cls, método de CLASSE
#@staticmethod - método estático ((SEM X)SELF, (SEM X)CLS)



         #método de instância(self)
# class Connection:
#     def __init__(self, host='localhost'):
#         self.host = host
#         self.user = None
#         self.password = None
    
#     def set_user(self, user): #setter
#         self.user = user
#     def set_password(self, password): #setter
#         self.password = password

# c1 = Connection()
# c1.set_user('Yuri')
# c1.set_password(31052017)
# print(c1.user)
# print(c1.password)


        #método de classe(cls)
# class Connection:
#     @classmethod
#     def creat_with_auth(cls, user, password):
#         connection = cls()
#         connection.user = user
#         connection.password = password
#         return connection

# c1 = Connection.creat_with_auth('Maria', '22091972')
# print(c1.user)
# print(c1.password)


        #@staticmethod
class Connection:
    @staticmethod
    def soma(x, y):
        return x + y
    
print(Connection.soma(3, 2))
    