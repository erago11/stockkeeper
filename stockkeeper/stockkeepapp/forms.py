from django import forms
from .models import Stock

class StockSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['code']

class StockResultForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(StockResultForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
