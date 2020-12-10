from django.shortcuts import render

# Create your views here

def view_bag(request):
    """ A viewto return the index page """
    return render(request, 'bag/bag.html')