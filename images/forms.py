from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
	class Meta:
		model=Image
		fields=('title','url','description')
		widgets={
				'url':forms.HiddenInput,
		}

	def clean_url(self):
		url=self.cleaned_data['url']
		valid_extensions=['jpg','jpeg']
		extensions=url.rsplit('.',1)[1].lower()
		if extensionsnot in valid_extensions:
			raise forms.ValidationError('the url does not'\
										'match valid image extensions')
		return url