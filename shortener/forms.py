from django import forms 


class UrlForm(forms.Form):
    url = forms.URLField(required=True, label="Url to shorten", widget=forms.URLInput(
        attrs={'placeholder': "https://example.com/some/very/long/url?with=some&parameters=true"}
    ))
