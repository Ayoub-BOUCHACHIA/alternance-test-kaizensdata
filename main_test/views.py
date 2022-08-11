from django.shortcuts import render

# Create your views here.


from .backend import extracing
# Create your views here.
from .utils import get_cnx_database

def home(request):
    print("get connection ...")
    db = get_cnx_database()
    print("connection etablished")

    hashtag = "harassment"
    print(hashtag)
    
    descriptions = extracing(hashtag)
    print("len of description : ",len(descriptions))
    
    for description in descriptions:
        instance = {
            "description" : description,
        }

        db["harassment"].insert_one(instance)


    return render(request, 'main_test/index.html', context={
        'data' : descriptions
    })