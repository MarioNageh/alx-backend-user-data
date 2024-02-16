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
    ...
