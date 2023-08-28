from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement
from django.contrib.auth import get_user_model
from django.db.models import Count
#https://github.com/skraler/advertisements
User = get_user_model()

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements =  Advertisement.objects.all()
    context = {'advertisements': advertisements,
               'title': title
               }
    return render(request, 'app_advertisement/index.html', context)

def top_sellers(request):
    users= User.objects.annotate(
        adv_count=Count('advertisement')
    ).order_by('-adv_count')
    context = {
        'users': users
    }
    return render(request, 'app_advertisement/top-sellers.html', context)

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'app_advertisement/advertisement_post.html', context)

def redir_adv(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {
        'advertisement': advertisement
    }
    return render(request, 'app_advertisement/advertisement.html', context)