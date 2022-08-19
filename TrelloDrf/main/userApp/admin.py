from django.contrib import admin
from userApp.models import CustomUser

admin.site.register(CustomUser)


class CustomUserAdmin(admin.ModelAdmin):

    class Meta:
        model = CustomUser
        fields = '__all__'
