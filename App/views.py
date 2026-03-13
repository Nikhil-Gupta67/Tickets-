from django.shortcuts import render, redirect
from .models import Flight, Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'App/home.html')


def search_flight(request):

    if request.method == "POST":

        source = request.POST['source']
        destination = request.POST['destination']

        flights = Flight.objects.filter(
            source=source,
            destination=destination
        )

        return render(request, 'App/search.html', {'flights': flights})

    return render(request, 'App/search.html')


def book_flight(request, id):

    flight = Flight.objects.get(id=id)

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']

        Booking.objects.create(
            passenger_name=name,
            email=email,
            flight=flight
        )

        return redirect('success')

    return render(request, 'App/book.html', {'flight': flight})


def success(request):
    return render(request, 'App/success.html')


# -------- USER REGISTER --------

def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'App/register.html')


# -------- USER LOGIN --------

def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)
            return redirect('home')

    return render(request, 'App/login.html')


# -------- USER LOGOUT --------

def logout_user(request):

    logout(request)
    return redirect('home')