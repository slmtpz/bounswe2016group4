from kwue.models.models import *


def db_insert_food(food_tuple):
    new_food = FoodModel(
        food_description=food_tuple[0],
        food_name=food_tuple[1],
        food_image=food_tuple[2],
        food_owner=food_tuple[3]
    )
    try:
        FoodModel.save(new_food)
        return True
    except:
        return False


def db_retrieve_food(food_id):
    food = FoodModel.objects.get(food_id=food_id)
    return food


def db_delete_food(food_id):
    food = FoodModel.objects.filter(food_id=food_id)
    try:
        food.delete()
        return True
    except:
        return False


def db_update_food(food_id, food_tuple):
    try:
        FoodModel.objects.filter(food_id=food_id).update(
            food_description=food_tuple[0],
            food_name=food_tuple[1],
            food_image=food_tuple[2],
            food_owner=food_tuple[3]
        )
        return False
    except:
        return True


def db_up_rate_food(food_id):
    try:
        rate = FoodModel.objects.get(food_id=food_id).food_rate
        rate += 1
        FoodModel.objects.filter(food_id=food_id).update(food_rate=rate)
        return True
    except:
        return False


def db_down_rate_food(food_id):
    try:
        rate = FoodModel.objects.get(food_id=food_id).food_rate
        rate -= 1
        FoodModel.objects.filter(food_id=food_id).update(food_rate=rate)
        return True
    except:
        return False
