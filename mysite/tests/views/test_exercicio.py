import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('exercicio')

    response = client.get(url)
    assert response.status_code == 200
    # espera que retorne um content com hello World
    assert response.content == b'hello world'
