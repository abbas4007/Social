from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	phone_number = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

	# def clean_phone_number(self):
	# 	phone_number = self.cleaned_data['phone_number']
	# 	user = User.objects.filter(phone_number=phone_number).exists()
	# 	if user:
	# 		raise ValidationError('this phone_number already existing')
	# 	return phone_number

	def clean(self):
		cd=super().clean()
		p1 = cd.get('password1')
		p2 = cd.get('password2')

		if p1 and p2 and p1 != p2:
			raise ValidationError('password must match')
    
	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class EditUserForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Profile
		fields = ('age', 'bio')
