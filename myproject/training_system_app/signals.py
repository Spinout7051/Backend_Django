from django.db.models import Count
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import User, Product, UserGroup


@receiver(post_save)
def my_receiver(sender, instance, created, **kwargs):
    if not created:
        return

    try:
        if instance.permission.codename != 'have_access':
            return

        user = User.objects.get(username=instance.user)
        product = Product.objects.get(pk=instance.object_pk)

        groups = UserGroup.objects.filter(product=product).annotate(count=Count('users')).order_by('-count')

        for group in groups:
            if group.count < group.min_users:
                group.users.add(user)
                print(f'в {group.name} добавлен пользователь {user.username}')
                return

        for group in range(len(groups)-1, -1, -1):
            if groups[group].count < groups[group].max_users:
                groups[group].users.add(user)
                print(f'в {groups[group].name} добавлен пользователь {user.username}')
                return

    except AttributeError:
        pass
