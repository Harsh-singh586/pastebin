from django import forms

class text(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs.update({'class':'form-control', 'rows':'20'})

