from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Lesson, Product, UserGroup


@admin.register(Lesson)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'product', 'name', 'video_link'


@admin.register(UserGroup)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'product', 'name', 'min_users', 'max_users'


class ProductAdmin(GuardedModelAdmin):
    list_display = 'pk', 'creator', 'name', 'start_date_time', 'price'


admin.site.register(Product, ProductAdmin)
