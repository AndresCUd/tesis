from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)
    title = forms.CharField(max_length=50)

