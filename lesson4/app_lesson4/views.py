from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement

def index(request):
    advertisements =  Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisement/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save()
            advertisement.author = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'app_advertisement/advertisement_post.html', context)