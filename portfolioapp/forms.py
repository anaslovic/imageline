from django import forms
from .models import Photo, Category, Portfolio, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'portfolio', 'category','title','description','camera_name','lens','used_light')

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}),
            'portfolio': forms.TextInput(attrs={'class': 'form-control', 'id': 'portfolio', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'id': 'category'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'}),
            'camera_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'camera_name'}),
            'lens': forms.TextInput(attrs={'class': 'form-control', 'id': 'lens'}),
            'used_light': forms.Select(attrs={'class': 'form-control', 'id': 'used_light'}),
        }


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title','description', 'category','camera_name', 'lens', 'used_light')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'id': 'category'}),
            'camera_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'camera_name'}),
            'lens': forms.TextInput(attrs={'class': 'form-control', 'id': 'lens'}),
            'used_light': forms.Select(attrs={'class': 'form-control', 'id': 'used_light'}),
        }


class UpdatePortfolioInfoForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('artistic_name','profile_pic','cover_image','bio','location')

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'id': 'profile_pic'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control', 'id': 'cover_image'}),
            'artistic_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'artistic_name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'id': 'bio'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'location'}),
        }

        labels = {
            'profile_pic': 'Profile image',
            'cover_image': 'Cover image',
            'artistic_name': 'Artistic name',
            'bio': 'Biography',
            'location': 'Location',
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'photo', 'body')

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'photo': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'photo', 'value': '', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'body', 'style': 'height:80px;'}),
        }

        labels = {
            'body':'Add Comment'
        }

