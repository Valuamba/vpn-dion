from enum import Enum


class VpnSubscriptionStatus(str, Enum):
    PAID = "paid"
    WAITING_FOR_PAYMENT = "waiting for payment"
    PAYMENT_WAS_FAILED = "payment_was_failed"

    def __str__(self) -> str:
        return str(self.value)
