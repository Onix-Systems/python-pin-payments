from enum import Enum

import requests

from pin_payments.base import Base


class EventType(Enum):
    """List of available event types."""
    CHARGE_AUTHORISED = "charge.authorised"
    CHARGE_VOIDED = "charge.voided"
    CHARGE_CAPTURED = "charge.captured"
    CHARGE_FAILED = "charge.failed"
    CUSTOMER_CREATED = "customer.created"
    CUSTOMER_UPDATED = "customer.updated"
    CUSTOMER_DELETED = "customer.deleted"
    RECIPIENT_CREATED = "recipient.created"
    RECIPIENT_UPDATED = "recipient.updated"
    RECIPIENT_DELETED = "recipient.deleted"
    REFUND_CREATED = "refund.created"
    REFUND_SUCCEEDED = "refund.succeeded"
    REFUND_FAILED = "refund.failed"
    TRANSFER_CREATED = "transfer.created"
    TRANSFER_FAILED = "transfer.failed"
    DEPOSIT_CREATED = "deposit.created"
    SUB_MERCHANT_APPLICATION_SUBMITTED = "sub_merchant_application.submitted"
    SUB_MERCHANT_APPLICATION_ACTIVATED = "sub_merchant_application.activated"
    SUB_MERCHANT_APPLICATION_DECLINED = "sub_merchant_application.declined"
    SUB_MERCHANT_APPLICATION_ON_HOLD = "sub_merchant_application.on_hold"
    PLAN_CREATED = "plan.created"
    PLAN_DELETED = "plan.deleted"
    SUBSCRIPTION_CREATED = "subscription.created"
    SUBSCRIPTION_UNSUBSCRIBED = "subscription.unsubscribed"
    SUBSCRIPTION_CANCELLED = "subscription.cancelled"
    SUBSCRIPTION_EXPIRED = "subscription.expired"
    SUBSCRIPTION_RENEWED = "subscription.renewed"
    SUBSCRIPTION_RENEWAL_FAILED = "subscription.renewal_failed"
    DISPUTE_EVIDENCE_REQUIRED = "dispute.evidence_required"
    DISPUTE_RESOLVED = "dispute.resolved"
    DISPUTE_CANCELLED = "dispute.cancelled"
    DISPUTE_EVIDENCE_UNDER_REVIEW = "dispute.evidence_under_review"
    DISPUTE_LOST = "dispute.lost"
    DISPUTE_WON = "dispute.won"
    DISPUTE_EXPIRED = "dispute.expired"
    DISPUTE_ACCEPTED = "dispute.accepted"
    DISPUTE_ARBITRATION_UNDER_REVIEW = "dispute.arbitration_under_review"
    DISPUTE_ARBITRATION_WON = "dispute.arbitration_won"
    DISPUTE_ARBITRATION_LOST = "dispute.arbitration_lost"


class Events(Base):
    """
    The Events API allows you to view the activity on your account.
    """

    def __init__(self, api_key: str, mode: str = 'live'):
        super().__init__(api_key=api_key, mode=mode)
        self._base_url += 'events/'

    def list(self) -> dict:
        """
        Returns a paginated list of all events.

        GET /events

        :return: dict
        """
        response = requests.get(self._base_url, auth=self._auth)
        return self._handle_response(
            response,
            'Events.list',
            200
        )

    def details(self, event_token: str) -> dict:
        """
        Returns the details of a specified event.

        GET /events/event-token

        :param event_token: The token of the event.
        :return: dict
        """
        url = f"{self._base_url}{event_token}"
        response = requests.get(url, auth=self._auth)
        return self._handle_response(
            response,
            'Events.details',
            200
        )


if __name__ == '__main__':
    events_api = Events()
