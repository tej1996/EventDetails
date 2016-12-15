from django.shortcuts import render
from django.http import HttpResponse
from website.event_form import EventForm
from website.models import Events

# Create your views here.


def index(request):
    return render(request, 'website/index.html')


def dashboard(request):
    return render(request, 'website/dashboard.html')


def profile(request):
    return render(request, 'website/profile.html')


def new_event(request):
        if request.method == 'POST':  # if the form has been filled
            form = EventForm(request.POST)
            if form.is_valid():  # All the data is valid
                name = request.POST.get('event_name', '')
                desc = request.POST.get('description', '')
                s_date = request.POST.get('start_date', '')
                e_date = request.POST.get('end_date', '')
            # creating an user object containing all the data
            event_obj = Events(event_name=name, description=desc, start_date=s_date, end_date=e_date)
            # saving all the data in the current object into the database
            event_obj.save()

            return render(request, 'website/dashboard.html')

        else:
            form = EventForm()  # an unboundform
            return render(request, 'website/dashboard.html', {'form': form})
