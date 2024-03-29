from django.shortcuts import render
from app1.models import Products


# Create your views here.
def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html", {'nbar': 'home'})

def stock(request):
    return render(request, "stock.html", {'nbar': 'stock'})

def scan_in(request):
    return render(request, "scan_in.html", {'nbar': 'scan_in'})

def people(request):
    return render(request, "people.html", {'nbar': 'people'})

def members(request):
    return render(request, "members.html", {'nbar': 'members'})

def add_member(request):
    return render(request, "add_member.html", {'nbar': 'add_member'})

def scan_out(request):
    return render(request, "scan_out.html", {'nbar': 'scan_out'})

# def searchAjax(request, q):
#     print('Query? = ')
#     print(q)
#     productList=Products.objects.filter(name__contains=q)
#     n=len(productList)
#     print('Number of results:')
#     print(n)
#     if (n>0):
#         out=""
#         for x in productList:
#             print("test output")
#             # out+="<div class='bg-" + 'red' + "-500'>"
#             # out+="<div class='flex flex-row justify-center align-middle'>"
#             # out+="<div class='mb-3 xl:w-96'>"
#             # out+="<div class=input-group relative flex flex-wrap items-stretch w-full mb-4'>"
#             # out+="<form action=''>"
#             # out+="<label for=''>Search</label>"
#             # out+="<input type='text' name='' id='search' class='form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none' placeholder='Search' aria-label='Search' aria-describedby='button-addon3'>"
#             # out+="</form>"
#             # out+="</div>"
#             # out+="</div>"
#             # out+="</div>"
#             out+="<div class='justify-center text-center items-center flex flex-col h-screen w-screen' style='background-color:" + x.color + ";'>"
#             out+="<h1 class='md:text-5xl text-7xl'>" + x.name + "</h1>"
#             out+="</br>"
#             out+="<img class='h-100 w-100' src = '" + x.img + "'>"
#             out+="</br>"
#             out+="<p class='md:text-2xl text-5xl'>" + x.status + " | " + x.status_info + "</p>"
#             out+="<p class='md:text-lg text-3xl'><strong>" + str(x.daysSince) + "</strong> days since updated</p>"
#             out+="<p class='md:text-lg text-3xl'><strong>" + str(x.avg) + "</strong> average days between releases</p>"
#             out+="</div>"
#             out+="</br>"
#     else:
#         out=""
#         out+="<div class='justify-center text-center items-center flex flex-col h-screen w-screen' style='background-color:#F44336;' >"
#         out+="<p class='text-5xl'>no matching results</p>"
#         out+="</div>"
#     # print(out)
#     return HttpResponse(out)
