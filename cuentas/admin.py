from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioPersCreationForm, UsuarioPersChangeForm
from .models import UsuarioPers

class UsuarioPersAdmin(UserAdmin):
    add_form = UsuarioPersCreationForm
    form = UsuarioPersChangeForm
    model = UsuarioPers

admin.site.register(UsuarioPers, UsuarioPersAdmin)