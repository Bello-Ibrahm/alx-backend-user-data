#!/usr/bin/env python3
""" Authentication Module """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    '''
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    ''' Generate a uuid and return its string representation
    '''
    return str(uuid4())


class Auth:
    ''' Auth class to interact with the authentication database.
    '''
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''  Add a user to the database
        '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        '''
        '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        u_hashed_pwd = user.hashed_password
        pwd = password.encode("utf-8")
        return bcrypt.checkpw(pwd, u_hashed_pwd)

    def create_session(self, email: str) -> str:
        '''
        '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        '''
        '''
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        '''
        '''
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None
        return None
