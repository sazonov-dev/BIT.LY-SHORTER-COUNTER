# Bit.ly url validator and url shorter

## Environment

### Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

### Environment variables

- BITLY_TOKEN

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

#### How to get

* Register in [BIT.LY](https://bitly.com/) and get the `API Key` for Environment BITLY_TOKEN:

## Run

Launch on Linux(Python 3) or Windows:

```
python3 main.py YOUR_URL
```

You will see:

```
Битлинк - https://bit.ly/3Pe0zEz

OR

По ссылке https://bit.ly/3Pe0zEz, общее кол-во кликов 0
```


