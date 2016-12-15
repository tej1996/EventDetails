from django import forms


class EventForm(forms.Form):
    event_name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)
    start_date = forms.DateField()
    end_date = forms.DateField()
