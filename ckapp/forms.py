from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Product
class ProductCreationForm(forms.ModelForm):

    # long_description = forms.CharField(widget=CKEditorWidget())

    long_description = forms.TextInput()

    class Meta:
        model = Product
        fields = ['product_name', 'long_description', 'description']

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'long_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductCreationForm, self).__init__(*args, **kwargs)
        # self.fields['product_name'].widget.attrs.update({'class' : 'form-control', 'placeholder': '', 'autocomplete':'off'})
        # self.fields['description'].widget.attrs.update({'class' : 'form-control', 'autocomplete':'off'})