

from todoapp.models import users,todos

session= {}


def SigninRequird(fn):
    def wrapper(*args,**kwargs):
        if "user " in session:
            return fn(*args,**kwargs)
        else:
            print(("U must Login "))
    return wrapper

def autenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] ==password]
    return user


class Signinview:
    username:str
    password:str
    def post(self, *args,**kwargs):
        print( autenticate(username="anu",password="Password@123"))
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = [user for user in users if user["username"] == username and user["password"] == password]
        if user:
            session["user"]=user[0]
            print("Success")
            print(session)
        else:
            print("Invalid")


class Todoview:
    @SigninRequird
    def get(self,*args,**kwargs):
        return
    def post(self,*args,**kwargs):
        print(kwargs)
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        print(kwargs)

class MyTodoView:

    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        my_todo=[todo for todo in todos if todo["userid"]==userId]
        print(my_todo)
        return my_todo

    def edit(self,*args,**kwargs):
        print(session)




sign=Signinview()
sign.post(username="anu",password="Password@123")
todo=MyTodoView()
todo.get()



