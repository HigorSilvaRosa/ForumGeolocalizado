import json
from dajaxice.decorators import dajaxice_register
from django.db.models.query_utils import Q
from core.models import UserCoordinates, Topic

__author__ = 'higorsilvarosa'

@dajaxice_register(method='POST')
def save_user_coordinates(request, latitude, longitude):
    response = {"ok": False}
    if request.user.is_authenticated() and latitude and longitude:
        user_coordinates = UserCoordinates(user=request.user, latitude=latitude, longitude=longitude)
        user_coordinates.save()
        request.session["coordinates"] = (latitude, longitude)
        response["ok"] = True
    return json.dumps(response)

@dajaxice_register(method='POST')
def get_near_topics(request, latitude, longitude):
    response = {"ok": False,
                "topics": []}
    if latitude and longitude:
        topics = Topic.objects.filter(Q(latitude__gte=(latitude-0.5)) | Q(longitude__gte=(longitude-0.5)))
        topics = topics.exclude(Q(latitude__gte=(latitude+0.5)) | Q(longitude__gte=(longitude+0.5)))
        response = {"ok": True}
        topics_response = []
        for topic in topics:
            topics_response.append({
                "id":topic.id,
                "name":topic.name,
                "user":topic.user.username,
                "latitude":topic.latitude,
                "longitude":topic.longitude
            })
        response['topics'] = topics_response
    return json.dumps(response)