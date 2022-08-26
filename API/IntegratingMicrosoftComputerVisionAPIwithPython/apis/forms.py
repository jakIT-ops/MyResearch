from django import forms
from django.forms import widgets 
from .models import Key_Endpoint, OCR, ImageAnalysis2

class OCRForm(forms.ModelForm): 
    class Meta:
        model = OCR
        fields = ['image_url']

class ImageAnalysis2Form(forms.ModelForm): 
    
    ANALYSIS_CHOICES = (
        ("DESCRIPTION", "Description"),
        ("CATEGORY", "Category"),
        ("TAG", "Tag"),
        ("OBJECT", "Detect Object"),
        ("BRAND", "Detect Popular Brand"),
        ("FACES", "Detect Faces"),
        ("ADULT", "Detect Adult, Racy, or Gory Content"),
        ("COLOR","Color Schemes in Images"),
        ("CELEBRITIES","Detect Celebrities"),
        ("LANDMARK","Detect Landmarks"),
        ("TYPE","Detect Image Type")
    )
    select = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=ANALYSIS_CHOICES)
    class Meta:
        model = ImageAnalysis2
        fields = ['image_url']