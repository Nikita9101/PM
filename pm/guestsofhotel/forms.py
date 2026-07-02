from django import forms
from guestsofhotel.models import Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest

        fields = "__all__"
        widgets = {

            "birthday": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }