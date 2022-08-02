from enum import Enum


class VpnSubscriptionTariffDataOperation(str, Enum):
    EQUAL = "equal"
    GREATER_THAN_OR_EQUAL = "greater_than_or_equal"

    def __str__(self) -> str:
        return str(self.value)
