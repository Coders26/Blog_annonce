from django.shortcuts import render
from . import models
from .models import Message, Info, Contact

# Create your views here.
def contact(request):
    message = Message.objects.filter()
    info = Info.objects.filter()

    if request.method == 'POST':
        contact = models.Contact()
        nom = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contenu = request.POST.get('message')

        contact.nom = nom
        contact.email = email
        contact.phone = phone
        contact.contenus = contenu
        contact.save()

    datas = {
        'message': message,
        'info': info,
    }

    return render(request, 'contact.html', datas)
