#!/usr/bin/env python3
""" Authentication Module"""

from flask import request
from typing import List, TypeVar


class Auth:
    ''' API Auth class
    '''


    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
            ) -> bool:
        ''' Required auth
        '''
        return False

    def authorization_header(self, request=None) -> str:
        ''' Header authorization
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' Current user
        '''
        return None
