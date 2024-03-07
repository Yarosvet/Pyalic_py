"""Exceptions of Pylic module"""
from .types import OperationResponse


class PyalicException(Exception):
    """All pyalic exceptions"""


class RequestFailed(PyalicException):
    """Request failed or broken response got"""


class PyalicOperationException(PyalicException):
    """Error got from server"""
    message: str
    response: OperationResponse

    def __init__(self, *args, response: OperationResponse):
        self.response = response
        # Initialize with message if no args given
        if args:
            super().__init__(*args)
        else:
            super().__init__(self.message or "")


class CheckLicenseException(PyalicOperationException):
    """Error while checking license"""


class KeepaliveException(PyalicOperationException):
    """Error with keepalive"""


class EndSessionException(PyalicOperationException):
    """Error while ending session"""


class InvalidKeyException(CheckLicenseException):
    """Invalid license key"""
    message = "Invalid license key"


class LicenseExpiredException(CheckLicenseException):
    """License expired"""
    message = "License expired"


class SessionsLimitException(CheckLicenseException):
    """Sessions limit exceeded"""
    message = "Sessions limit exceeded"


class InstallationsLimitException(CheckLicenseException):
    """Installations limit exceeded"""
    message = "Installations limit exceeded"
