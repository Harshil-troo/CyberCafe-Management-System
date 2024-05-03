from django import forms
from .models import User,Reservation

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','name', 'id_proof', 'id_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["username"].widget.attrs['placeholder'] = 'User Name...'
        self.fields["name"].widget.attrs['class'] = 'form-control'
        self.fields["name"].widget.attrs['placeholder'] = 'Customer Name...'
        self.fields["id_proof"].widget.attrs['class'] = 'form-control'
        self.fields["id_number"].widget.attrs['class'] = 'form-control'
        self.fields["id_number"].widget.attrs['placeholder'] = 'ID Number..'




class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'computer_name', 'start_time', 'end_time']
        widgets = {
            'yes_or_no': forms.DateTimeInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["user"].widget.attrs['class'] = 'form-control'
        self.fields["computer_name"].widget.attrs['class'] = 'form-control'
        self.fields["start_time"].widget.attrs['class'] = 'form-control'
        self.fields["start_time"].widget.attrs['placeholder'] = 'Start Time...'
        self.fields["end_time"].widget.attrs['class'] = 'form-control'
        self.fields["end_time"].widget.attrs['placeholder'] = 'End Time...'

