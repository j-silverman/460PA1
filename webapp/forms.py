from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from webapp.models import Photos, Album, Comment, Tag

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 30)
    home_town = forms.CharField(max_length= 20)
    gender = forms.CharField(max_length=1)
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','home_town','gender','date_of_birth','password1','password2')

class PhotoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album_id'].queryset = Album.objects.filter(a_author=user)
    
    class Meta:
        model = Photos
        fields = ('caption','photo_data','album_id')
        
        
        
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name']
        
    #def __init__(self, *args, **kwargs):
     #   super(AlbumForm, self).__init__(*args, **kwargs)
      #  self.fields['photo_id'].queryset = Photos.objects.filter(
       #         author_id = User.objects.get_by_natural_key)
                   
#class AddAlbum(forms.ModelForm):
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        
        
        
class LoggedInCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag_text',)
        
