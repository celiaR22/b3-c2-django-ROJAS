from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from booking.models import Cart, Reservation, pilotEvent

# vue page accueil avec la liste des events
def index(request):
    events = pilotEvent.objects.all()
    return render(request, 'booking/bookingList.html', context= {"events": events})

# vue page de détail d'un event
def event_detail(request, id):
    event = get_object_or_404(pilotEvent, id= id)
    return render(request, 'booking/detail.html', context= {"event": event})

#vue ajout dans le panier
def add(request, id):
    user = request.user
    event = get_object_or_404(pilotEvent, id= id)
    cart, _ = Cart.objects.get_or_create(user = user)
    reservation, created = Reservation.objects.get_or_create(user = user, pilotEvent = event)
       
    if created:
        cart.reservation.add(reservation)
        cart.save()
    else:
        reservation.quantity += 1
        reservation.save()
    
    event.nbPerson -= 1
    event.save()   
       
    return redirect(reverse("event_detail", kwargs={"id": id}))

#vue des reservations de l'utilisateur
def cart(request):
    cart, _ = Cart.objects.get_or_create(user = request.user)
    reservations = get_object_or_404(Cart, user = request.user)
    return render(request, 'booking/cart.html', context={"reservations": reservations.reservation.all()})

#suppression event
def delete(request, id):
    cart= Cart.objects.get(user = request.user)
    reservation = Reservation.objects.get(user = request.user, id = id)
    event = get_object_or_404(pilotEvent, id= reservation.pilotEvent_id)
    
    if reservation:
        reservation.delete()
        event.nbPerson += reservation.quantity
        event.save()
             
    return render(request, 'booking/cart.html', context={"reservations": cart.reservation.all()})