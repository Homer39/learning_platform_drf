from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user2@sky.pro',
            first_name='user2',
            last_name='Learning_platform',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('1234')
        user.save()
