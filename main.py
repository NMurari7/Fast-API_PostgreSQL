from typing import Optional
import datetime as dt

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from sqlalchemy.sql import text


import models
from database import SessionLocal, engine
from schemas import Trade
from crud import *


#models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/trades/", response_model=Trade)
async def create_item(trade: Trade,db: Session = Depends(get_db), ):
    """
    Create trade entrys
    """
    print(trade)
    create_trade(db, trade=trade)
    return trade

@app.get("/get_all_trades/", response_model=Trade)
def get_trades_details(db: Session = Depends(get_db), assetClass: Optional[str] = None, end: Optional[str] = None,
                        maxPrice: Optional[int] = None, minPrice: Optional[int] = None,
                        start: Optional[str] = None, tradetype: Optional[str] = None,
                        skip: Optional[int] = 0, limit: Optional[int] = 100):
    """
    List all trades with details
    """
    if skip and limit:
        obj = get_stock_details(db, maxPrice = maxPrice, minPrice = minPrice, start = start, end = end,
                            tradeType=tradetype, assetClass=assetClass,
                            skip=skip, limit=limit)
    else:
        obj = get_stock_details(db, maxPrice = maxPrice, minPrice = minPrice, start = start, end = end,
                            tradeType=tradetype, assetClass=assetClass)
    return JSONResponse(content=obj)

@app.get("/get_trade/{trade_id}", response_model=Trade) 
def get_trade(id: str, db: Session = Depends(get_db)):
    """
    return trade details of particular trade with trade id
    """
    obj = get_trade_obj(db, id=id)
    return JSONResponse(content=obj)

@app.get("/search_trade/{text}", response_model=Trade)
def search_trade(text: str, db: Session = Depends(get_db)):
    """
    FInds the given text and looks for the records
    the text exist in
    
    fields that will look into it 
    counterparty
    instrumentId
    instrumentName
    trader
    """
    obj = search_trade_details(db, text = text)
    return JSONResponse(content=obj)
