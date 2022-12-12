from recipesweb_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are defined correctly
    """
    recipe = Recipe('Paella', 'Rice, Chicken, Saffron', 'Fry the chicken, Add Saffron, Add the rice, Boil everything', 4, True)
    assert recipe.name == 'Paella'
    assert recipe.ingredients == 'Rice, Chicken, Saffron'
    assert recipe.steps == 'Fry the chicken, Add Saffron, Add the rice, Boil everything'
    assert recipe.rating == 4
    assert recipe.favorite == True