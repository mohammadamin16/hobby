from django import forms
from .imdbDB import search


class SearchForm(forms.Form):
    query = forms.CharField(label='Search',widget=forms.TextInput(attrs={'placeholder': 'Type a movie title in english'}))

    def send_query(self):
        q = self.cleaned_data['query']

        return search.search(q)

