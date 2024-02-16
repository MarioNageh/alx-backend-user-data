#!/usr/bin/env python3
""" Module of auth
"""
import os
from datetime import datetime
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Auth class."""

    def __init__(self):
        """Constructor"""
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id: str = None) -> str:
        """Create a session."""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {'user_id': user_id, 'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return the User ID by requesting it."""
        if session_id is None or not isinstance(session_id, str):
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        user_id = session_dictionary.get('user_id')
        if user_id is None:
            return None
        if self.session_duration <= 0:
            return user_id
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        if (datetime.now() - created_at).seconds > self.session_duration:
            return None
        return user_id
