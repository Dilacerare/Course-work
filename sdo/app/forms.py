from django import forms

from .models import Hours, Status, Faculty, SpecialtyByCycle, FormsOfTraining, SourcesOfFunding, FormOfEducation, \
    PaymentForm, Cycles


class cycleForm(forms.Form):
    cyc_name = forms.CharField(max_length=200, label='Название')
    begin = forms.DateField(label='Начало')
    end = forms.DateField(label='Окончание')
    cyc_hours = forms.ModelChoiceField(queryset=Hours.objects.all(), label='Часы')
    cyc_status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
    cyc_faculty = forms.ModelChoiceField(queryset=Faculty.objects.all(), label='Кафедра')
    cyc_specialty = forms.ModelChoiceField(queryset=SpecialtyByCycle.objects.all(), label='Специальность по циклу')


class groupForm(forms.Form):
    group_training = forms.ModelChoiceField(queryset=FormsOfTraining.objects.all(), label='Форма обучения')
    group_funding = forms.ModelChoiceField(queryset=SourcesOfFunding.objects.all(), label='Источник финансирования')
    group_education = forms.ModelChoiceField(queryset=FormOfEducation.objects.all(), label='Форма получения образования')
    group_payment = forms.ModelChoiceField(queryset=PaymentForm.objects.all(), label='Форма оплаты')
    group_cycles = forms.ModelChoiceField(queryset=Cycles.objects.all(), label='Цикл')
