from django.shortcuts import render
# from booktest.modeles import BookInfo
# Create your views here.

def index(request):
    a=10
    return render(request,'booktest/index.html',{'a':10})

def index2(request):
    return render(request,'booktest/index2.html')


# def temp_var(request):
#     my_dict={'title':'字典键值'}
#     my_list=[1,2,3]
#     book=BookInfo.objects.get(id=1)
#
#     context={'my_dict':my_dict,'my_list':my_list,'book':book}
#     return render(request,'booktest/temp_var.html',context)

