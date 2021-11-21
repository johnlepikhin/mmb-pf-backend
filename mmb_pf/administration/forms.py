from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)

from .models import MainMenu, MMBPFGroups, MMBPFUsers, SystemSettings


class MMBPFUsersAdminPasswordChangeForm(AdminPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MMBPFUsersForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "password" in self.fields:
            self.fields[
                "password"
            ].help_text = '<h3><a class="h3" href="../password/">Принудительная смена пароля пользователя </a></h3>'

    def clean(self):
        if "groups" in self.cleaned_data and not len(self.cleaned_data.get("groups")):
            raise forms.ValidationError("Пользователь должен быть включён хотя бы в одну группу")

        return self.cleaned_data

    class Meta(UserChangeForm):
        model = MMBPFUsers
        fields = "__all__"


class MMBPFUsersCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MMBPFUsersCreationForm, self).__init__(*args, **kwargs)

    def clean(self):
        if "groups" in self.cleaned_data and not len(self.cleaned_data.get("groups")):
            raise forms.ValidationError("Пользователь должен быть включён хотя бы в одну группу")

        return self.cleaned_data

    class Meta(UserCreationForm):
        model = MMBPFUsers
        fields = "__all__"


class SystemSettingsCreationForm(forms.ModelForm):
    class Meta:
        model = SystemSettings
        fields = "__all__"


class SystemSettingsForm(forms.ModelForm):
    def clean(self):
        return self.cleaned_data

    class Meta:
        model = SystemSettings
        fields = "__all__"
