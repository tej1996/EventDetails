from django import forms
from django.forms.extras import SelectDateWidget

from .models import Event


class EventForm(forms.ModelForm):

    CHOICES = [('1', 'I'),
               ('2', 'II'),
               ('3', 'III'),
               ('4', 'IV'), ]

    # category = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple,)

    start_date = forms.DateField(widget=SelectDateWidget(years=range(2016, 2050)))
    end_date = forms.DateField(widget=SelectDateWidget(years=range(2016, 2050)))

    class Meta:
        model = Event

        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Event Name', 'class': 'form-control',
                                                  'id': 'event_name'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control',
                                                        'id': 'event_desc'}),
                   }
