from django.shortcuts import render
from .models import First, Second, Third, Fourth, Plus, Info

# Create your views here.
def about(request):

    first = First.objects.filter()
    second = Second.objects.filter()
    third = Third.objects.filter()
    fourth = Fourth.objects.filter()
    plus = Plus.objects.filter
    info = Info.objects.filter()

    datas = {
        'first': first,
        'second': second,
        'third': third,
        'fourth': fourth,
        'plus': plus,
        'info': info,
    }
    return render(request, 'about.html', datas)