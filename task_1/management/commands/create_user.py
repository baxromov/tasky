from django.core.management.base import BaseCommand

from task_1 import models


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        username = "admin"
        email = "admin@admin.com"
        password = "1"

        models.User.objects.create_superuser(username=username, email=email, password=password)
        print("User:", "\nUsername:", username, "\nPass:", password)
