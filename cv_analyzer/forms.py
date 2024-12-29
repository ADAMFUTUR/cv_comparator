from django import forms
from .models import CV, JobRequirement

class CVUploadForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'title', 'skills', 'experience', 'education', 'file']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter candidate name',
                'required': True
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter current or desired job title',
                'required': True
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List key skills (e.g., Python, Project Management, Leadership)',
                'rows': 4,
                'required': True
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Years of experience',
                'min': '0',
                'required': True
            }),
            'education': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Educational background and qualifications',
                'rows': 3,
                'required': True
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
                'required': True
            })
        }
        help_texts = {
            'skills': 'Separate skills with commas',
            'file': 'Accepted formats: PDF, DOC, DOCX'
        }

class JobRequirementForm(forms.ModelForm):
    class Meta:
        model = JobRequirement
        fields = ['title', 'required_skills']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the job title',
                'required': True
            }),
            'required_skills': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List required skills (e.g., Python, Project Management, Leadership)',
                'rows': 4,
                'required': True
            })
        }
        help_texts = {
            'required_skills': 'Separate skills with commas. The more specific you are, the better the matching will be.'
        }
