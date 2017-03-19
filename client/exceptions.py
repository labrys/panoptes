# coding=utf-8

import requests.exceptions


class ClientError(Exception):
    """
    An error occurred in the client.

    This error should not be thrown directly, instead it should be sub-classed
    and the appropriate sub-classed error should be thrown.
    """


class RequestException(ClientError,
                       requests.exceptions.RequestException):
    """
    A wrapper around RequestException from the requests package.

    https://github.com/kennethreitz/requests
    """


class AuthError(ClientError, RequestException):
    """An error occurred while trying to authenticate."""
