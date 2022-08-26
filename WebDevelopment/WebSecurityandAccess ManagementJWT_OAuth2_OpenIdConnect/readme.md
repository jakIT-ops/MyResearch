# 1. Getting started with Web Application Security

### What is web application security?

Web application security deals with securing websites, mobile apps, and web APIs. Hackers subject web applications to different kinds of attacks, with the objective of stealing data or defacing a website.

Types of attacks differ based on the mode of attack and the attacker’s objective. Common web attacks include SQL Injection, Cross-site scripting attack, Cross-site Request forgery, and Denial-of-Service attack. We will discuss some of them in the upcoming lessons.

### Why do we need to secure web applications?

As many things are moving online, attackers have easier access to information shared on the internet. Millions of financial transactions take place over the Internet every day, and large amounts of private data is shared. If a web application is not secured, then it can cause a considerable loss to its users. To safeguard the interest of its users, the owners of any given website must take the necessary steps to prevent attacks. It is the responsibility of the website owners to put a proper system in place so only the intended users can view its data and perform actions on the website.

## Cross-site Scripting Attack (XSS)

The Cross-site Scripting attack, also known as XSS attack, is a kind of attack in which a malicious script is added to a website. When a user accesses this website then they accidentally run this malicious script, compromising their data as the attacker gets control of the user’s browser.

## Cross-site Request Forgery (CSRF)

Cross-site Request Forgery (CSRF), is an attack that tricks a web browser into executing an unwanted action in an application after a user logs in. It allows an attacker to force a logged-in user to act without their consent or knowledge.

In a CSRF attack, the attacker cannot access the data because the attacker does not have access to the response. This can be devastating, as the attacker can force the user to transfer funds from a banking website or share sensitive information.

### How does CSRF work?

To perform a CSRF attack, a few conditions should be met.

1. Cookie-based session handling – The user has already logged in into the website that is being attacked, and the website relies on cookies to identify the user.

2. No unpredictable request parameters – The requests that perform the malicious action do not contain any parameters whose values the attacker cannot determine or guess. For example, when tricking a user into transfering funds, the attacker must not be required to know the password of the user.

# 2. HTTPS Basics

## What is Encryption

Today, many people use the Internet for communication, sharing data, banking, shopping, and lots of other stuff. The problem with this level of use is the rapidly increasing threat of cybercrime, and other intrusions on your privacy. A hacker might be listening to our data while it is being transferred over the network. This is troublesome if we are sending sensitive data like passwords.

One of the best ways to protect the data transferred over the Internet is encryption.

Encryption is a way of converting plaintext into ciphertext (an encoded text that is not understandable by the third party). Encryption requires the use of an encryption key and an encryption algorithm. The key is used to encrypt/decrypt the plaintext into ciphertext. How that key is used to encrypt the plaintext is defined by the encryption algorithm. Both the receiver and the sender must have the encryption key.

### Types of encryption

There are two main types of encryption:

#### 1. Symmetric Encryption

In symmetric encryption, the same key is used for both encryption and decryption. Here’s a good analogy to explain how symmetric encryption works:

Suppose John needs to send a message to Carl. John will put a message in a box and will lock the box. Carl already has a duplicate copy of the key which was used to lock the box. Carl will receive the box and will unlock it using the key. This is symmetric encryption. Symmetric encryption is much faster than asymmetric encryption and is used to encrypt a large amount of data.

The disadvantage of this encryption type is that the sender and receiver will have to send their key to each other. An attacker may access this key while in transit and will be able to read all the messages. The keys used in symmetric encryption are not very large, as the max length is 256 bits.

#### 2. Asymmetric Encryption

In asymmetric encryption, the sender and receiver use a separate key to encrypt and decrypt the message. This is also known as PKI (Public Key Infrastructure). The advantage of this encryption is that the keys are not transferred over the network. So, it is much safer than symmetric encryption. This encryption is achieved through a public-private key model.

The recipient sends a public key to all the senders. The senders then encrypt the messages using this public key. When the receiver receives the message, it uses its private key to decrypt the message. The keys used in asymmetric encryption are fairly large and can be around 2048 bits.


### What is an encryption algorithm?

An encryption algorithm is a mathematical formula used to transform data into ciphertext. An encryption algorithm uses an encryption key to transform plaintext into ciphertext. The ciphertext can be changed back to plaintext using a decryption algorithm and the decryption key.

Below are some of the commonly used encryption algorithms:

* AES
* DES
* Blowfish
* TwoFish
* RC4, RC5, RC6


### What is a brute force attack?

In a brute force attack, an attacker tries to guess the decryption key. The attacker is not required to do this manually, and there is computer software that performs the same actions. To prevent this from happening, the key should be very strong, so that it becomes impossible for the computer to try all the combinations.

Let’s see what we mean by a strong key. We know that data is represented by bits in computing language. Each bit can have a value of 0 or 1. If a key is 2 bits long then there are four possible combinations, i.e. 00, 01, 10, 11. This is very easy for computers to crack.

Let’s take a key which is 256 bits long. The total number of possible combinations are 2^{256}
2
256

. A 256-bit private key will have 115, 792, 089, 237, 316, 195, 423, 570, 985, 008, 687, 907, 853, 269, 984, 665, 640, 564, 039, 457, 584, 007, 913, 129, 639, 936 possible combinations. No supercomputer can crack that in any reasonable timeframe. So, to prevent brute force attacks, the key should be of sufficient length.


## What are SSL certificates?

When a user accesses a website, data is transferred between the client (browser) and the server (website). This data is not safe to send in the clear because it may be read by an attacker. This is a problem if we are sending sensitive data like credit card details, passwords, or personal information over the Internet.

SSL (Secure Sockets Layer) certificates create an encrypted environment between a client and a server. A Secure Sockets Layer certificate (SSL certificate) is a small data file installed on a Web server that allows for a secure connection between the server and a web browser.

The certificate is base64 encoded and contains the following information:

* Name of the entity to which the certificate was issued.
* The public key required for encryption and digital signature verification.
* The digital signature created with the private key of the certificate issuer.

## Benefits of using HTTPS over HTTP

There are few benefits of using HTTPS instead of HTTP:

1. Authenticity

HTTPS ensures that the client is talking to the intended website. It is not possible for an attacker to respond to the client’s requests. In HTTPS, the website provides its identity to the client.

2. Confidentiality

HTTPS ensures that the data that is being transferred between the client and server is secure and an attacker cannot read it. This is achieved by encrypting the data in HTTPS.

3. Message Integrity

HTTPS ensures that the data is not modified by an attacker while it is being transferred over the Internet. It gives the client and server a way to verify that the data has not been tampered with.

## How does HTTPS work?

In HTTPS, before transferring any data, the client first verifies that the server it is talking to is the correct server and how the data will be encrypted. This process is called the TLS handshake.

TLS handshakes are a series of datagrams, or messages, exchanged by a client and a server. A TLS handshake involves multiple steps, as the client and server exchange the information necessary for completing the handshake and making further conversation possible.

The exact steps within a TLS handshake will vary depending upon the kind of key exchange algorithm used and the cipher suites supported by both sides.

Step 1 -> The ‘client hello’ message

Step 2 -> The ‘server hello’ message

Step 3 -> Certificate Validation

Step 4 -> Pre-master secret

Step 5 -> Session Key creation

Step 6 -> Client Finished

Step 7 -> Server Finished

Step 8 -> Symmetric encryption successful

### What are Cookies

HTTP cookies, or web cookies, are small text files that store small pieces of information. They are created by the websites we visit and are stored on our browser. Cookies are limited to 4kb in size, which means they cannot store large amounts of data.

A cookie generally contains:

1. name - A website or a third-party server identifies a cookie using its name.

2. value - A random alphanumeric character, and it stores data like a unique identifier to identify the user and other information.

3. attribute – A set of characteristics such as the expiration date, domain, path, and flags.

### Types of Cookies

Based on the source, the cookies can be classified into two types:

#### First-party cookies

* These are installed by the website that the user is currently on.
* They are normally used to determine whether a user is logged in.

#### Third-party cookies

* These are installed by other websites or third-party servers that are not being viewed by the users.
* Third-party cookies are used to track users’ browsing patterns and interests to show relevant advertisements.
* You may have noticed that when you search for a product on an eCommerce website, then you start seeing the ads for that product on other websites. This is achieved through third party cookies.

Based on the validity, the cookies can be classified into two types:

#### Session cookies

* Session cookies are created for a single session and vanish once you close the browser.
* These cookies are created by the website and the user cannot disable them from the browser.
* These cookies are used to save session information while users browse a website. As soon as we close the browser, these cookies expire.

#### Permanent cookies

* Permanent cookies don’t expire even after we close the browser or even shut down the computer.
* They have a specific expiration date set by the website and remain valid until then.
* Suppose we log in to a website and after a few days, when we try to login again, then we don’t need to re-enter the username and password. This becomes possible because of permanent cookies.
* Since these cookies store sensitive information, it’s not safe and can be risky if people with malicious intentions somehow get access to our computer.

# 3. JSON Web Token

HTTP is a stateless protocol. This means that each HTTP request is considered an independent request and no information from the previous request is saved. If the application is static and it is available to everyone, then we don’t have any problems. We just need to inform the server which page we want to access, and we will get the result. If the application is dynamic, then we may need to send additional information regarding who is accessing the page.

## Introducing Session-based authentication

If you look at the above example, we need to send our login information each time an HTTP request is made to the server.

This is not a good practice and can be frustrating for the user. To solve this issue, session-based authentication comes into the picture. It is also known as cookie-based authentication.

Below are the steps to create a session between a user and a web server.

1. The user (normally a browser) sends a request to the server. The request contains the login credentials of the user and the info it is requesting.

2. The web server authenticates the user. It creates a session and stores all the information about the user in memory or a database and returns a sessionId to the user.

3. This sessionId is stored by the user in browser cookies. The next time the user makes a request it sends the cookies as well in the HTTP header.

4. The web server looks at the sessionId and checks if it has any info regarding this sessionId.

5. If the sessionId is valid then the web server recognizes the user and returns the requested information.

## Token Based Authentication

In the previous lesson, we discussed that in session-based authentication, the user information is stored on the server. This resulted in lots of issues related to performance and scalability. But what if we don’t want to save the user information on our server? We can’t save the user information in cookies as they have a size limit and also it is not safe.

We have an alternative to cookies, and that alternative is tokens. A token can store all the user information in an encrypted format and this token can be stored on the client-side.

Here is the basic flow of token-based authentication:

1. The client sends a request to the server with a username/password.
2. The application validates the credentials and generates a secure, signed token for the client.
3. The token is sent back to the client and stored there.
4. When the client needs to access something new on the server, it sends the token through the HTTP header.
5. The server decodes and verifies the attached token. If it is valid, the server sends a response to the client.
6. When the client logs out, the token is destroyed.

## Types of Tokens

There are basically two token types:

1. Access Tokens

2. Refresh Tokens

Access tokens are used to grant access to a protected resource. When a client first authenticates it is given both types of tokens, but the access token is set to expire after a short period. By doing this, even if someone manages to get access to your token, it can be used only for some time.

Refresh tokens are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with an identical or narrower scope. It does not need the credential information again. The refresh token is also valid for some duration, but it is much more than an access token.

## JWT - JSON Web Token

A JSON Web Token (JWT) is a standard that defines a safe, compact, and self-contained way of transmitting information between a client and a server in the form of a JSON object. A JWT can either be signed (JWS) or encrypted (JWE) or both. If a JWT is neither signed nor encrypted, then it is called an insecure JWT.

### Common use cases for using JWT

Here are some use cases in which JSON Web Tokens are useful:

`1) Authorization`

One of the most important use cases of JWT is the authorization. Suppose we are using an application that needs some data from our Gmail. We can authenticate ourselves on the Gmail authentication server by providing credentials. Gmail will provide us with a JWT, which our application can use to get data from Gmail. The token will contain information regarding what data can be accessed.

`2) Information Exchange`

JWT can also be used to share certain information between two parties secretly.

## JWT Validation

In this lesson, we will look at how JWTs can be used as an authentication and authorization mechanism. As mentioned in the previous lesson, we will be discussing signed JWTs.

Here is the basic flow of JWT authentication:

1. The client sends a request to the server with user credentials.
2. The server generates a signed JWT for the client if the credentials are valid.
3. The server sends the token back to the client which is stored in the browser.
4. For every subsequent request, the client sends the token back to the server.
5. The server validates the token, and if it is valid then grants access to the client.


# 4. OAuth Introduction

Consider we want to use a new app called PicsArt, which allows us to beautify our images. We just need to upload our images and this app gives us some options to edit our images.

This app provides us a few methods to upload images, such as from the phone gallery or a direct upload from our social media accounts like Facebook or Instagram.

The problem is, the PicsArt app needs access to our Facebook account to access our images.

Here are a few methods to solve this problem:

In the first method, we can share the credentials with the client app which it can use to access our images

1. The PicsArt app will ask us to provide our Facebook credentials.

2. The app will use those credentials to access our images from Facebook.

## What is OAuth 2.0?

OAuth 2.0 is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity while providing specific authorization flows for web applications, desktop applications, mobile phones, and living room devices.

## OAuth Terminologies

### Resource owner

The resource owner is the owner of the resource that is being accessed. When you log in to PicsArt App using your Facebook account, you are granting access to PicsArt to access your images. In this case, you are the resource owner.

### Client

The client is an application that accesses protected resources on behalf of the resource owner. The client could be hosted on a server, desktop, mobile, or other devices. In our example, the PicsArt app is the client.

### Resource server

The server that is hosting the protected resources and is capable of accepting and responding to requests by clients using access tokens. In our example, Facebook is the resource server.

### Authorization server

The server which issues access tokens after successfully authenticating a client and resource owner is called authorization server. In our example, the Facebook server was issuing the access token. Normally, there is a separate server that does this task.

### Authorization grant

An authorization grant is a credential representing the resource owner’s authorization (to access its protected resources) used by the client to obtain an access token. The OAuth specification defines four grant types, which we will discuss in the upcoming lessons.

### Authorization code

In our example, we showed that the Facebook App shared a token with the client. In some OAuth flows, the authorization server does not give the access token directly. It first issues an authorization grant. The client then sends this grant with the client secret (more on this later) to the authorization server. After this, the authorization server gives access token to the client.

### Access token

Access tokens are credentials used to access protected resources. An access token is a string representing an authorization issued to the client. Tokens represent specific scopes and durations of access, granted by the resource owner, and enforced by the resource server and authorization server.

### Scope

Scope defines the permissions of a token. It defines what resources can be accessed using a given access token. In our example, the client app wants to access only images, so the images are scope.


# OpenID Connect

OAuth 2.0 is designed only for authorization. It is used for granting access to data and features from one application to another. In OAuth, the client is given a token which it uses to access the data on the resource server, but it doesn’t get to know anything about the user. OAuth was used for authentication as well, but since it was not designed for authentication it was extended further to support authentication.

OpenID Connect is an extension of OAuth. It is a thin layer above OAuth which adds support for authentication.
