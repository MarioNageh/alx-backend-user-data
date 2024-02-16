#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class."""

    AUTH_KEY: str = ""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that require authentication.
        :param path:
        :param excluded_paths:
        :return:
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Method that require authorization header.
        :param request:
        :return:
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that require current user.
        :param request:
        :return:
        """
        return None
