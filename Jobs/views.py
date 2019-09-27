from django.shortcuts import render
from faker import Faker
from .models import Person
from decouple import config
# Create your views here.


def index(request):
    return render(request, 'Jobs/index.html')


def jobs(request):
    a = request.POST.get('name')
    b = Person.objects.filter(name=a)
    if b:
        c = b[0].job
    else:
        faker = Faker('ko_KR')
        c = faker.job()
        p = Person()
        p.name = a
        p.job = c
        p.save()
# 직업 결과에 따라 giphy 호출
    api_key = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={c}&lang=en'
    import requests
    response = requests.get(url).json()
    try:
        image_url = response['data'][0].get('images').get('original').get('url')
    except:
        image_url = None
    context = {
        'name': a,
        'job': c,
        'url': image_url
    }
    return render(request, 'Jobs/job.html', context)


def l_admin(request):
    return render(request, 'Jobs/l_admin.html')


def main(request):
    i_pwd = request.GET.get('pwd')
    if i_pwd == '12345':
        a = Person.objects.all()
        context = {
            'a': a
        }
        return render(request, 'Jobs/list.html', context)
    else:
        return render(request, 'Jobs/wrong.html')
