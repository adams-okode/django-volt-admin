import random

from django.db import transaction
from django.core.management.base import BaseCommand

from test_data.models import Person, Thread, Club, Comment
from test_data.factories import (
    UserFactory,
    ThreadFactory,
    ClubFactory,
    CommentFactory
)

NUM_USERS = 20000
NUM_CLUBS = 5000
NUM_THREADS = 1000
COMMENTS_PER_THREAD = 10
USERS_PER_CLUB = 60

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Person, Thread, Comment, Club]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            people.append(person)

        self.stdout.write("Finished Adding users..")
        # Add some users to clubs
        for _ in range(NUM_CLUBS):
            club = ClubFactory()
            members = random.choices(
                people,
                k=USERS_PER_CLUB
            )
            club.member.add(*members)
        self.stdout.write("Finished Adding Clubs..")
        # Create all the threads
        for _ in range(NUM_THREADS):
            creator = random.choice(people)
            thread = ThreadFactory(creator=creator)
            # Create comments for each thread
            for _ in range(COMMENTS_PER_THREAD):
                commentor = random.choice(people)
                CommentFactory(
                    poster=commentor,
                    thread=thread
                )