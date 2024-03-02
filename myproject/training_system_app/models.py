from django.db import models
from django.contrib.auth.models import User, Group


class Product(models.Model):
    creator = models.ForeignKey(User, default=None, null=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    start_date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)

    class Meta:
        permissions = (
            ('have_access', 'Есть доступ к продукту'),
        )


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    video_link = models.URLField()

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, default=None, null=True, related_name='user_groups')
    min_users = models.PositiveIntegerField(default=5)
    max_users = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name
