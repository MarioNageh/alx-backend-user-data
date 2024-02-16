#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Auth class."""

    AUTH_KEY: str = ""
