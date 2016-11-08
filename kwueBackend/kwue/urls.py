from django.conf.urls import url
from kwue.controllers import food
from kwue.controllers import home
from kwue.controllers import tag

urlpatterns = (
    url(r'^search_semantic_tags', tag.search_semantic_tags),

    ### REQUEST
    # 'food_id'
    ### RESPONSE
    # 'serving_weight_grams'
    # 'protein_value'
    # 'calorie_value'
    # 'fiber_value'
    # 'food_owner_id'
    # 'food_recipe'
    # 'food_description'
    # 'food_image'
    # 'food_name'
    # 'fat_value'
    # 'sugar_value'
    # 'food_rate'
    # 'food_id'
    # 'carbonhydrate_value'
    url(r'^get_a_food', food.get_food),


    url(r'^remove_a_food', food.remove_food),

    ### REQUEST
    # 'food_description'
    # 'food_name'
    # 'food_image'
    # 'food_owner'
    # 'food_recipe'
    # 'food_tags'
    ### RESPONSE
    # 'is_success' : if adding food process is successful or not
    # 'reason' : if not successful, the reason of it
    url(r'^add_food', food.add_food),
    url(r'^$', home.get_home),
)