import pytest
from django.urls import reverse

# criando um pytest


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    # vai pegar 1 e não uma lista
    response = client.get(url)
    # espero que seja 200 ( OK )
    assert response.status_code == 200
    # espera que retorne um content com hello, World!
    assert response.content == b'Hello, World!'
