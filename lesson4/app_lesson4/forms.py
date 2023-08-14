from django import forms

class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg'}))
    price = forms.DecimalField()
    auction = forms.BooleanField(required=False)
    image = forms.ImageField()