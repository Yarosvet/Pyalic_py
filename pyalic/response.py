"""Responses environment and managing responses"""
from . import exceptions
from .types import LicenseResponse, OperationResponse


def process_check_key(status_code: int, content: dict) -> LicenseResponse:
    """Process response for checking key"""
    if status_code == 200:
        return LicenseResponse(request_code=status_code,
                               content=content,
                               session_id=content['session_id'],
                               additional_content_product=content['additional_content_product'],
                               additional_content_signature=content['additional_content_signature'])
    error = content.get('error', None) or content.get('detail', None) or content  # If no error found, set it to content
    if error == exceptions.InvalidKeyException.message:
        raise exceptions.InvalidKeyException(response=OperationResponse(status_code, content))
    if error == exceptions.LicenseExpiredException.message:
        raise exceptions.LicenseExpiredException(response=OperationResponse(status_code, content))
    if error == exceptions.SessionsLimitException.message:
        raise exceptions.SessionsLimitException(response=OperationResponse(status_code, content))
    if error == exceptions.InstallationsLimitException.message:
        raise exceptions.InstallationsLimitException(response=OperationResponse(status_code, content))
    raise exceptions.CheckLicenseException(error, response=OperationResponse(status_code, content))


def process_keepalive(status_code: int, content: dict) -> None:
    """Process response for keepalive and raise exceptions if it's failed"""
    if status_code == 200 and 'success' in content and content['success']:
        return
    error = content.get('error', None) or content.get('detail', None) or content  # If no error found, set it to content
    raise exceptions.KeepaliveException(error, response=OperationResponse(status_code, content))


def process_end_session(status_code: int, content: dict) -> None:
    """Process response for ending session and raise exceptions if it's failed"""
    if status_code == 200 and 'success' in content and content['success']:
        return
    error = content.get('error', None) or content.get('detail', None) or content  # If no error found, set it to content
    raise exceptions.EndSessionException(error, response=OperationResponse(status_code, content))
