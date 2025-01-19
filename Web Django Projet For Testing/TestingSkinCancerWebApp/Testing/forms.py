from django import forms

class PredictionForm(forms.Form):
    image = forms.ImageField(label='Image')
    age = forms.FloatField(label='Âge')
    location = forms.ChoiceField(
        label='Localisation',
        choices=[
            ('face', 'Visage'),
            ('scalp', 'Cuir chevelu'),
            ('neck', 'Cou'),
            ('trunk', 'Tronc'),
            ('hand', 'Main'),
            ('foot', 'Pied'),
            ('back', 'Dos'),
            ('chest', 'Poitrine'),
            ('ear', 'Oreille'),
            ('genital', 'Zone génitale'),
            ('lower extremity', 'Membre inférieur'),
            ('upper extremity', 'Membre supérieur'),
        ]
    )