"""
1. 가격 및 거래량의 일일, 주간, 월간 변동을 추적하는 테이블.
CREATE TABLE changes AS
SELECT candle_date_time_utc,
       trade_price - LAG(trade_price) OVER (ORDER BY candle_date_time_utc) as daily_change,
       trade_price - LAG(trade_price, 7) OVER (ORDER BY candle_date_time_utc) as weekly_change,
       trade_price - LAG(trade_price, 30) OVER (ORDER BY candle_date_time_utc) as monthly_change
FROM bitcoins;

2. 각 날짜별로 비트코인의 변동성을 측정하는 테이블. 예를 들어, 고가와 저가의 차이나, 일일 종가 기반의 이동 평균 변동성 등을 계산할 수 있다.
CREATE TABLE volatility AS
SELECT candle_date_time_utc,
       high_price - low_price as daily_volatility,
       AVG(trade_price) OVER (ORDER BY candle_date_time_utc ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as moving_avg_volatility
FROM bitcoins;

3.비트코인의 중장기 트렌드를 파악하기 위한 테이블. 이동 평균, 지수 이동 평균 등의 기법을 활용해 트렌드를 측정할 수 있다.
CREATE TABLE trend AS
SELECT candle_date_time_utc,
       AVG(trade_price) OVER (ORDER BY candle_date_time_utc ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as moving_avg,
       AVG(trade_price) OVER (ORDER BY candle_date_time_utc ROWS BETWEEN 89 PRECEDING AND CURRENT ROW) as moving_avg_long
FROM bitcoins;

4.각 날짜별로 비트코인의 거래량을 기록하는 테이블. 일일 거래량 뿐만 아니라, 거래량의 변동성, 거래량 기반의 이동 평균 등을 계산할 수 있다.
CREATE TABLE volume AS
SELECT candle_date_time_utc,
       candle_acc_trade_volume,
       AVG(candle_acc_trade_volume) OVER (ORDER BY candle_date_time_utc ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as moving_avg_volume
FROM bitcoins;
"""