## What is HATEOAS?

> HATEOAS stands for "Hypermedia as the engine of application state"

Its complicated acronym. Let's decode it for you.

What do you see when visit a web page?

The data that you would want to see. Is that all? You would alse see links and buttons to see related data.]

For example, if you go to a student page, you will see

* Student profile

* Links Edit and Delete Student details

* Links to see details of other students

* Links to see details of the courses and grades of the student

HATEEOAS brings the same concepts to Restful Web Services.

When some details of a resource arre requested, you will provide the resoucre details as will ass details of related resources and the possible actions you can perform on the resouce. For example, when requesting information about a facebook user, a Rest service can return the following

* User details

* Links to get his recent posts

* Links to get his recent comments

* Links to retrieve his friend's list

## What is Content Negatiation

> REST stands for Representional State Transfer

Key abstraction in Rest a Resoirce. There is no restriction on what can be a resource. A todo is a resource. A person on facebook is a resource.

A resource can have mutliple reporesentations

* XML

* HTML

* JSON

When a resoirce is requested, we proivde the representation of the resource.

When a consumer sends a request, it can specify two HTTP Headers related to Content Negotiation

* Accept and

* Content-Type

Content-Type indicates the content type of the body of the request.

Accept indicates the expected content type of the response


# Versioning RESTful Services - Spring Boot REST API

### Why do we need to version our RESTful API?

The best approach to versioning is NOT to do it. Yeah, that’s right. Do not version as long as versioning is not needed.

> Build your services to backward compatible so that you can avoid versioning as much as possible!

However there are a number of situations where versioning is needed.

Let’s consider an example.

You had this version of the student service initially


```json
{
  "name": "Bob Charlie"
}
```

At a later point, you wanted to split the name up. So, you created this version of the service.

```json
{
  "name": {
    "firstName": "Bob",
    "lastName": "Charlie"
  }
}
```

You can support both these requests from the same service, but it becomes complex as the requirements diversify for each of the versions.

In these kind of situations, versioning becomes mandatory.

Let’s create a simple project and understand the 4 different approaches to versioning your RESTful services.


