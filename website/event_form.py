from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    CHOICES = [('1', 'I'),
               ('2', 'II'),
               ('3', 'III'),
               ('4', 'IV'), ]

    # category = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple,)

    class Meta:

        model = Event

        start_date = forms.DateField()
        end_date = forms.DateField()

        fields = ('name', 'description', 'start_date', 'end_date')

        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Event Name', 'class': 'form-control',
                                                  'id': 'event_name'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control',
                                                        'id': 'event_desc'}),
                   'start_date': forms.DateInput(format='%d-%m-%y',
                                                 attrs={'class': 'form-control', 'id': 'event_start_date',
                                                        'type': 'date'}),
                   'end_date': forms.DateInput(format='%d-%m-%y',
                                               attrs={'class': 'form-control', 'id': 'event_end_date',
                                                      'type': 'date'}),
                  }
