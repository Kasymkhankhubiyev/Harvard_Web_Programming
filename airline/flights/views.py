from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request: HttpRequest, flight_id: int) -> HttpResponse:
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()  # passengers except ones that are already on a flight
    })


def book(request: HttpRequest, flight_id: int) -> HttpResponse:
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)  # getting a flight by its id/pk
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))  # gets a passenger with a scpecific id/pk
        passenger.flights.add(flight)  # addes a flight to a passenger table
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

