from django.http import HttpRequest
from django.shortcuts import render

# In Django there are two types of views. Function based View and Class based view
# Function based View
def home(request: HttpRequest):
    if request.method == 'GET':
        msg: str = 'Welcome to Home'
        return render(request,"index.html", {'message': msg})


def add(request: HttpRequest):
    if request.method == 'POST':
        fNum: int = int(request.POST['firstNumber'])
        sNum: int = int(request.POST['secondNumber'])
        print(fNum+sNum)
        return render(request,"create.html")
    
    return render(request,"create.html")