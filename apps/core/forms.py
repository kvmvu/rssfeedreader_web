from django import forms


class Form(forms.Form):
    rss_feed_url = forms.URLField(label='Feed URL')
