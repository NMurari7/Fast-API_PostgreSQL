from fastapi.encoders import jsonable_encoder
from sqlalchemy import text
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy import and_
import models, schemas
import json

def create_trade(db: Session, trade: schemas.Trade):
    """
    Creates a trade entry into database
    """
    db_obj = models.Trade(asset_class=trade.asset_class,counterparty = trade.counterparty,
                            instrument_id = trade.instrument_id, instrument_name = trade.instrument_name,
                            trade_date_time = trade.trade_date_time, TradeDetails = eval(trade.trade_details.json()),
                            trade_id = trade.trade_id,  trader = trade.trader)
    db.add(db_obj)
    
    db.commit()
    
    db.refresh(db_obj)
    
    return db_obj

def get_stock_details(db: Session, asset_class = None, maxPrice = None, minPrice = None, start = None, end = None,
                        tradeType = None, assetClass = None, skip = None, limit = None):
    """
    Returns all the trade details
    """

    if maxPrice and minPrice:
        if skip and limit:
            obj = db.query(models.Trade).filter(text("""("TradeDetails"->>'price')::FLOAT >= {}""".format(minPrice))).filter(text("""("TradeDetails"->>'price')::FLOAT <= {}""".format(maxPrice))).offset(skip).limit(limit).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
        else:
            obj = db.query(models.Trade).filter(text("""("TradeDetails"->>'price')::FLOAT >= {}""".format(minPrice))).filter(text("""("TradeDetails"->>'price')::FLOAT <= {}""".format(maxPrice))).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
    elif start and end:
        if skip and limit:
            obj = db.query(models.Trade).filter(models.Trade.trade_date_time >= start).filter(models.Trade.trade_date_time<= end).offset(skip).limit(limit).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
        else:
            obj = db.query(models.Trade).filter(models.Trade.trade_date_time >= start).filter(models.Trade.trade_date_time<= end).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
    elif tradeType:
        if skip and limit:
            obj = db.query(models.Trade).filter(text("""("TradeDetails"->>'buySellIndicator') = {}""".format(tradeType))).offset(skip).limit(limit).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
        else:
            obj = db.query(models.Trade).filter(text("""("TradeDetails"->>'buySellIndicator') = {}""".format(tradeType))).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
    elif assetClass:
        if skip and limit:
            obj = db.query(models.Trade).filter(models.Trade.asset_class==assetClass).offset(skip).limit(limit).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
        else:
            obj = db.query(models.Trade).filter(models.Trade.asset_class==assetClass).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data
    else:
        if skip and limit:
            obj = db.query(models.Trade).offset(skip).limit(limit).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data

        else:
            obj = db.query(models.Trade).all()
            json_compatible_item_data = jsonable_encoder(obj)
            return json_compatible_item_data

def get_trade_obj(db: Session, id: str):
    """
    Return trade details for particular trade
    using trade id
    """

    obj = db.query(models.Trade).filter(models.Trade.trade_id == id).first()
    json_compatible_item_data = jsonable_encoder(obj)
    return json_compatible_item_data

def search_trade_details(db: Session, text: str):
    """
    Given text will be searched in applicable feilds 
    and return all the rows that cotains the text
    """
   
    obj = db.query(models.Trade).filter((models.Trade.counterparty.ilike(text)) |(models.Trade.instrument_id.ilike(text)) |(models.Trade.instrument_name.ilike(text)) |(models.Trade.trader.ilike(text))).all()
    json_compatible_item_data = jsonable_encoder(obj)
    return json_compatible_item_data
    
