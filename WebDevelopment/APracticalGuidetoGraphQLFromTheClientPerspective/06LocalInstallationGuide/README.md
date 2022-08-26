# 1. Installing Packages to Use React with GraphQL

For the purpose of this course, all the required packages are installed beforehand for the in-browser environment. However, if you want to further practice on your local browser, you can follow the installation guide in this chapter to help you install the required packages to get started locally.

```graphql
npm install -g create-react-app
```

Now, let’s create the application with create-react-app. In your general projects folder, type the following instructions:

```graphql
create-react-app react-graphql-github-vanilla
cd react-graphql-github-vanilla
```

After your application has been created, you can test it with npm start and npm test.

The following application will focus on the src/App.js file. It’s entirely up to you to split out components, configuration, or functions to their respective folders and files.

```graphql
npm install axios --save
```

Replace the YOUR_GITHUB_PERSONAL_ACCESS_TOKEN string with your own personal access token. To avoid cutting and pasting your access token directly into the source code, you can create a .env file to hold all your environment variables on the command line in your project folder. If you don’t want to share the personal token in a public GitHub repository, you can add the file to your .gitignore.

```graphql
touch .env
```

Environment variables are defined in this .env file. Be sure to follow the correct naming constraints when using create-react-app, which uses REACT_APP as prefix for each key. In your .env file, paste the following key value pair. The key has to have the REACT_APP prefix, and the value has to be your personal access token from GitHub.

```graphql
REACT_APP_GITHUB_PERSONAL_ACCESS_TOKEN=xxxXXX
```

# 2. Installing Packages to Use Apollo Client with GraphQL

To get started, find the Node.js boilerplate project and its installation instructions. You will use Apollo Client on the command line in a Node.js environment for now. On top of the minimal Node.js project, you will introduce the Apollo Client with Apollo Boost to experience the GraphQL client without a view-layer library.

In the following, you will consume GitHub’s GraphQL API, and then output the queries and mutation results in the command line. To do this, you need a personal access token on GitHub’s website, which we covered in a previous chapter. If you haven’t done it yet, head to GitHub’s instructions to generate a personal access token with sufficient permissions.

```graphql
npm install apollo-boost graphql --save
```

### Install `dotenv`

Note: There may be additional configuration steps for the previously installed dotenv package. Since the installation instructions may vary with different dotenv versions, check their GitHub website after you have installed it to find the best configurations.

```graphql
npm install cross-fetch --save
```






























