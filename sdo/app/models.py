from django.db import models


class Roles(models.Model):
    role = models.CharField('Роль', max_length=200)

    def __str__(self):
        return self.role


class Genders(models.Model):
    gender = models.CharField('Пол', max_length=200)

    def __str__(self):
        return self.gender


class Users(models.Model):
    surname = models.CharField('Фамилия', max_length=200)
    name = models.CharField('Имя', max_length=200)
    patronymic = models.CharField('Отчество', max_length=200)
    login = models.CharField('Логин', max_length=200)
    ur_email = models.EmailField('Эл. почта', max_length=200)
    password = models.CharField('Пароль', max_length=200)
    BDay = models.DateField('День рождения')
    ur_role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    ur_gender = models.ForeignKey(Genders, on_delete=models.CASCADE)

    def __str__(self):
        return self.login


class Hours(models.Model):
    hour = models.CharField('Ко-во часов', max_length=200)

    def __str__(self):
        return self.hour


class Status(models.Model):
    status = models.CharField('Статус цикла', max_length=200)

    def __str__(self):
        return self.status


class Faculty(models.Model):
    faculty = models.CharField('Кафедра', max_length=200)

    def __str__(self):
        return self.faculty


class SpecialtyByCycle(models.Model):
    specialty_by_cycle = models.CharField('Специальность по циклу', max_length=200)

    def __str__(self):
        return self.specialty_by_cycle


class Cycles(models.Model):
    cyc_name = models.CharField('Название', max_length=200)
    begin = models.DateField('Начало')
    end = models.DateField('Окончание')
    cyc_hours = models.ForeignKey(Hours, on_delete=models.CASCADE)
    cyc_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    cyc_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    cyc_specialty = models.ForeignKey(SpecialtyByCycle, on_delete=models.CASCADE)

    def __str__(self):
        return self.cyc_name


class FormsOfTraining(models.Model):
    forms_of_training = models.CharField('Форма обучения', max_length=200)

    def __str__(self):
        return self.forms_of_training


class SourcesOfFunding(models.Model):
    sources_of_funding = models.CharField('Источник финансирования', max_length=200)

    def __str__(self):
        return self.sources_of_funding


class FormOfEducation(models.Model):
    form_of_education = models.CharField('Форма получения образования', max_length=200)

    def __str__(self):
        return self.form_of_education


class PaymentForm(models.Model):
    payment_form = models.CharField('Форма оплаты', max_length=200)

    def __str__(self):
        return self.payment_form


class Groups(models.Model):
    group_training = models.ForeignKey(FormsOfTraining, on_delete=models.CASCADE)
    group_funding = models.ForeignKey(SourcesOfFunding, on_delete=models.CASCADE)
    group_education = models.ForeignKey(FormOfEducation, on_delete=models.CASCADE)
    group_payment = models.ForeignKey(PaymentForm, on_delete=models.CASCADE)
    group_cycles = models.ForeignKey(Cycles, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.group_cycles


class Positions(models.Model):
    position = models.CharField('Должность', max_length=200)

    def __str__(self):
        return self.position


class Specializations(models.Model):
    specialization = models.CharField('Специальность', max_length=200)

    def __str__(self):
        return self.specialization


class Students(models.Model):
    diploma_surname = models.CharField('Фамилия в дипломе', max_length=200)
    diploma_series = models.CharField('Серия диплома', max_length=200)
    diploma_number = models.CharField('Номер диплома', max_length=200)
    identity_series = models.CharField('Серия удостоверение', max_length=200)
    identity_number = models.CharField('Номер удостоверение', max_length=200)
    place_of_work = models.CharField('Место работы (нас. пункт)', max_length=200)
    job = models.CharField('Работа (организация)', max_length=200)
    snils = models.CharField('СНИЛС', max_length=200)
    citizenship = models.CharField('Гражданство (код страны)', max_length=200)
    payment_status = models.CharField('Состояние оплаты', max_length=200)
    disability = models.CharField('Инвалидность', max_length=200)
    student_group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    student_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    student_position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    student_specialization = models.ForeignKey(Specializations, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
