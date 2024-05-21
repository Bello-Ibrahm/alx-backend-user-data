#!/usr/bin/env python3
""" Handles basic auth """
from api.v1.auth.auth import Auth


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
