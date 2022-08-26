# 1. My First Query

Before we start building full-fledged GraphQL applications, let’s explore GraphQL with the tools we have installed in the previous chapter. You can either use GraphiQL or the GitHub’s GraphQL Explorer. In the following lessons, you will learn about GraphQL’s fundamentals by executing your first GraphQL queries and mutations. We will even further explore features such as pagination in the context of GitHub’s GraphQL API.

### GraphQL Query with GitHub’s GraphQL API

Let’s start interacting with the GitHub API using queries and mutations without React. This will allow you to use your GraphiQL application or GitHub’s GraphQL Explorer to make GraphQL query requests to GitHub’s API. Both tools should be authorized to make requests using a personal access token as explained in the previous chapter. On the left-hand side of your GraphiQL application, you can fill in GraphQL queries and mutations.

```graphql
{
  viewer {
    name
    url
  }
}
```

### GraphQL Objects

```graphql
{
  "data": {
    "viewer": {
      "name": "Robin Wieruch",
      "url": "https://github.com/rwieruch"
    }
  }
}
```

# 2. Queries and Organizations

### GitHub Organization

Organizations are shared accounts where groups of people can collaborate across multiple projects at once.

To specify a GitHub organization, you can pass an argument to a field:

```graphql
{
  organization(login: "the-road-to-learn-react") {
    name
    url
  }
}
```

#### Identifying an Organization

When using GitHub’s API, you can identify an organization using a `login`. If you have previously used GitHub, you might know this is part of the organization URL: `https://github.com/the-road-to-learn-react`.

```graphql
{
  "data": {
    "organization": {
      "name": "The Road to learn React",
      "url": "https://github.com/the-road-to-learn-react"
    }
  }
}
```

### GraphQL Aliases

If you ever want to request data about two identical objects, you would have to use aliases in GraphQL. The following query would not be possible because GraphQL would not know how to resolve the two organization objects in a result:

```graphql
{
  book: organization(login: "the-road-to-learn-react") {
    name
    url
  }
  company: organization(login: "facebook") {
    name
    url
  }
}
```

```graphql
{
  "data": {
    "book": {
      "name": "The Road to learn React",
      "url": "https://github.com/the-road-to-learn-react"
    },
    "company": {
      "name": "Facebook",
      "url": "https://github.com/facebook"
    }
  }
}
```

### GraphQL Fragments

Next, imagine you want to request multiple fields for both organizations. Re-typing all the fields for each organization would make the query repetitive and verbose, so instead, we will use fragments to extract the query’s reusable parts. Fragments let you construct sets of fields, and then include them in queries where you need to. They are especially useful when your query becomes deeply nested and uses lots of shared fields.

```graphql
{
  book: organization(login: "the-road-to-learn-react") {
    ...sharedOrganizationFields
  }
  company: organization(login: "facebook") {
    ...sharedOrganizationFields
  }
}

fragment sharedOrganizationFields on Organization {
  name
  url
}
```

# 3. GraphQL Variables

```graphql
query ($organization: String!) {
  organization(login: $organization) {
    name
    url
  }
}
```

This defines the organization argument as a variable using the ＄ sign. Furthermore, the argument’s type is defined as a String and since the argument is required to fulfill the query, the String type has an exclamation point.

In the “Query Variables” panel, the variables would have the following content for providing the organization variable as an argument for the query:

```graphql
{
  "organization": "the-road-to-learn-react"
}
```

Essentially, variables can be used to create dynamic queries. Following the best practices in GraphQL, we don’t need manual string interpolation to structure a dynamic query later on. Instead, we provide a query that uses variables as arguments which are available when the query is sent as a request to the GraphQL API. You will see both implementations later on in your React application.

# 4. The Structure of a Query

### The Query Statement

Now, let’s take a step back to examine the structure of the GraphQL query. After we were introduced to variables, we encountered the query statement in our query structure for the first time. Before using the query statement, we used the shorthand version of a query in which we omitted the statement. However, as we are using variables, the query statement must be included. Try the following query without variables but with the query statement to verify that the longer version of a query works.

```graphql
query {
  organization(login: "the-road-to-learn-react") {
    name
    url
  }
}
```

The query statement is also called an operation type in GraphQL lingua; for instance, it can also be a mutation statement. In addition to the operation type, we can even define an operation name.

```graphql
query OrganizationForLearningReact {
  organization(login: "the-road-to-learn-react") {
    name
    url
  }
}
```

### Accessing a Nested Object

```graphql
query OrganizationForLearningReact(
  $organization: String!,
  $repository: String!
) {
  organization(login: $organization) {
    name
    url
    repository(name: $repository) {
      name
    }
  }
}
```

Provide a second variable to request a specific repository of the organization:

```graphql
{
  "organization": "the-road-to-learn-react",
  "repository": "the-road-to-learn-react-chinese"
}
```

# 5. GraphQL Mutations

### Mutation vs Query

GraphQL mutations complement GraphQL queries because they are used for writing data that queries can read. The mutation shares the same principles as the query: it has fields and objects, arguments and variables, fragments and operation names, as well as directives and nested objects for the returned result. When the mutation is valid, we should receive the updated data for the specified fields and objects in our query. Before we start making our first mutation, we need to be aware that we are using live GitHub data, so if you follow a person on GitHub using your experimental mutation, you will follow this person for real.

### Starring a GitHub Repository

In this lesson, we will star a repository on GitHub using a mutation from GitHub’s API. This would be the same repository we requested using a query in the previous lesson. The addStar mutation can be found in the “Docs” sidebar. The repository we will be working with is a project for teaching developers about the fundamentals of React so, starring it should prove useful.

```graphql
query {
  organization(login: "the-road-to-learn-react") {
    name
    url
    repository(name: "the-road-to-learn-react") {
      id
      name
    }
  }
}
``` 

In the results section in GraphiQL for the above query, we should see the identifier for the repository: `"MDEwOlJlcG9zaXRvcnk2MzM1MjkwNw=="`. Before using the identifier as a variable, we can structure your mutation in GraphiQL the following way:

```graphql
mutation AddStar($repositoryId: ID!) {
  addStar(input: { starrableId: $repositoryId }) {
    starrable {
      id
      viewerHasStarred
    }
  }
}
```

```graphql
{
  "repositoryId": "MDEwOlJlcG9zaXRvcnk2MzM1MjkwNw=="
}

```

# 6. GraphQL Pagination

### Why Do we Need Pagination?

This is where we return to the concept of pagination mentioned in the previous chapter. Imagine we have a list of repositories in our GitHub organization, but we only want to retrieve a few of them to display on our UI. It could take ages to fetch a list of repositories from a large organization. In GraphQL, you can request paginated data by providing arguments to a list field, such as an argument that specifies how many items you are expecting from the list.

```graphql
query OrganizationForLearningReact {
  organization(login: "the-road-to-learn-react") {
    name
    url
    repositories(first: 2) {
      edges {
        node {
          name
        }
      }
    }
  }
}
```

### Solution: Cursor Field

After executing the query, we should see two items from the list in the repositories field. However, we still need to figure out how to fetch the next two repositories in the list. The first result of the query is the first page of the paginated list, the second query result should be the second page. In the following code, we will see how the query structure for paginated data allows us to retrieve meta information to execute successive queries. This is done by allowing each edge to come with its own cursor field to identify its position in the list.

```graphql
query OrganizationForLearningReact {
  organization(login: "the-road-to-learn-react") {
    name
    url
    repositories(first: 2) {
      edges {
        node {
          name
        }
        cursor
      }
    }
  }
}
```

The result should be similar to the following:

```graphql
{
  "data": {
    "organization": {
      "name": "The Road to learn React",
      "url": "https://github.com/the-road-to-learn-react",
      "repositories": {
        "edges": [
          {
            "node": {
              "name": "the-road-to-learn-react"
            },
            "cursor": "Y3Vyc29yOnYyOpHOA8awSw=="
          },
          {
            "node": {
              "name": "hackernews-client"
            },
            "cursor": "Y3Vyc29yOnYyOpHOBGhimw=="
          }
        ]
      }
    }
  }
}
```





























