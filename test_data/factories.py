# factories.py
import factory
from factory.django import DjangoModelFactory

from test_data.models import Person, Thread, Comment, Club
# Defining a factory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = Person
    name = factory.Faker("first_name")


class ThreadFactory(DjangoModelFactory):
    class Meta:
        model = Thread

    title = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    creator = factory.SubFactory(UserFactory)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    body = factory.Faker("sentence", nb_words=15, variable_nb_words=True)
    poster = factory.SubFactory(UserFactory)
    thread = factory.SubFactory(ThreadFactory)


class ClubFactory(DjangoModelFactory):
    class Meta:
        model = Club
    name = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    # member = factory.SubFactory(UserFactory)
