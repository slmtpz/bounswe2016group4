from django.shortcuts import render
from kwue.DB_functions.food_db_functions import *

def get_home(req):
    food = db_retrieve_all_foods()
    user_dict = req.POST.dict()
    req.session['user_id'] = -2

    req.session['username'] = 'doruk1994'
    print(req.session['username']+ " has been authenticated")
    return render(req, 'kwue/home.html', {'foods': food})