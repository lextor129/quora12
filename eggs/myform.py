import datetime
from django import forms
from eggs.models import Eggs
from django.utils import timezone
from crispy_forms.helper import FormHelper




FRUIT_CHOICES= (("A", "A"), ("AA", "AA"),("EXTRA", "EXTRA"),("B", "B"))

class Myform(forms.ModelForm):
    customer = forms.CharField()
    quantity = forms.IntegerField()
    price = forms.FloatField()
    type = forms.TypedChoiceField(
        label="Type",
        choices=FRUIT_CHOICES,
        #coerce=lambda x: bool(int(x)),

        widget=forms.RadioSelect,
        initial='',
        required=True,
    )
    '''type = forms.CharField(label='Type', widget=forms.RadioSelect(choices=FRUIT_CHOICES))'''
    pub_date = forms.DateTimeField(initial=datetime.datetime.now(),
                                   widget=forms.TextInput(attrs={'readonly':'readonly'}))



    class Meta:
        model = Eggs
        fields = ('customer','quantity','price', 'type','pub_date')





