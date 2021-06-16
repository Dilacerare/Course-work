from django.contrib import admin
from .models import Users, Cycles, Groups, Students, Roles, Genders, Hours, Status, Faculty, SpecialtyByCycle, \
    FormsOfTraining, SourcesOfFunding, FormOfEducation, PaymentForm, Positions, Specializations

admin.site.register(Users)
admin.site.register(Cycles)
admin.site.register(Groups)
admin.site.register(Students)
admin.site.register(Roles)
admin.site.register(Genders)
admin.site.register(Hours)
admin.site.register(Status)
admin.site.register(Faculty)
admin.site.register(SpecialtyByCycle)
admin.site.register(FormsOfTraining)
admin.site.register(SourcesOfFunding)
admin.site.register(FormOfEducation)
admin.site.register(PaymentForm)
admin.site.register(Positions)
admin.site.register(Specializations)
