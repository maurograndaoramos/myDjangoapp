from django import forms

class CategoryForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    new_category = forms.CharField(label='New Category')
