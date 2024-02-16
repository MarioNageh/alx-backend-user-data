#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar
import os

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class.
    """
    AUTH_KEY = "Basic "

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract base64 authorization header
        """
        if isinstance(authorization_header, str) and \
                authorization_header.startswith(self.AUTH_KEY):
            return authorization_header[len(self.AUTH_KEY):]
