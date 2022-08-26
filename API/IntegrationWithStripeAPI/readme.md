## What is Stripe?

### Stripe overview

To better understand what Stripe is, you should first know what a payment gateway is. On an e-commerce site or mobile app, you take the customer’s billing information and pass it along to a payment gateway. A payment gateway is an intermediary between the credit/debit card companies and the business account. The payment gateway confirms that the charge can be made for the given card information and sends the charge details to the business account. The same charge details are also passed to the app making the payment request.

Stripe is one of the prime payment gateways. It enables businesses and individuals to accept payments using their rich API and robust platform. Stripe makes it easier for business owners and vendors to start and manage their internet businesses by providing various payment solutions.

### Features

* <b>Payments for business</b> — Stripe provides a complete set of solutions to businesses and platforms that own e-commerce shops. These solutions allow them to manage subscription billing and enable them to accept payment through various channels.

* <b>Easy activation</b> — Stripe onboarding is very user-friendly. You can create an account in minutes and get started with the libraries and SDKs to accept payment.

* <b>Optimized revenue</b> — Stripe uses machine learning techniques to detect fraud and increase authorization rates for every transaction.

* <b>Global reach</b> — Businesses can use different payment methods made available by Stripe to accept payment globally and increase the conversion rate significantly.

* <b>Developer-friendly</b> — Stripe libraries and SDKs are production-build-ready and have excellent support for integration with legacy applications. By using the Stripe development platform, you can accept payments simply and focus more on customer and product experience.

### Prerequisites for the course

This course assumes that you are skilled at JavaScript, React, NodeJS, and knows how MERN stack applications work and how to get them running on your local machine. If you are not adept at these technologies, please continue learning, and take this course after you are comfortable with them. This course is designed for candidates who want to learn about Stripe SDKs and libraries (both client and server) to enable payments in their apps and expand their skill set.

#### Understanding the regulatory terms

As a developer, you must understand different regulations and terminologies associated with processing online transactions. Being up-to-date with new security standards is just as important as developing secure payment flows. Failing to support new regulations will result in payments being declined by the issuing bank.

#### Second Payment Services Directive (PSD2)

Second Payment Services Directive (or PSD2) is the latest and revised regulation in Europe that focuses on making payments safer and more secure. It mandates customers to set up 3D Secure, push banks to use protocols like SCA, and modern technologies to facilitate open banking.

#### Post Card Industry (PCI) Compliance

The entities — Stripe or any businesses — involved in the processing, transferring, or storing of sensitive data like card details must adhere to the rules mentioned in the Payment Card Industry (PCI) Data Security Standards.

#### Strong Customer Authentication (SCA)

Strong Customer Authentication is a regulatory requirement that needs to be enabled by the customers to use a two-factor authentication process — like 3D Secure — to verify their payment. Merchants need to support SCA to charge the customer and prevent rejection from the customer’s bank.

#### 3D Secure

3D Secure is a protocol developed to enable additional authentication for card transactions. It protects merchants from counterfeit payments.

#### Card authentication

Card authentication is an additional step that needs to be performed by the customer to authorize the payment. The bank sends a verification code to the customer’s email or mobile number, which is then entered in a secure channel sent by the bank.

# 1. Understanding Api

## 1.1 Stripe API Keys and Intents

The Stripe API is built around the REST paradigm. Stripe API accepts form-encoded request bodies and returns JSON responses along with standard HTTP status codes.

Stripe has excellent server-side libraries for Ruby, Python, NodeJS, PHP, .NET, and Go. If you like being old-school, you can just use curl in your terminal to test the APIs.

Throughout this course, you will be closely working with the stripe npm library for NodeJS.

Before proceeding, you need to get the Developer API keys from the Stripe dashboard.

### Payment Intents

Payment Intents are used to build payment systems that can handle complexity. The Payment Intents API has the ability to trail the payment from initialization through the entire checkout flow and invoke additional verification steps as and when needed.

Additional processes like custom fraud rules, regulatory mandates, redirect-based payment methods, etc. can trigger additional authentication steps. If these cases are not handled by the payment integration, the transaction will not complete and will eventually fail, leading to a poor user experience.

Stripe’s Payment Intent API offers the following:

* Automatic authentication handling

* Zero double charges

* Support for Strong Customer Authentication (SCA)

The Payment Intents API can be used with Payment Methods and Setup Intents APIs to build a complete integration that can handle complex cases and additional authentication steps like 3D Secure.

The Payment Intents API’s integration comprises two steps:

1. Creating a Payment Intent

2. Confirming the Payment Intent

### Setup Intents

Setup Intents API is used to set up payment methods for future payments. You can save payment credentials and optimize them for future use. This can be useful for businesses that don’t charge the customer right away and only initiate the payment process once the service has been provided. For example, hotel owners can collect the card details for verification purposes and only charge the customer once they checkout from the hotel.

## 1.2 Interacting with Stripe API

### Authentication

The Stripe API provides API keys so that it can authenticate your requests. API key grants complete access to your account and hence it must be stored securely and should not be pushed to any public repositories.

Let’s use the secret key to start interacting with Stripe. You need to provide this key in the following widget. As soon as you provide the key, it’s stored in the `SECRET_KEY` variable in line 3. We then pass this key to the `Stripe()` function in line 5, which returns an object that will be used to make further requests.

```js
const Stripe = require("stripe");

const SECRET_KEY = "{{SECRET_KEY}}";
console.log(SECRET_KEY)
const stripe = Stripe(SECRET_KEY);
```

### Getting a single product

```js
const Stripe = require("stripe");

async function getSingleProduct(stripe) {
    const product = await stripe.products.retrieve("{{PRODUCT_ID}}");
    console.log(product);
}

const SECRET_KEY = "SECRET_KEY";
const stripe = Stripe(SECRET_KEY);
getSingleProduct(stripe);
```

### Listing all products

The `products.list()` method can be used to list all the products in your account.

```js
const Stripe = require("stripe");
const SECRET_KEY = "SECRET_KEY";
const stripe = Stripe(SECRET_KEY);

async function listAllProducts() {
    const products = await stripe.products.list();
    console.log(products);
}

listAllProducts();
```

You can pass a params object to this method to pass additional parameters like limit, ids, etc. For example, the following implementation of listAllProducts() retrieves only three products. You can test this code by placing it in the widget above.




























