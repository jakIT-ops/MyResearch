# 1. Introduction

[Marqeta](https://www.marqeta.com/) is a modern card issuing and transaction processing platform that allows companies to launch and scale card programs to meet their business needs. It streamlines business payments because it works with card networks and issuing banks in order to issue cards, authorize transactions, and communicate with settlement entities.

Marqeta alleviates the need to deal directly with a traditional bank. Instead, it takes care of the back-end payment technology and works with banks to process payment transactions. This allows businesses to offer payment card products to their customers

### What is Marqeta’s Core API?

Marqeta’s Core API is a RESTful interface that’s used to create and manage payment card programs. It supports webhooks to provide real-time updates about events in a program. For example, the occurrence of a transaction, changes in a card’s state, actions performed through cards, among others. In this course, we’ll learn how to use Marqeta’s core API to create a simple payment card program.

###  Intended audience

This course is designed for anyone who wants to explore and integrate payment card systems and their functionalities. It’ll provide an understanding of Marqeta’s Core API’s various endpoints with some hands-on examples.

The features of Marqeta’s Core API enable users to manage card programs for their businesses. These features include the ability to issue cards and process card payments.

## Core API resources

The Core API comprises the following key resources:

* A user, also known as a cardholder, is a person who owns and uses a Marqeta card.

* The card, is a physical or virtual payment card owned by a user.

* The card product defines the behavior and functionality of Marqeta cards. It further defines the attributes of the card and specifies the policies regarding its usage.

* A general purpose account, also known as GPA, it is the default account for a user.

* The funding source is the source from which funds are transferred to a user’s general purpose account (GPA) using a GPA order.

* A GPA order is the means by which funds are transferred from a funding source into a general purpose account (GPA) of a user.


## Create a Marqeta user

We can create a Marqeta user by making a `POST` request to the `{BASE_URL}/users` endpoint. We can provide the user’s basic information in the body of the request. If we want to create a child user, we must provide a value for the `parent_token`. Additionally, we can allow the child user to share an account with their `parent` by setting the uses_parent_account field value to True.


### Request parameters 

| Parameter | Type | Category | Description |
| :-------- | ---- | -------- | ----------: |
| first_name | string | optional | User's first name, Maximum length: 40 characters |
| last_name | string | optional | User's last name,  Maximum length: 40 characters |
| email | string | optional | User's email address, Length: 1–255 characters, Note: Email address must be unique among all users. |
| password | string | optional | User's account password, Maximum length: 255 characters  Conditions: Must contain at least one numeric digit Must contain at least one lowercase letter Must contain at least one uppercase letter Must contain at least one of the following symbols:`@ # $ % ! ^ & * ( ) \ _ + ~ ` - = [ ] { } , ; : ' " , . / < > ?` |
|address1 | string | optional | User's address Maximum length: 255 characters |
| country | string | optional | Country corresponding to the user's address Maximum length: 40 characters |
| phone | string | optional | User's phone number Format: +00000000000 Maximum length: 255 characters |
| company | string | optional | Name of the company Maximum length: 255 characters |
| token | string | optional | Unique token of the user Length: 1–36 characters Note: If not specified, the system generates one automatically. This value can't be updated once set.
| uses_parent_account | boolean | optional | Set to True if the child account shares balances with the parent, "False" otherwise this value is False. Note: If the value is set to True, the parent_token must also have a value be set. This value can't be updated once set. Default value: False |
|parent_token | string | optional | Token of a user or business that is be set as the parent of the current user Note: This parameter is required if uses_parent_account = True. |
| active | boolean | optional | Status of the user |

### Update a Marqeta user

We can update a Marqeta user by making a PUT request to the {BASE_URL}/users/{token} endpoint. The path parameter ({token}) refers to the token of the user we want to update. We also need to specify the fields that we want to update in the body of the request.

## List Users 

In this lesson, we’ll look at a couple of useful endpoints that allow us to retrieve a list of all registered Marqeta users as well as a single Marqeta user’s information.

### Endpoints

#### Get all users

We can get a list of all users by making a GET request to the {BASE_URL}/users endpoint. This enlists all the active and non-active users. This endpoint allows us to filter the visibility of the response fields if required. This endpoint also supports pagination, which allows us to retrieve a specific range of resources from a complete and sorted list of returned resources.

#### Get user information

Similarly, we can retrieve the information of a single Marqeta user by making a GET request to the {BASE_URL}/users/{token} endpoint. The path parameter ({token}) refers to the token of the user whose information we want to retrieve. This endpoint allows us to filter the visibility of the response fields if required.

#### Request parameters

| Parameter | Type | Category | Description |
| token | string | required | Token of the user whose information we want to retrieve Note: This is a path parameter to get a single user. |
| fields | string | optional | A comma-separated list of fields we want like to retrieve Note: All fields are returned if this parameter is not supplied. This is a query parameter. |
| count | integer | optional | Number of users to retrieve Allowable values: 1–10 Note: This is a query parameter to get all users. |
| search_type | string | optional | Type of search Allowable values: query_then_fetch, dfs_query_then_fetch Note: This is a query parameter to get all users.
| sort_by | string | optional | Sorts by the given value Note: By default, the sorting is done in ascending order. To sort in descending sort, add a hyphen (-) to the field name. This is a query parameter to get all users.
| start_index | integer | optional | Sort order index of the first object in the array of returned resources Note: This is a query parameter to get all users. |

# Card Products

We can create a card product by making a POST request to the {BASE_URL}/cardproducts endpoint. We can provide basic information about the card product in the body of the request. We can also provide configuration information if we use the config object. This information defines the features and the behavior of the card product.

### Request parameters

`name`, `start_date`, `token`, `active`, `end_date`, `config`, 

### Update a card product

We can update a card product by making a PUT request to the {BASE_URL}/cardproducts/{token} endpoint. The path parameter ({token}) refers to the token of the card product to be updated. We also need to specify the fields that we want to update in the body of the request.


## List Card Products

### Endpoints

#### Get all card products

We can get a list of all card products by making a GET request to the {BASE_URL}/cardproducts endpoint. This gives us a list of all existing card products with their details. This endpoint also supports pagination, which allows us to retrieve a specific range of resources from the sorted list of returned resources.

#### Get a single card product

Similarly, we can get a single card product by making a GET request to the {BASE_URL}/cardproducts/{token} endpoint. The path parameter ({token}) refers to the token of the card product that we want to retrieve.

#### Request parameters

`token`, `count`, `sort_by`, `start_index`

# Cards

A card is a payment card that’s owned by a user. It can either be a physical or a virtual card. The behavior and the attributes of the card are defined by the card product object associated with it. We can also define the attributes of the card inside the card object. In that case, the definition inside the card object will take precedence over the definition inside the card product object.

## Create a card

We can create a Marqeta payment card by making a POST request to the {BASE_URL}/cards endpoint. We can provide basic information about the card in the body of the request. This includes the shipping information. We also need to specify the user_token of the card owner as well as the card_product_token of the card product that controls the card. Therefore, we need to create a user and a card product before we create a new Marqeta card.

### Request Parameters

| Parameter | Type | Category | Description |
| show_cvv_number | boolean | optional | True to show the CVV2 number in the response, otherwise False Note: This is a query parameter. |
| show_pan | boolean | optional | True to show the card’s PAN (primary account number) in the response, otherwise False Note: This is a query parameter. |
| card_product_token | string | required | Token of the card product |
| expedite | boolean | optional | True when we want to request the fulfillment provider to expedite card processing, otherwise False Default value: False |
| metadata | object | optional | Adds metadata provided by the customer to the card Allowable values: Maximum 20 key-value pairs allowed Format: "my_name_1": "my_value_1" |
| expiration_offset | object | optional | Defines the duration for card validity after issuance |
| token | string | optional | Unique token of the card Length: 1–36 characters Note: If not specified, the system generates one automatically. This value cannot be updated once set.
| user_token | string | required | Unique token of the card user |
| fulfillment | object | optional | Contains shipping information and the physical characteristics of the card |
| reissue_pan_from_card_token | string | optional | Reissues the specified card and assigns the new card the same PAN and PIN (personal identification number) but a new expiration date and CVV2 number Maximum length: 36 characters | translate_pin_from_card_token | string | optional | Assigns the newly created card the same PIN as the specified card Maximum length: 36 characters Note: Both cards must belong to the same user. Additionally, reissue_pan_from_card_token must not be set.
| activation_actions | object | optional | Contains actions to perform at card activation Note: The fields in this object are mutually exclusive.
| bulk_issuance_token | string | optional | Token of the bulk card order to link the card to Note: This field cannot be updated once set. Maximum length: 36 characters |

## Create card transition

Card transition refers to when we set the state of an existing card. All cards are inactive upon creation and require us to activate them. We can set the state of an existing card by making a POST request to the {BASE_URL}/cardtransitions endpoint.

### Request parameters

card_token, channel, state, token, reason, reason_code, validation,

## Update a card

We can update a card by making a PUT request to the {BASE_URL}/cards/{token} endpoint. The path parameter ({token}) refers to the token of the card to be updated. We also need to specify the fields that we would like to update in the body of the request.

### Request Parameters

token, user_token, expedite, fulfillment, metadata

# General Purpose Accounts

## GPAs and Balances

A general purpose account (GPA) is a user’s default account. Funds are transferred from a funding source to a user’s GPA.

### Types of GPA balances

Let’s take a look at the different types of GPA balances that are available for a user or a business:

* In regards to standard funding, a ledger balance is an amount that refers to available funds. This includes those from authorized transactions that are yet to be cleared. In regards to Just-in-Time (JIT) funding, this refers to authorized funds that are yet to be cleared and are currently on hold.

* Available balance refers to the user’s purchasing power. This is the amount that results from the deduction of authorized transactions that are yet to be cleared from the ledger balance. This balance is 0.00 if the user uses JIT funding.

* Pending credits refer to the ACH loads that are accepted but are still pending clearance.

* Cached balance and credit balance are not used at this time.

### Get GPA balances

We can get all GPA balances for a user or a business by making a GET request to the {BASE_URL}/balances/{token} endpoint. The path parameter ({token}) refers to the token of the user or business whose GPA balances we want to get. This endpoint also provides us with a link to the GPA balances of the specified user or business in the response.

## Gpa Orders

Funds are transferred from a funding source into a user’s GPA through GPA orders, which are either funded by our payment card program or by the user. We can also use GPA orders to transfer funds from a user’s funding source into our program’s funding source.

In this lesson, we’ll learn how to create a GPA order. We’ll also learn to retrieve a specific GPA order with its unique token.

### Create a GPA order

We can create a GPA order by making a POST request to the {BASE_URL}/gpaorders endpoint. This allows us to fund a user’s GPA. We must specify the user_token or the business_token in the body of the request to indicate the account we want to fund.

### Get GPA order information

We can get information for a GPA order by making a GET request to the {BASE_URL}/gpaorders/{token} endpoint. The path parameter ({token}) refers to the token of the GPA order that we want to retrieve.

## GPA Unloads

### Create a GPA unload

We can unload a GPA order by making a POST request to the {BASE_URL}/gpaorders/unloads endpoint. This allows us to return the funds from the GPA to the funding source. We must specify the token of the original GPA order that we want to unload in addition to the amount to be returned. This amount must be less than or equal to the amount of the original GPA order.

### Request Parameters

amount, original_order_token, funding_source_address_token, token, lags, memo

### Get GPA unload information

We can get information about a GPA unload by making a GET request to the {BASE_URL}/gpaorders/unloads/{unload_token} endpoint. The path parameter ({unload_token}) refers to the token of the GPA unload that we want to retrieve.

# Transactions

## Simulate and Reverse a Transaction

A transaction is the process of making a payment. We can use a Marqeta payment card to make a payment. An authorization transaction request includes the authorization details provided by the user and generates an electronic message that contains information used for payment processing.

### Simulate an authorization transaction

We can simulate an authorization transaction by making a POST request to the {BASE_URL}/simulate/authorization endpoint. This endpoint requires the card_token and other authorization details to accompany the request.

###  Simulate a transaction reversal#

We can simulate a reversal of an authorization transaction by making a POST request to the {BASE_URL}/simulate/reversal endpoint. This endpoint requires the values for original_transaction_token and amount to accompany the request. A reversal of the transaction returns the funds to the account from which the transaction was originally made. This is done when the hold placed on the funds by the authorization transaction is released.


## List Transactions

### Endpoints

#### Get all transactions

We can get a list of all transactions by making a GET request to the {BASE_URL}/transactions endpoint. This endpoint allows us to filter the visibility of the response fields, if necessary. This endpoint also supports pagination, which allows us to retrieve a specific range of resources from a complete and sorted list of the returned resources.

#### Get transaction details

We can get details of a single transaction by making a GET request to the {BASE_URL}/transactions/{token} endpoint. The path parameter, {token}, refers to the token of the transaction that we want to retrieve. This endpoint allows us to filter the visibility of the response fields, if necessary.


# Appendix

### Get all transactions

Some common transaction types include the following:

* account.credit
* account.debit
* balanceinquiry
* authorization
* authorization.atm.withdrawal
