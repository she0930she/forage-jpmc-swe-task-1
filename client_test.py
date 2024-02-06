import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # print("quote", quote)
      # print("in test")

      # my app res
      res = getDataPoint(quote)

      # mock res
      stock = quote['stock']
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price + ask_price) / 2
      mock_res = stock, bid_price, ask_price, price

      self.assertEqual(res, mock_res)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      #print("quote", quote)
      # my app res
      res = getDataPoint(quote)

      # mock res
      stock = quote['stock']
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price + ask_price) / 2
      mock_res = stock, bid_price, ask_price, price

      self.assertEqual(res, mock_res)


  """ ------------ Add more unit tests ------------ """
  def test_getRatioWithValue(self):
    price_a = 87.97
    price_b = 85.93

    # my app res
    res = getRatio(price_a, price_b)

    # mock res
    mock_res = price_a / price_b

    self.assertEqual(res, mock_res)

  def test_getRatioWithZeroDenominator(self):
    price_a = 87.97
    price_b = 0

    # my app res
    res = getRatio(price_a, price_b)

    # mock res
    mock_res = None

    self.assertEqual(res, mock_res)

  def test_getRatioWithZeroNumerator(self):
    price_a = 0
    price_b = 85.93

    # my app res
    res = getRatio(price_a, price_b)

    # mock res
    mock_res = price_a / price_b

    self.assertEqual(res, mock_res)

if __name__ == '__main__':
    unittest.main()
