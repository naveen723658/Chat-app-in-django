from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = user
    list_display = ['pk','username', 'email' ,'is_active']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ('avatar', 'email', 'first_name', 'last_name')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (('Documents'), {'fields': ('avatar',)}),
    )
admin.site.register(user, CustomUserAdmin)



admin.site.register(ChatMessage)
class ChatMessage(admin.TabularInline):
    model = ChatMessage



# class ThreadForm(forms.ModelForm):
#     def clean(self):
#         """
#         This is the function that can be used to
#         validate your model data from admin
#         """
#         super(ThreadForm, self).clean()
#         first_person = self.cleaned_data.get('first_person')
#         second_person = self.cleaned_data.get('second_person')
#
#         lookup1 = Q(first_person=first_person) & Q(second_person=second_person)
#         lookup2 = Q(first_person=second_person) & Q(second_person=first_person)
#         lookup = Q(lookup1 | lookup2)
#         qs = Thread.objects.filter(lookup)
#         if qs.exists():
#             raise ValidationError(f'Thread between {first_person} and {second_person} already exists.')
#


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)