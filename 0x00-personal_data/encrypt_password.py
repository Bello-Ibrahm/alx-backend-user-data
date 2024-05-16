#!/usr/bin/env python3
"""  """
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Args:
        password (str): password to be hashed

    Return:
        A hashed password
    '''
    p_enc = password.encode('utf-8')
    return bcrypt.hashpw(p_enc, bcrypt.gensalt())
