# 1. Introduction to Apollo Client

Apollo is best used as a new layer in your stack that sits between your services and your applications. It’s a combination of open source components, commercial extensions, and cloud services. Apollo is an entire ecosystem built by developers as an infrastructure for GraphQL applications. Apollo is designed for the needs of product engineering teams building modern, data-driven applications. You can use it on the client-side for a GraphQL client application, or server-side for a GraphQL server application. At the time of writing this course, Apollo offers the richest and most popular ecosystem around GraphQL in JavaScript. There are other libraries for React applications like Relay and Urql, but they are just for React applications, and they are not as popular as the Apollo Client. Apollo is framework agnostic, meaning you can use it with libraries other than React. It can be coupled with other libraries/frameworks like Vue and Angular as well, so everything you learn in this course is transferable to other frameworks as well.

Some of the advantages of Apollo Client also include it being small and self-contained, so you can just npm install apollo-client react-apollo and start loading data. Also, it is compatible with all GraphQL servers.

<br>
<div align="center">
	<img src="../img/apollo.png">
</div>
<br>


# 2. Starting with Apollo Boost 

### Apollo-Boost Package

The apollo-boost package gives access to a zero-configuration Apollo Client, and the [graphql](https://github.com/graphql/graphql-js) package allows GraphQL queries, mutations, and subscriptions on both the client and server. It is JavaScript’s reference implementation of [Facebook’s GraphQL specification](https://github.com/graphql/graphql-spec00).

```graphql
import ApolloClient from 'apollo-boost';
const client = new ApolloClient({
  uri: 'https://api.github.com/graphql',
});
```

### Configuring your Personal Access Token

The Apollo Client already works this way. Remember, however, that GitHub’s GraphQL API requires a personal access token. That’s why we have to define it once when creating the Apollo Client instance. Therefore, you can use the `request` property to define a function which has access to the context of each request made through the Apollo Client. There, we pass the authorization header using Apollo Boost as one of its default headers.

```graphql
import ApolloClient from 'apollo-boost';
const client = new ApolloClient({
  uri: 'https://api.github.com/graphql',
  request: operation => {
    operation.setContext({
      headers: {
        authorization: `Bearer YOUR_GITHUB_PERSONAL_ACCESS_TOKEN`,
      },
    });
  },
});
```

We did the same for the previous application in the previous chapter, using only axios for plain HTTP requests. We configured axios once with the GraphQL API endpoint to default all requests to this URI, and to set up the authorization header. The same happened here because it’s enough to configure your client once for all the following GraphQL requests.

Remember, we have to replace the `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` string with our personal access token that you created on GitHub’s website before. However, when you are locally executing this code, you may not want to put your access token directly into the source code, so you can create a `.env` file which holds all of your environment variables in the project folder.

```graphql
import ApolloClient from 'apollo-boost';
import 'dotenv/config';
const client = new ApolloClient({
  uri: 'https://api.github.com/graphql',
  request: operation => {
    operation.setContext({
      headers: {
        authorization: `Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}`,
      },
    });
  },
});
```













