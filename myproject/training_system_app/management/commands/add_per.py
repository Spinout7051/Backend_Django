import random

from django.contrib.auth.models import User, Group
from django.core.management import BaseCommand
from training_system_app.models import UserGroup, Product
from guardian.models import UserObjectPermission


class Command(BaseCommand):
    def handle(self, *args, **options):
        group = Group.objects.get(name='students')
        users = group.user_set.all()
        prods = Product.objects.all()

        for user in users:
            number = random.randint(0, len(prods)-1)
            UserObjectPermission.objects.assign_perm('have_access', user, obj=prods[number])
            print(f'for user {user.username} add have_access to {prods[number].name}')
