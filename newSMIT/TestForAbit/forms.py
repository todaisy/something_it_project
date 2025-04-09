from django import forms

class MyRadioForm(forms.Form):
    def __init__(self, lst, lbl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем поле в словарь fields формы
        self.fields['option'] = forms.ChoiceField(
            widget=forms.RadioSelect,
            label=lbl,
            choices=lst,
        )