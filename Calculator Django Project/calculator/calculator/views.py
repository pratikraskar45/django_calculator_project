from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse ("welcome to my page")


def calculator(request):
    c=''
    data={ }
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            data= {
                'n1':n1,
                'n2':n2,
                'opr':opr,
                'c':c,
                
            }
                
    except:
        c="Invalid Opration"
        print(c)
    return render(request,"calculator.html",data)