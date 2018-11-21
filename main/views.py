from django.shortcuts import render, redirect,get_object_or_404
import random
from .models import Urls


def hash_url(request):
    if request.method == 'POST':
        if request.POST['url']:
            url = request.POST['url']
            identifier = str(random.randint(1, 10000000000000))
            new_url = 'https://pacific-ocean-74936.herokuapp.com/main/hash_url/' + identifier
            urls = Urls()
            urls.url = url
            urls.identifier = identifier
            urls.counter = 0
            urls.save()

            return render(request, 'main/hash_url.html', {'url': new_url})
    else:
        return render(request, 'main/hash_url.html')


def check(request):
    if request.method == 'POST':
        if request.POST['url']:
            url = request.POST['url']
            if Urls.objects.get(identifier=url[-13:]):
                urls = Urls.objects.get(identifier=url[-13:])
                return render(request, 'main/check.html', {'url': urls})
        else:
            return render(request, 'main/check.html', {'error': 'Please input something!!!'})
    else:
        return render(request, 'main/check.html')


def hash_url_redirect(request, url_id):
    url = get_object_or_404(Urls, identifier=url_id)
    counter_change = Urls.objects.get(identifier=url_id)
    counter_change.counter += 1
    counter_change.save()
    return redirect(counter_change.url)

