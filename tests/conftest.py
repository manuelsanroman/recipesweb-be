import pytest
from recipesweb_api.models import Recipe
from recipesweb_api import db, app

@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('Test Recipe', 'Ingredient1, Ingredient2', 'Step1, Step2', 3, False)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()