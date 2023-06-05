from sqlalchemy import Boolean,Column, Integer, String, DateTime

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
import datetime as db

from database import Base



class Trade(Base):

    __tablename__ = "Trade"
    
    id = Column(Integer, primary_key=True, nullable=False)

    asset_class = Column(String, default=None)

    counterparty =  Column(String, default=None)

    instrument_id = Column(String)

    instrument_name = Column(String)

    trade_date_time = Column(DateTime)
    
    TradeDetails =  Column(JSON, nullable=True)

    trade_id = Column(String, default=None)

    trader = Column(String)





