class User:

    def __init__(self,first_name,last_name):
        self.user_first_name=first_name
        self.user_last_name=last_name

    def get_user_first_name(self):
        return self.user_first_name

    def get_user_last_name(self):
        return self.user_last_name

    def get_user_info(self):
        return f" имя фамилия:{self.user_first_name} {self.user_last_name}"


user=User("Светлана","Лунёва")
print (user.get_user_first_name())
print (user.get_user_last_name())
print (user.get_user_info())


    