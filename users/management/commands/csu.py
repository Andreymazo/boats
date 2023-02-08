from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        u = User.objects.create(
            email='newadmin@mymail.com',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        u.set_password('123qwe456rty')
        u.save()
