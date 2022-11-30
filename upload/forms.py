from django.forms import ModelForm  
from .models import FileModel

class UploadForm(ModelForm):
    
    class Meta:
        model = FileModel
        fields = ['upload']