# Writing your first React with GraphQL and Apollo Client

The <b>Apollo toolset</b> can be used to create a GraphQL client, GraphQL server, and other complementary applications, but for now, we will use the Apollo Client for your React client-side application. Along the way, we will build a simplified GitHub client that consumes [GitHub’s GraphQL API](https://docs.github.com/en/graphql) using Apollo instead of using plain HTTP requests as we did in one of the previous chapters.

<b>Apollo Client</b> can be used to perform queries and mutations.

Let’s now focus on using Apollo Client in React by building another client application. Basically, you will learn how to:

* connect the data-layer to the view-layer

* send queries and mutations from the view-layer

* update the view-layer to reflect the results

* use GraphQL features like pagination, optimistic UI, caching, local state management, and prefetching with Apollo Client in React.

Regarding the repository, the folders primarily represent React components. Some components will be reusable UI components such as the Input and Link components, while other components like Repository and Profile components are domain specific for the GitHub client application. Moreover, the constants folder has only one file to specify the application’s routes, which will be introduced later. You may want to navigate from a page that shows repositories of an organization (Organization component) to a page which shows your repositories (Profile component).






































