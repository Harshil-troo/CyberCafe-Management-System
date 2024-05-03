from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'processor', 'ram', 'operating_system','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["computer_name"].widget.attrs['class'] = 'form-control'
        self.fields["computer_name"].widget.attrs['placeholder'] = 'Computer Name...'
        self.fields["processor"].widget.attrs['class'] = 'form-control'
        self.fields["processor"].widget.attrs['placeholder'] = 'Processor...'
        self.fields["ram"].widget.attrs['class'] = 'form-control'
        self.fields["ram"].widget.attrs['placeholder'] = 'RAM(GB)'
        self.fields["operating_system"].widget.attrs['class'] = 'form-control'
        self.fields["operating_system"].widget.attrs['placeholder'] = 'Operating System..'
        self.fields["status"].widget.attrs['class'] = 'form-control'
