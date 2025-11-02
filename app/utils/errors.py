class AppError(Exception):
    def __init__(self, message, status_code=400, payload=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

    def to_dict(self):
        return {
            "status": "error",
            "message": self.message,
            **self.payload
        }

class BadRequestError(AppError):
    def __init__(self, message="Bad request", payload=None):
        super().__init__(message, 400, payload)

class UnauthorizedError(AppError):
    def __init__(self, message="Unauthorized", payload=None):
        super().__init__(message, 401, payload)

class ForbiddenError(AppError):
    def __init__(self, message="Forbidden", payload=None):
        super().__init__(message, 403, payload)

class NotFoundError(AppError):
    def __init__(self, message="Not found", payload=None):
        super().__init__(message, 404, payload)



"""
usage:
from app.utils.errors import NotFoundError

if not user:
    raise NotFoundError("User not found")

"""