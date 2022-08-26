# Introduction

[FreshBooks](https://www.freshbooks.com/) was founded in 2003 as a web-based software as a service (SaaS) model. It provides many accounting services like invoicing, and tracking expenses, time, inventory, clients, payments, and much more. Its primary targets are small and medium-sized businesses. Users can access FreshBooks using a desktop or mobile.

# Clients

### Create a client

In this section, we’ll create a new client using the {base_url}/accounting/account/{ACCOUNT_ID}/users/clients endpoint. This endpoint utilizes the HTTP POST method to create a new client in our FreshBooks account. We’ll make payments and send invoices to this client in the next lessons.

### Request headers

Mostly, the headers of a request contain the following:

* `Content-Type:` This defines the format of our request, and normally its value is applications/json.
* `Authorization:` This defines the type of authorization used by FreshBooks endpoints. These endpoints utilize the Bearer token to authenticate whether the request is valid.

### Request parameters

email, fname, lname, organization, p_streetm p_city, p_province, p_code

### Response 

accounting_systemid, bus_phone, company_industry. currency_code, email, id, organization

### Update a client

Now that we’ve created a client, let’s try updating it. We have to give the ID of the client created at the end of the same endpoint as follows: users/clients/{CLIENT_ID}. L

## Add, Edit, and Delete a Secondary Contact

A client’s profile represents a company. Therefore, secondary contacts are like members of a company. Secondary contacts are useful in situations where we want to send emails or invoices to multiple contacts within the same organization. We can have multiple secondary contacts in a single client.

These operations are performed using the following endpoints:

* Add a contact: {base_url}/accounting/account/{ACCOUNT_ID}/users/clients/{CLIENT_ID}
* Get all contacts: {base_url}/accounting/account/{ACCOUNT_ID}/users/contacts
* Update and delete a contact: {base_url}/accounting/account/{ACCOUNT_ID}/users/contacts/{CONTACT_ID}

### Add a secondary contact

In this section, we create a contact in the client profile that we created in the previous lesson. The {base_url}/accounting/account/{ACCOUNT_ID}/users/clients/{CLIENT_ID} endpoint is similar to the one we used to update a client. In fact, this is an update operation with the difference of the contacts object.



