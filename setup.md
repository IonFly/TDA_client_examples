# Setting Up The TD Ameritrade API

TD Ameritrade has a software API for querying price data and executing trades. Conveniently, the Python library `tda-api` uses this backend for Python related experiments.

1. Initialize developer and trading accounts
2. Install libs
3. Obtain API token to interface with TDA backend
4. Run sample script to obtain price quote

## Required Accounts

To start an application for TD Ameritrade, you will need

- A trading account ( [Link](https://www.tdameritrade.com) )
- A developer account ( [Link](https://developer.tdameritrade.com) )

The developer account is used to create your own application that can access the TD Ameritrade API. A brokerage account
is required to access TD Ameritrade products and services.

## Create Application

Please follow the sections for 'Creating a Developer Account' and 'Registering an App' ( [Reference](https://developer.tdameritrade.com/content/getting-started) )

Once the application is created, a 'Consumer Key' will be generated for your application. This is your application's OAauth User ID
which is also referenced as the `client_id` within the `POST /v1/oauth2/token` API call.
Details about your applications such as App Name, Callback URL, purpose, and Order Limit can be changed at anytime.

## Python Installation

The `tda-api` has a convenient how-to for installing the libraries. ( [Link](https://tda-api.readthedocs.io/en/stable/getting-started.html) ) The author leaves it to the user to install the version of Python, libraries, and virtual environment at their discretion.

## Quickstart

### Webdriver Authentication

**While a user could use the `tda.auth.client_from_manual_flow` method instead to bypass the need for a webdriver, instructions for how to setup for `tda.auth.client_from_login_flow` are included for completeness**

The not so obvious piece is the webdriver. While the `tda-api` does a fair job explaining how-to install Python and bindings, the webdriver must be installed separately.

What the webdriver does, is map the python binding to a web browser. This is necessary, as the TD Ameritrade uses the browser session to athenticate the app/user.

- How to Webdriver ( [Link](https://sites.google.com/chromium.org/driver/getting-started) )
- Driver download ( [Link](https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.63/) )

From here, the following script could be run:

```python
from selenium import webdriver
import tda

# Instantiate a webdriver
driver = webdriver.Chrome('./path/to/chromedriver')

# Make a client, save token to path
# 
# tda.auth.client_from_login_flow(
#     webdriver,
#     api_key,
#     redirect_uri,
#     token_path )

tda.auth.client_from_login_flow(
    driver,
    '123456789QwErTy',
    'https://localhost',
    'token_baby' )
```

The API key is generated when initializing an application through the developer portal, see section [Create Application](#create-application) for instructions.

The user will be taken to a login screen, here use your trading account user/pass to authenticate (not the developer account).

### Manual Authentication

If one were not to desire fussing with webdrivers, they may also obtain a token by executing the following:

```python
import tda

# Make a client, save token to path
# 
# tda.auth.client_from_manual_flow(
#     api_key,
#     redirect_uri,
#     token_path )

tda.auth.client_from_manual_flow(
    '123456789QwErTy',
    'https://localhost',
    'token_baby' )
```

What this will do is form a URL that the user will then paste into the web browser of their choice. Follow the instructions and a token will be generated at the specified path.

The API key is generated when initializing an application through the developer portal, see section [Create Application](#create-application) for instructions.

The user will be taken to a login screen, here use your trading account user/pass to authenticate (not the developer account).

### Fetch Price Quotes Example

The following code snippet was borrowed and amplified from the `tda-api` readthedocs page. ( [Link](https://tda-api.readthedocs.io/en/stable/client.html) )

Assuming the `api_key` and `token_path` are valid, the following should save *APPL* historical price data to *report.json*.

``` python
import httpx  # Original forgot import  =/
import json   # Like json better
from tda.auth import easy_client
from tda.client import Client

c = easy_client(
        api_key='123456789QwErTy',
        redirect_uri='https://localhost',
        token_path='./token_baby')

resp = c.get_price_history('AAPL',
        period_type=Client.PriceHistory.PeriodType.YEAR,
        period=Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=Client.PriceHistory.FrequencyType.DAILY,
        frequency=Client.PriceHistory.Frequency.DAILY)

assert resp.status_code == httpx.codes.OK
history = resp.json()

with open('./report.json', 'w') as write_file:
        write_str = json.dumps(history, indent=4)
        write_file.write(write_str)
```
