from django.shortcuts import render
from .models import Title, First, Second, Third, Info

# Create your views here.
def index(request):

    title = Title.objects.filter()
    first = First.objects.filter()
    second = Second.objects.filter()
    third = Third.objects.filter()
    info = Info.objects.filter()


    datas = {
        'title': title,
        'first': first,
        'second': second,
        'third': third,
        'info': info,
    }

    return render(request, 'index.html', datas)

