from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command inserts category data"

    def handle(self, *args, **options):
        # Deleting existing data
        Category.objects.all().delete()

        categories = ["Sports ", "Gaming", "Studying", "Playing", "Reading"]

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))
