import factory
from faker import Factory as FakerFactory
# objetivo do factory é contruir modelos ja carregados ou pre definidos
# para não precisar criar objetos dentro do arquivo de test

# django disponibiliza modelo de user
from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()

# vai criar um modelo fake do User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # preenche os campos com dados fake
    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(
        lambda x: faker.name())  # faker controi um valor

    # salva o usuario
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
            return user

# gera esses campos, cria dados fakes


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0

    class Meta:
        model = Post
