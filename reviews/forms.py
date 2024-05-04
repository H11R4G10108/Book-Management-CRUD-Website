from django import forms
from .models import Book, Publisher, Review


class PublisherForm(forms.ModelForm):
 class Meta:
  model = Publisher
  fields = "__all__"
BOOK_CHOICES =(
    ("title", "Title"),
    ("contributor", "Contributor"))
class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=BOOK_CHOICES)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]
    rating = forms.IntegerField(min_value=0, max_value=5)


class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["title", "publication_date", "isbn", "publisher","contributors"]
    cover = forms.ImageField(required=False)
    sample = forms.FileField(required=False)
