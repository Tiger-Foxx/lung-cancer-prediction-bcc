import os
import tempfile
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .utils import predict_bcc  # Votre fonction de prédiction

@ensure_csrf_cookie
def home(request):
    return render(request, 'predict.html')

def predict(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Récupération des données
            image = request.FILES['image']
            age = float(request.POST.get('age'))
            location = request.POST.get('location')

            # Sauvegarde temporaire de l'image
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                for chunk in image.chunks():
                    tmp.write(chunk)
                temp_path = tmp.name

            try:
                # Appel à votre fonction de prédiction
                results = predict_bcc(
                    chemin_image=temp_path,
                    age=age,
                    localisation=location,
                    taille="28x28",
                    type_modele="all"
                )

                return JsonResponse({
                    'success': True,
                    'results': results
                })
            finally:
                # Nettoyage du fichier temporaire
                os.unlink(temp_path)

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

    return JsonResponse({
        'success': False,
        'error': 'Méthode non autorisée ou données manquantes'
    })