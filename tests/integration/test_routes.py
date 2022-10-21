# from earnings_release.server import app
# import json
# import unittest

# class TestGetPressReleaseDatesRoute(unittest.TestCase):
#     def test_should_return_200_when_get_press_release_dates_by_ticker_of_googl(self):
#         _, response = app.test_client.get('/press-release-dates/googl')
#         self.assertEqual(response.status, 200)
#         data = json.loads(response.text)
#         self.assertEqual(data['ticker'], 'GOOGL')
#         self.assertEqual(data['company_name'], 'Alphabet Inc')
#         self.assertEqual(type(data['earnings_release_date']), list)


#     def test_should_return_404_when_get_press_release_dates_by_ticker_of_invalid(self):
#         _, response = app.test_client.get('/press-release-dates/invalid')
#         self.assertEqual(response.status, 404)
#         data = json.loads(response.text)
#         self.assertEqual(type(data['error']), str)


# class TestPostGetPressReleasesDatesRoute(unittest.TestCase):
#     def test_should_return_200_when_get_press_release_dates_by_tickers_of_adbe_and_v(self):
#         _, response = app.test_client.post('/press-release-dates', json=["adbe", "v"])
#         self.assertEqual(response.status, 200)
#         data = json.loads(response.text)
#         self.assertEqual(len(data), 2)
#         self.assertEqual(data[0]['ticker'], 'ADBE')
#         self.assertEqual(data[1]['ticker'], 'V')


#     def test_should_return_200_when_get_press_release_dates_by_ticker_of_googl_and_invalid(self):
#         _, response = app.test_client.post('/press-release-dates', json=["googl", "invalid"])
#         self.assertEqual(response.status, 200)
#         data = json.loads(response.text)
#         self.assertEqual(len(data), 2)
#         self.assertEqual(data[0]['ticker'], 'GOOGL')
#         self.assertEqual(data[1]['ticker'], 'INVALID')


#     def test_should_return_400_when_get_press_release_dates_by_ticker_with_list_of_numbers(self):
#         _, response = app.test_client.post('/press-release-dates', json=[1, 2])
#         self.assertEqual(response.status, 400)
#         data = json.loads(response.text)
#         self.assertTrue('error' in data)


#     def test_should_return_400_when_get_press_release_dates_by_ticker_with_empty_list(self):
#         _, response = app.test_client.post('/press-release-dates', json=[])
#         self.assertEqual(response.status, 400)
#         data = json.loads(response.text)
#         self.assertTrue('error' in data)


#     def test_should_return_400_when_get_press_release_dates_by_ticker_with_invalid_json(self):
#         _, response = app.test_client.post('/press-release-dates', json='{')
#         self.assertEqual(response.status, 400)
#         data = json.loads(response.text)
#         self.assertTrue('error' in data)

