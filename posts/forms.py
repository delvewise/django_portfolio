from django import forms
from .models import Post, Comment




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )

# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)
# 
#     # def send_email(self):
#     #     #later
#     #     pass
