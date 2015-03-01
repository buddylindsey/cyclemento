from django import forms

from .models import Maintenance


class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        fields = ['description', 'place', 'gear', 'activity']
        widgets = {
            'activity': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MaintenanceForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['gear'].choices = user.gear.order_by(
                'primary').values_list('id', 'name')
            self.fields['activity'].initial = user.activties.latest().id

    def save(self, commit=True):
        maintenance = super(MaintenanceForm, self).save(commit=False)
        gear = self.cleaned_data['gear']
        maintenance.distance = gear.distance_since_last_maintenance()
        maintenance.distance_unit = Maintenance.DISTANCE_UNITS.mi

        if commit:
            maintenance.save()

        return maintenance

