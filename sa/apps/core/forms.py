from django import forms

from sa.apps.core.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'span8'
        self.fields['body_type'].widget.attrs['class'] = 'span4'
        self.fields['transmission'].widget.attrs['class'] = 'span4'
        self.fields['drive'].widget.attrs['class'] = 'span4'
        self.fields['engine'].widget.attrs['class'] = 'span2'
        self.fields['price'].widget.attrs['class'] = 'span2'
