from typing import Optional

import requests

from pin_payments.base import Base


class Disputes(Base):
    """
    The disputes API allows you to retrieve details of
    disputes against your charges and perform actions
    to either challenge or accept them.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'disputes/'

    def list_disputes(
            self,
            sort: Optional[str] = None,
            direction: Optional[int] = 1
    ) -> dict:
        """
        Returns a paginated list of all disputes.
        GET /disputes
        :param sort: The field used to sort the disputes.
        :param direction: The direction in which to sort the
        disputes (1 for ascending or -1 for descending).
        :return: dict
        """
        params = {}
        if sort is not None:
            params['sort'] = sort
        params['direction'] = direction
        response = requests.get(self._base_url, auth=self._auth, params=params)
        return self._handle_response(
            response,
            'list_disputes',
            200
        )

    def search_disputes(
            self,
            query: Optional[str] = None,
            status: Optional[str] = None,
            sort: Optional[str] = None,
            direction: Optional[int] = 1
    ) -> dict:
        """
        Returns a paginated list of disputes matching the search criteria.
        GET /disputes/search
        :param query: Query for searching disputes.
        :param status: The status of the disputes.
        :param sort: The field used to sort the disputes.
        :param direction: The direction of sorting.
        :return: dict
        """
        params = {}
        if query is not None:
            params['query'] = query
        if status is not None:
            params['status'] = status
        if sort is not None:
            params['sort'] = sort
        params['direction'] = direction
        response = requests.get(f"{self._base_url}search", auth=self._auth, params=params)
        return self._handle_response(
            response,
            'search_disputes',
            200
        )

    def get_dispute_details(self, dispute_token: str) -> dict:
        """
        Returns the details of a dispute.
        GET / disputes / < dispute_token >
        :param dispute_token: The token of the dispute.
        :return: dict
        """
        response = requests.get(f"{self._base_url}{dispute_token}", auth=self._auth)
        return self._handle_response(
            response,
            'get_dispute_details',
            200
        )

    def get_dispute_activity(self, dispute_token: str) -> dict:
        """
        Returns the activity feed for a dispute.
        GET / disputes / < dispute_token > / activity
        :param dispute_token: The token of the dispute.
        :return: dict
        """
        response = requests.get(f"{self._base_url}{dispute_token}/activity", auth=self._auth)
        return self._handle_response(
            response,
            'get_dispute_activity',
            200
        )

    def get_dispute_evidence(self, dispute_token: str) -> dict:
        """
        Displays current evidence batch for a dispute.
        GET / disputes / < dispute_token > / evidence
        :param dispute_token: The token of the dispute.
        :return: dict
        """
        response = requests.get(f"{self._base_url}{dispute_token}/evidence", auth=self._auth)
        return self._handle_response(
            response,
            'get_dispute_evidence',
            200
        )

    def update_dispute_evidence(
            self,
            dispute_token: str,
            evidence_data: dict[str, str]
    ) -> dict:
        """
        Updates evidence batch for a dispute.
        PUT / disputes / < dispute_token > / evidence
        :param dispute_token: The token of the dispute.
        :param evidence_data: The evidence data to be updated.
        :return: dict
        """
        response = requests.put(f"{self._base_url}{dispute_token}/evidence", auth=self._auth, json=evidence_data)
        return self._handle_response(
            response,
            'update_dispute_evidence',
            200
        )

    def submit_dispute_evidence(self, dispute_token: str) -> dict:
        """
        Submits current evidence batch for review.
        POST / disputes / < dispute_token > / evidence
        :param dispute_token: The token of the dispute.
        :return: dict
        """
        response = requests.post(f"{self._base_url}{dispute_token}/evidence", auth=self._auth)
        return self._handle_response(
            response,
            'submit_dispute_evidence',
            200
        )

    def accept_dispute(self, dispute_token: str) -> dict:
        """
        Accepts a dispute.
        POST / disputes / < dispute_token > / accept
        :param dispute_token: The token of the dispute.
        :return: dict
        """
        response = requests.post(f"{self._base_url}{dispute_token}/accept", auth=self._auth)
        return self._handle_response(
            response,
            'accept_dispute',
            200
        )
