import os
import falcon
import datetime
from app.models import UserProfile
from .base import BaseResource


def process_players_stat(query):
    days_total = datetime.datetime.now() - datetime.datetime.strptime(query.get("created_at"), "%Y-%m-%d %H:%M:%S.%f")
    rating = query.get("battles_total") / max(days_total.days, 1)
    exp_avg = query.get("exp_total", 0) / max(days_total.days, 1)
    query.update({
        'days_total': days_total.days,
        'rating': rating,
        'exp_avg': exp_avg,
    })
    return query


class Users(BaseResource):
    """Processing request for '/users/' url"""
    def on_get(self, request, response):
        query_params = self.get_query_params(request)

        limit = query_params.get("limit", None)
        offset = query_params.get("offset", None)

        session = request.context['session']
        result = session.query(UserProfile).offset(offset).limit(limit).order_by('id').all()
        resp = [process_players_stat(user.as_dict()) for user in result]
        self.on_success(response, resp)

    def on_post(self, request, response):
        data = request.context['data']
        session = request.context['session']
        user = UserProfile()
        user.create_or_update(data)
        session.add(user)
        self.on_success(response, status=falcon.HTTP_201)


class UserDetail(BaseResource):
    """Processing request for detail users representation, '/users/{user_id}' url."""
    def on_get(self, request, response, user_id):
        session = request.context['session']
        user = session.query(UserProfile).get(user_id)
        if user:
            self.on_success(response, user.as_dict())
        self.on_success(response, status=falcon.HTTP_404)

    def on_put(self, request, response, user_id):
        data = request.context['data']
        session = request.context['session']
        user = session.query(UserProfile).get(user_id)
        user.create_or_update(data)
        session.add(user)
        self.on_success(response, status=falcon.HTTP_201)

    def on_patch(self, request, response, user_id):
        data = request.context['data']
        session = request.context['session']
        user = session.query(UserProfile).get(user_id)
        user.create_or_update(data)
        session.add(user)
        self.on_success(response, status=falcon.HTTP_201)

    def on_delete(self, request, response, user_id):
        session = request.context['session']
        session.query(UserProfile).filter_by(id=user_id).delete()
        self.on_success(response, status=falcon.HTTP_204)
