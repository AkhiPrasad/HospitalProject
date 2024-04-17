import reg
from django.http import JsonResponse
from django.shortcuts import render, redirect

from HospitalApp.forms import hospitalform
from HospitalApp.models import mainpg, Reg


# Create your views here.

def Main(request):
    return render(request, 'MainPage.html')


def Doctor(request):
    return render(request, 'Dr.html')


def About(request):
    return render(request, 'Aboutus.html')


def deptartment(request):
    return render(request, 'Dept.html')


def addbooking(request):
    if request.method == 'POST':
        name = request.POST.get('n1')
        age = request.POST.get('a1')
        gender = request.POST.get('g1')
        department = request.POST.get('d1')
        phone = request.POST.get('p1')
        email = request.POST.get('e1')
        v1 = Reg(Name=name, Age=age, Gender=gender, Department=department, Phone=phone, Email=email)
        v1.save()
    return render(request, 'BookingWeb.html')


def newpg(request):
    f = hospitalform()
    new2 = {'key1': f}

    # if request.method == 'POST':
    #     form = hospitalform(request.POST, request.FILES)  # Ensure to pass request.FILES
    #     if form.is_valid():
    #         form.save()
    #         return redirect("m1")

    if request.method == 'POST' and request.is_ajax():
        form = hospitalform(request.POST, request.FILES)
        # form = hospitalform(request.POST, request.FILES)  # Ensure to pass request.FILES

        if form.is_valid():
            form.save()
            print('hiiiiii')
            return JsonResponse({
                'msg': 'Success'
            })
    return render(request, 'Bookingpg.html', new2)
