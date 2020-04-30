from django.contrib import admin
from myapp.models import contact, Hightlight , Hobbies , project , skills , about_you,Personal_info,profile
# Register your models here.
admin.site.register(contact)
admin.site.register(Hightlight)
admin.site.register(Hobbies)
admin.site.register(project)
admin.site.register(skills)
admin.site.register(about_you)
admin.site.register(Personal_info)
admin.site.register(profile)