CREATE TABLE day_candle (
    id  SERIAL  PRIMARY KEY,
    market  VARCHAR(32),
    candle_date_time_utc   TIMESTAMP,
    candle_date_time_kst   TIMESTAMP,
    opening_price   DECIMAL(27,9),
    high_price  DECIMAL(27,9),
    low_price  DECIMAL(27,9),
    trade_price  DECIMAL(27,9),
    last_timestamp   BIGINT,
    candle_acc_trade_price  DECIMAL(27,9),
    candle_acc_trade_volume  DECIMAL(27,9),
    prev_closing_price  DECIMAL(27,9),
    change_price  DECIMAL(27,9),
    change_rate  DECIMAL(27,9),
    converted_trade_price  DECIMAL(27,9)
);