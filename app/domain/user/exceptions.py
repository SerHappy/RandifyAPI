class BaseUserError(Exception):
    """Base class for user exceptions."""


class PasswordTooShortError(BaseUserError):
    """User password is too short."""


class PasswordTooLongError(BaseUserError):
    """User password is too long."""


class PasswordTooCommonError(BaseUserError):
    """User password is too common."""


class UserNotFoundError(BaseUserError):
    """User not found."""

class UserAlreadyExistsError(BaseUserError):
    """User already exists."""