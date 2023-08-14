from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement

def index(request):
    advertisements =  Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    #form = AdvertisementForm()
    #context = {'form' : form}
    #return render(request, 'advertisement_post.html', context)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            asvertisement = Advertisement(**form.cleaned_data)
            Advertisement.user = request.user
            Advertisement.save()
            url = reverse('main-page')
            return redirect(url)
        context = {'form':form}
        return render(request, 'advertisement-post.html', context)