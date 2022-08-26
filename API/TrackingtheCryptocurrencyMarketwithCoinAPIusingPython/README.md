# 1. Introduction

We can describe cryptocurrency as a form of currency that only exists virtually and isn't regulated by a central authority. Rather, there is a secure decentralized system to trade cryptocurrency. Cryptocurrencies are built using the principles of blockchain technology. With cryptocurrency, we can transfer funds cheaply, quickly, and securely. The process is somewhat shielded from government interference, which is one of the reasons why it has taken the financial world by storm.

With the newfound popularity of cryptocurrencies, market data on cryptocurrency trading has become equally important. This market data is essential for evaluating the value of crypto portfolios, managing risk when trading cryptocurrencies, drafting good market-making strategies, and even for use in big data research.

We'll quickly go through the CoinAPI service in this course, which provides us with essential data on the cryptocurrency market. This data includes information on the different cryptocurrency exchanges, metadata on each cryptocurrency, current and historical prices, exchange rates, and more. Don't be intimidated by any of these terms yet! We'll cover each of them in detail later in this course. By the end of the course, we'll integrate CoinAPI into a demo dashboard application to provide interactive and visual cryptocurrency-market data.

## Overview of CoinAPI

Before delving into how [CoinAPI](https://www.coinapi.io/) works, it’s important to know what an API is and understand some of its protocols.

An API is an intermediary that passes information back and forth between two applications. APIs pass a request for information from one application to another and then deliver the information as a response back to the original requestor.

### Market Data API of CoinAPI

The Market Data API is the primary API of CoinAPI, which provides high-quality data on the cryptocurrency market. CoinAPI not only provides reliable data, though, but also standardizes it across different exchanges.

The Market Data API follows the REST API architecture to deliver most of the market data stored on the CoinAPI database. For more complex integrations which require streaming real-time market data, we need to use the WebSocket and FIX architectures for the API.

We need to use the HTTP GET method to send requests to CoinAPI’s Market Data API. Here are the endpoints available on the Market Data API to make API calls to CoinAPI:

| Endpoint environment | Encryption | Endpoint URL |
| :------------------- | ---------- | -----------: |
| Production | Yes | https://rest.coinapi.io/ |
| Production | No  | http://rest.coinapi.io/ |
| Sandbox    | Yes | https://rest-sandbox.coinapi.io/ |
| Sandbox    | No  | http://rest-sandbox.coinapi.io/ |

### The sandbox environment

CoinAPI also provides a sandbox environment, a testing environment generally used for exploration or development purposes. To use this sandbox, we’ll need an API key (we will cover how to acquire an API key in the next chapter). The key can be the same one we use for the production environment, even if it’s free. CoinAPI sandbox environment is different from its production environment in a few ways:

* CoinAPI doesn’t provide active support for the sandbox environment. It doesn’t handle any issues on priority, unlike the production environment.

* Data on the sandbox environment is limited to only a few market data sources—COINBASE, ECB (European Central Bank), GEMINI, testnets, and UAT environments.

* Changes and updates to the Market Data API will be available on the sandbox environment before any of the production environments, which means that it will be less stable compared to the production environment.

* There’s a possibility that the data available in the sandbox could be outdated, incorrect, or even entirely fake.

# 2. Metadata

## Cryptocurrency Exchanges

### What are cryptocurrency exchanges?

Cryptocurrency exchanges are online platforms that help facilitate cryptocurrency trading for a service fee, and this trading sometimes even involves trading a cryptocurrency for fiat currency. Cryptocurrency exchanges act as the only intermediary between buyers and sellers of cryptocurrencies.

A cryptocurrency trade is different from a typical stock trade. In a stock trade, a bank acts as a custodian of assets and guarantees the repayment of those assets. Then, a stock exchange matches buyers and sellers, and a broker issues buying or selling orders on behalf of a buyer or seller. A cryptocurrency exchange takes up the responsibility and risk of all these roles, allowing for trading to take place with high frequency compared to stock trading.

Fiat currency transfers happen through traditional banks, whereas cryptocurrency transfer is done through blockchains in a cryptocurrency exchange. The trade on the exchange happens instantly as we deposit the money in a cryptocurrency exchange, and is readily available as a virtual balance. When a trade happens between a buyer and seller on the exchange, their virtual balances are adjusted, and they only get access to the traded currency once they withdraw it.

### The exchanges endpoint

We can get the details of the different exchanges on CoinAPI using the exchanges endpoint. We can list all supported exchanges on CoinAPI using /v1/exchanges. To list a single exchange, we use /v1/exchanges/{exchange_id}, where exchange_id represents the exchange we want to single out.

## Assests

### What are crypto assets?

We can describe assets as resources with some economic value assigned to them. Crypto assets are digital assets that include cryptocurrencies, NFTs, security tokens, and more. As of this writing, cryptocurrencies are the only crypto assets information available on CoinAPI.


### The assets endpoint

We can get the details of the different assets on CoinAPI using the assets endpoint. These assets on CoinAPI include some fiat currencies and some other cryptocurrencies. We can list all assets on CoinAPI using /v1/assets. To list a single asset, we use /v1/assets/{asset_id}, where asset_id represents the asset we want to single out.

## Symbols

### What are symbols in CoinAPI?

CoinAPI defines symbols as unique identifiers for specific assets of exchange based on a specific financial instrument. We use the type of symbol to define the pattern for constructing each symbol. The following table describes these different symbol types:

### Symbol types

| Name | Type | Description |
| :------ | -------- | ---------- |
| FX Spot | SPOT | An FX spot is an agreement to exchange one asset for another. For example, exchange BTC for USD. |
| Futures Contract | FUTURES | A futures contract is an fx spot derivative contract in which traders have an agreement to trade fx spots at a pre-determined time in the future. |
| Option Contract | OPTION | An option contract is an fx spot derivative contract that requires traders to buy or sell fx spots at pre-determined prices on an agreed-upon exercise date. |
| Perpetual Contract | PERPETUAL | A perpetual contract is an fx spot derivative contract in which traders have an agreement to trade fx spots continuously without setting any pre-determined delivery time in the future. |
| Index | INDEX | An index is a statistical composite measure for any market or economic changes. |
| Credit/Funding | CREDIT | Credit/funding refers to a margin funding contract where prices represent the daily rate and order books display loan and borrow bids. Price represents the daily rate. |
| Contract | CONTRACT | This symbol type represents other types of financial contracts or instruments like spreads and interest rate swaps. |

### Symbol Patterns

| Symbol type | Symbol pattern |
| SPOT | {exchange_id}_SPOT_{asset_id_base}_{asset_id_quote} |
| FUTURES | {exchange_id}_FTS_{asset_id_base}_{asset_id_quote}_{YYMMDD of future_delivery_time} |
| OPTION | {exchange_id}_OPT_{asset_id_base}_{asset_id_quote}_{YYMMDD of option_expiration_time}_{option_strike_price}_{option_type_is_call as C/P} |
| PERPETUAL | {exchange_id}_PERP_{asset_id_base}_{asset_id_quote} |
| INDEX |  {exchange_id}_IDX_{index_id} |
| CREDIT | {exchange_id}_CRE_{asset_id_base} |
| CONTRACT | {exchange_id}_COT_{contract_id} |

# 3. Cryptocurrency Market Data

## 3.1 Trade Transactions

### The trades endpoint

We use the trades endpoint to get data related to the several executed trade transactions on different exchanges. This data is also known as the matched orders or active data.

### The taker/aggressor side of a transaction

A taker or aggressor of a transaction is a trader who initiates a trade transaction with an at-market ask/bid price. This removes liquidity from the marketplace. A taker can be a buyer or seller. The following table defines the different taker values supported on CoinAPI:

### Latest trade transaction data

We can get a complete list of all trade transactions up to a minute ago for all or one specific symbol without any time limitations. To fetch the latest trades for all symbols, we use /v1/trades/latest and for a specific symbol, we use /v1/trades/{symbol_id}/latest. These will fetch and sort the latest trade data in descending order of time.

### Historical trade transaction data

We can get a complete history of all trade transactions for a specific symbol using /v1/trades/{symbol_id}/history. This will fetch and sort any historical trade data in ascending order of time.

## 3.2 OHLCV Data

The OHLCV endpoint provides the OHLCV time series data relating to all or one specific symbol. OHLCV is the aggregated form for the Open, High, Low, Close, Volume data attributes of market data. The first four attributes represent the opening, closing, highest, and lowest prices in a specific time interval. Volume represents the total number of trades in that time interval.

### Latest OHLCV data

We can get a complete list of the latest OHLCV data from up to a minute ago for all or one specific symbol. To fetch the latest OHLCV data for a specific symbol, we use /v1/ohlcv/{symbol_id}/latest. This will fetch and sort the latest OHLCV data in descending order of time. This endpoint can provide real-time data without any delays.

### Historical OHLCV data

We can get a complete history of all OHLCV data for a specific symbol by attaching the following URL pattern in front of the base URL /v1/ohlcv/{symbol_id}/history. This will fetch and sort any historical OHLCV data in ascending order of time.

# 4. Exchanging Data

We can describe exchange rates as the price in one asset or currency to convert it to another asset or currency. The exchange rate that CoinAPI provides is the 24-Hour (rolling window) Volume Weighted Average Price, or VWAP-24H, from across multiple data sources on the CoinAPI platform.

### Fetch a specific exchange rate

We can get a specific exchange rate for a currency pair on CoinAPI using /v1/exchangerate/{asset_id_base}/{asset_id_quote}, where asset_id_base represents the id of the base asset we want and asset_id_quote represents the id of the quote asset we want to exchange for the base asset.

### Fetch a current exchange rate

We can get the current exchange rate between an asset and other assets on CoinAPI using /v1/exchangerate/{asset_id_base}, where asset_id_base represents the id of the base asset we want.

