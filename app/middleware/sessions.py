import falcon
import sqlalchemy.orm.scoping as scoping
from sqlalchemy.exc import SQLAlchemyError

from app import setup


class SessionManager(object):
    """Middleware class for processing sessions."""

    def __init__(self, db_session):
        self._session_factory = db_session
        self._scoped = isinstance(db_session, scoping.ScopedSession)

    def process_request(self, request, response, resource=None):

        request.context['session'] = self._session_factory

    def process_response(self, request, response, resource=None):

        session = request.context['session']

        if setup.DB_AUTOCOMMIT:
            try:
                session.commit()
            except SQLAlchemyError:
                session.rollback()
                raise ValueError('Session aborted')

        if self._scoped:
            session.remove()
        else:
            session.close()
