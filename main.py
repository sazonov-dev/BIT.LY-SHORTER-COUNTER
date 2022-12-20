import argparse
import logging
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def is_bitlink(token, url):
  headers = {
    'Authorization': f'Bearer {token}',
  }
  parsed_url = urlparse(url)
  response = requests.get(
    f'https://api-ssl.bitly.com/v4/bitlinks/'
    f'{parsed_url.netloc}/{parsed_url.path}',
    headers=headers
  )
  return response.ok


def shorten_link(token, url):
  headers = {
    'Authorization': f'Bearer {token}',
  }
  long_url = {"long_url": url}
  response = requests.post('https://api-ssl.bitly.com/v4/shorten',
    headers=headers,
    json=long_url
  )
  response.raise_for_status()
  short_url = response.json()
  return short_url["link"]


def count_clicks(token, url):
  headers = {
    'Authorization': f'Bearer {token}',
  }
  params = {
    'unit': 'month',
  }
  parsed_url = urlparse(url)
  response = requests.get(
    f'https://api-ssl.bitly.com/v4/bitlinks/'
    f'{parsed_url.netloc}/{parsed_url.path}',
    headers=headers
  )
  response.raise_for_status()
  total_clicks = response.json()['total_clicks']
  return total_clicks


def main():
  load_dotenv()
  bitly_token = os.environ['BITLY_TOKEN']
  parser = argparse.ArgumentParser(
    description='Парсит ссылку для сервиса Bit.ly'
  )
  parser.add_argument('link')
  args = parser.parse_args()

  try:
    if is_bitlink(bitly_token, args.link):
          bitly_url_clicks = count_clicks(bitly_token, args.link)
          print(f'По ссылке {args.link}, общее кол-во кликов {bitly_url_clicks}')
    else:
      short_bitly_url = shorten_link(bitly_token, args.link)
      print(f'Битлинк - {short_bitly_url}')
  except requests.exceptions.HTTPError as error:
    logging.error(error)


if __name__ == '__main__':
  main()
