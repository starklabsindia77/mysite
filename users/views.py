from django.shortcuts import render
from django.contrib import messages
from .forms import DriverRegisterForm
from django.http import HttpResponseRedirect



# Create your views here.

def register(request):
    return render(request, 'users/register.html')


def driver(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DriverRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DriverRegisterForm()


    return render(request, 'users/driver.html', {'form': form})


def LoginCustomer(request):
    mobile = request.GET["mobile"]
    password = request.GET["password"]
    result = mobile, password
    return render(request, 'users/customer.html', {'result' : result})



