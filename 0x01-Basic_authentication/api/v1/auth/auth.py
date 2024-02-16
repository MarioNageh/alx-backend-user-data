from typing import List, TypeVar

from flask import Flask, jsonify, abort, request


class Auth:
    """Auth class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that require authentication.
        :param path:
        :param excluded_paths:
        :return:
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method that require authorization header.
        :param request:
        :return:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that require current user.
        :param request:
        :return:
        """
        return None
