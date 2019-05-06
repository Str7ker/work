from django.contrib import admin
from .models import Company, Position, Personal, Rating

admin.site.register(Company)
# class Companyadmin(admin.ModelAdmin):
#     pass
admin.site.register(Position)
admin.site.register(Personal)
admin.site.register(Rating)
