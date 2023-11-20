import pdb
import re
import sys
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if re.match("^[a-zA-Z]{3,}$", username) is None:
            raise UserInputError("Username is invalid")

        if self._user_repository.find_by_username(username) is not None:
            raise UserInputError("Username is already taken")

        if len(password) < 8:
            raise UserInputError("Password is too short")

        if re.search("[0-9]", password) is None:
            raise UserInputError("Password must contain numbers")


