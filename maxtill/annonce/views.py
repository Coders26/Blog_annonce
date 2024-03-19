from django.shortcuts import render, redirect
from .models import Info, Annonce, Commentaire

# Create your views here.
def annonce(request):
    annonce = Annonce.objects.filter()
    info = Info.objects.filter()

    datas = {

        'info': info,
        'annonce': annonce
    }

    return render(request, 'annonce.html', datas)

def annonce_single(request, pk):
    annonce = Annonce.objects.get(id=pk)
    info = Info.objects.filter()
    if request.POST:
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')
        commentaire = Commentaire()
        commentaire.nom = name
        commentaire.annonce = annonce
        commentaire.commentaire = comment
        commentaire.save()

    datas = {
        'info': info,
        'annonce': annonce
    }
    return render(request, 'annonce_single.html', datas)


def new_annonce(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        contenu = request.POST.get('contenu')

        # Enregistrer l'annonce dans la base de données
        annonce = Annonce(title=title, image=image, description=description, contenu=contenu)
        annonce.save()

        return redirect('annonce')  # Redirection vers la page des annonces après avoir ajouté une nouvelle annonce

    return render(request, 'new_annonce.html')
