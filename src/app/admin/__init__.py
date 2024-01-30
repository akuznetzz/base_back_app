from django.contrib import admin

from app.admin.PersonAdmin import PersonAdmin
from app.models import User
# from app.models.person import Person

admin.site.register(User)
# admin.site.register(Person, PersonAdmin)