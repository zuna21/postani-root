from django.forms import ModelForm
from .models import Article, Comment, Reply

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        labels = {
            'body': 'Ostavite svoj komentar...'
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']

        labels = {
            'body': 'Odgovorite...'
        }