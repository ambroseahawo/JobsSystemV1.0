from django import forms
from django.contrib.auth.models import User
from users.models import Account, Experience, Industry, Education, Skill

class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['headline', 'country', 'interests', 'summary']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['position', 'role']


class InterestsForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['interests']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'grade', 'activities']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'about']