from django import forms
from .models import Squad

class SquadUploadForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ('squad_file')
