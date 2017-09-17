from django import forms

from docmanager.models import *

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['ISBN', 'title', 'description', 'doc_type']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['release_date'] = forms.DateField()
        self.fields['author'] = forms.ModelChoiceField( \
            queryset=Author.objects.all())
        self.fields['doc_type'] = forms.ChoiceField( \
            choices=Document._meta.get_field('doc_type').choices)
