from django.contrib import admin

# Register your models here.
from .models import chat

class chatAdmin(admin.ModelAdmin):
	class Meta:
		model = chat

admin.site.register(chat, chatAdmin)
