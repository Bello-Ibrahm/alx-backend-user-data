#!/usr/bin/env python3
""" Handles basic auth """
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
    '''
    '''

    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        ''' Extract the Base64 part of the Authorization header
        for a Basic Authentication

        Args:
            authorization_header (str): auth_header
        Returns:
            str: base64 part of header
        '''
        if not (authorization_header and isinstance(authorization_header, str)
                and authorization_header.startswith('Basic ')):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        ''' Decode a Base64-encoded string
        '''
        if not (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        ''' Extracts user email and password
        from the Base64 decoded value.
        Args:
            self (obj): Basic Auth instance
            decoded_base64_authorization_header (str): auth header
        '''
        if not (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return None, None

        return tuple(decoded_base64_authorization_header.split(':', 1))
