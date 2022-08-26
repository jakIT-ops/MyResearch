## Next.js is a React Framework

## Client-Side Rendering vs. Server-Side Rendering

### Client-side rendering

First, let’s talk about what happens when you use client-side rendering on your application. When you create React apps using only React or the CLI command create-react-app, you are building an application that has a basic HTML file that calls one or more JavaScript files. That JavaScript creates and loads all of your HTML into the site by injecting it into the document object model dynamically. This all happens on the client side.

### Server-side rendering
When applications are using server-side rendering, the client receives a full HTML document. The server will access all the required data and run the JavaScript. It creates the page and sends it in its entirety back to the client.
