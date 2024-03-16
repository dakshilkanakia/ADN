from django import forms
from .models import Apparel

#add a form to add new apparel

class AddApparelForm(forms.ModelForm):
    
    # id is the primary key and should be autoincremented
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))  
    subcategory = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    object_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    designer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    label = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    basic_color = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    color_subcategory = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    hexcodes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    condition = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    material = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sale_location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sale_date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 

    class Meta:
        model = Apparel
        fields = ['title','category','subcategory','object_date','designer','label','description','basic_color','color_subcategory','hexcodes','condition','material','price','sale_location','sale_date']
        