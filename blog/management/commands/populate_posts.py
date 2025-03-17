from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args, **options):
        # Deleting existing data
        Post.objects.all().delete()

        titles = [
            "Reading is Fun",
            "Football is Passion",
            "Music is Life",
            "Traveling is Adventure",
            "Dancing is Joy",
            "Swimming is Refreshing",
            "Exercise is Health",
            "Coding is Creativity",
            "Gaming is Awesome",
            "Singing is Expression",
            "Writing is Art",
            "Learning is Growth",
            "Photography is Good",
            "Meditation is Peace",
            "Cycling is Freedom",
            "Movies are Escapism",
            "Gardening is Therapy",
            "Painting is Relaxation",
            "Technology is Nice",
            "Friendship is Strength",
        ]

        contents = [
            "Reading opens the doors to imagination and knowledge.\nIt helps expand vocabulary and understanding.",
            "Football is more than a sport; it's teamwork and strategy.\nIt builds endurance, skill, and discipline.",
            "Music soothes the soul and lifts the spirit.\nIt expresses emotions beyond words.",
            "Traveling introduces new cultures and experiences.\nIt broadens perspectives and refreshes the mind.",
            "Dancing is an art of movement and rhythm.\nIt brings joy, energy, and fitness.",
            "Swimming is a great full-body workout.\nIt keeps you active and improves lung capacity.",
            "Exercise is key to a healthy life.\nIt strengthens the body and boosts mental well-being.",
            "Coding is a blend of logic and creativity.\nIt helps solve problems and build innovative solutions.",
            "Gaming improves reflexes and strategic thinking.\nIt can be fun and educational at the same time.",
            "Singing is a way to express feelings.\nIt enhances mood and breathing techniques.",
            "Writing turns thoughts into stories.\nIt sharpens creativity and communication skills.",
            "Learning is a continuous journey.\nIt fuels curiosity and personal growth.",
            "Photography captures moments forever.\nIt tells stories without words.",
            "Meditation calms the mind and soul.\nIt improves focus and inner peace.",
            "Cycling is a fun way to stay fit.\nIt strengthens the heart and muscles.",
            "Movies take you into different worlds.\nThey provide entertainment and inspiration.",
            "Gardening connects you with nature.\nIt teaches patience and care.",
            "Painting is a form of self-expression.\nIt brings relaxation and creativity.",
            "Technology drives innovation.\nIt makes life easier and more efficient.",
            "Friendship is a treasure of life.\nIt provides support and happiness.",
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(
                title=title, content=content, img_url=img_url, category_id=category.id
            )

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))
