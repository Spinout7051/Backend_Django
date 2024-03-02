from django.core.management import BaseCommand
from django.db.models import Count
from training_system_app.models import UserGroup, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = UserGroup.objects.annotate(count=Count('users')).order_by('-count')
        for group in groups:
            print(f'name = {group.name} :: {group.count} :: min={group.min_users} :: max={group.max_users}')
