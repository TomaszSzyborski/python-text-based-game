from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class InventoryItem:
    """
    @name - string
    @unit_price - Decimal
    @quantity - int, default 1
    @required_level - int, default 0
    """
    name: str = field(init=True)
    unit_price: Decimal = field(init=True, repr=True, compare=True)
    quantity: int = field(repr=False, default=1)
    required_level: int = field(default=0, init=True, repr=True, compare=True, metadata=None)

    def total_cost(self) -> Decimal:
        return self.unit_price * self.quantity
