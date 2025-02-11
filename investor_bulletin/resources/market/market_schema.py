""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""

from pydantic import BaseModel, Field
from decimal import Decimal

class StockPrice(BaseModel):
    symbol: str
    price: Decimal = Field(description="Current stock price")
    currency: str = Field(default="USD")
    timestamp: str | None = None

class MarketPricesResponse(BaseModel):
    data: dict[str, StockPrice | str] = Field(
        description="Dictionary of stock prices keyed by symbol"
    )
