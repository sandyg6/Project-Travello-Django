from django.shortcuts import render
from . models import Destination

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "The city never sleeps"
    dest1.img = 'destination_1.jpg'
    dest1.price = 789
    dest1.offer = False


    dest2 = Destination()
    dest2.name = 'Chennai'
    dest2.desc = "Beaches and Night life"
    dest2.img = 'destination_2.jpg'
    dest2.price = 879
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Delhi'
    dest3.desc = "Cold Breeze and Wonders"
    dest3.img = 'destination_3.jpg'
    dest3.price = 978
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})