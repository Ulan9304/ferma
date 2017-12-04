# coding=utf-8
from django import forms

from adverts.models import CreateNewAdvert


class CreateNewAdvertForm(forms.ModelForm):
    images = forms.CharField(widget=forms.TextInput(attrs={'style': 'display: none;'})
                             , required=False)
    removed_images = forms.CharField(widget=forms.TextInput(attrs={'style': 'display: none;'})
                                     , required=False)

    class Meta:
        model = CreateNewAdvert
        fields = ('name',
                  'email',
                  'title',
                  'advert_type',
                  'categories',
                  'agree_with_rules',
                  'text',
                  'removed_images',
                  'images')

    def __init__(self, *args, **kwargs):
        super(CreateNewAdvertForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'id': 'ad_text', 'style': 'width:100%'})
