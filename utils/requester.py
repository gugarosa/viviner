"""Module used to provide the wrapped requesting class."""

import requests


class Requester:
    """Wraps basic `requests` package functions into a class.

    """

    def __init__(self, base_url):
        """Initializition method.

        Args:
            base_url (str): String that defines the base URL.

        """

        # Defines the base URL to be used
        self.base_url = base_url

        # Defines the default headers to be used
        self.headers = {
            "User-Agent": ""
        }

    def get(self, endpoint, **kwargs):
        """Wraps the `get` method of `requests`.

        Args:
            endpoint (str): Endpoint to be consumed.

        Returns:
            The `get` function with pre-populated headers over the endpoint.

        """

        # Defines the full-path URL
        url = self.base_url + endpoint

        return requests.get(url, headers=self.headers, **kwargs)
