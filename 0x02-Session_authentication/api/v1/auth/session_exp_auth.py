#!/usr/bin/env python3
""" Session Expiration Authentication Module
"""
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    '''
    '''
    def __init__(self):
        '''
        '''
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Execption:
            self.session_duration = 0

    def create_session(self, user_id=None):
        '''
        '''
        session_id = super().create_session(user_id)
        if type(session_id) is not str:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''
        '''
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' not in session_dict:
                return None
            cur_time = datetime.now()
            time_span = timedelta(seconds=self.session_duration)
            exp_time = session_dict['created_at'] + time_span
            if exp_time < cur_time:
                return None
            return session_dict['user_id']
