from kwue.models.models import IngredientModel


def db_insert_ingredient(ingredient_name):
    try:
        ingredient_name = ingredient_name.strip()
        if ingredient_name is None:
            return False
        if ingredient_name is '':
            return False
        new_object = IngredientModel(
            ingredient_name=ingredient_name
                 )
        new_object.save()
        return new_object
    except:
        return False


def db_retrieve_ingredient(ingredient_name):
    try:
        if ingredient_name is None:
            return False
        if ingredient_name is '':
            return False
        return IngredientModel.objects.get(ingredient_name__iexact=ingredient_name)
    except:
        return False