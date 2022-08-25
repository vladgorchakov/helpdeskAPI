from django.contrib.auth.models import User
import pytest


class UserData:
    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = password

    def get_payload(self):
        payload = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

        return payload

    def get_payload_with_incorrect_data(self):
        payload = {
            "username": self.username + 'x',
            "password": self.password + 'x54x'
        }

        return payload

    payload = property(get_payload)
    payload_incorrect = property(get_payload_with_incorrect_data)