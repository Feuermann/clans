import falcon

from app.api import users
from app.setup import session_init
from app.setup import SESSION
from app.middleware import JSONDecoder, SessionManager


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        self.add_route('/users', users.Users())
        self.add_route('/users/{user_id}', users.UserDetail())

session_init()
middleware = [JSONDecoder(), SessionManager(SESSION)]
application = App(middleware=middleware)