from django import forms


class LikeForm(forms.Form):
    userid = forms.IntegerField(label="userid")
    postid = forms.IntegerField(label="postid")
