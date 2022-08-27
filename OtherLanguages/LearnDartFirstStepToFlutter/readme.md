# A Bit About Dart

## Dart: A History

Dart 1.0 was released on November 14th, 2013 by Google and was founded by Lars Bak and Kasper Lund. It aims to help developers build modern web and mobile applications. It covers client, server, and now mobile with Flutter. Coming with a range of tools including a virtual machine, core libraries and package management repository, it lends enough ammunition for you to get started on your next project.

## Dart is Object-Oriented

Smalltalk was released in the 1970s and was one of the first pure object-oriented programming languages. You can now find object-oriented programming everywhere. It has dominated the world of programming languages.

The concept behind object-oriented programming is quite simple: all but the most trivial programs require a particular form of structure.

The most clear-cut way of achieving this particular structure is by using the concept of storage containers. A programming language can be divided into data and operations to be performed on data. We can store specific data and operations in some type of container. Furthermore, these containers are made to be general. Hence, they not only store data and operations but they are themselves values that can be stored in other containers and passed as parameters to other operations. In object-oriented programming, these containers are known as objects.

## Dart: Through the Eyes of JavaScript

Dart is a clean, simple, class-based object-oriented language that has more structure than JavaScript, the programming language it is heavily based on. It’s great for developers that are interested in having a structure in their programming language so that they can easily do refactoring and build large web applications.

### Optimized for UI

* Asynchronous operations let your program complete work while waiting for another operation to finish. Here are some common asynchronous operations:

    * Fetching data over a network
    * Writing to a database
    * Reading data from a file

* Most computers, even on mobile platforms, have multi-core CPUs. To take advantage of all those cores, developers traditionally use shared-memory threads running concurrently. However, shared-state concurrency is error-prone and can lead to complicated code. Instead of threads, all Dart code runs inside of isolates. Each isolate has its own memory heap, ensuring that no isolate’s state is accessible from any other isolate.

* A programming language optimized for building user interfaces with features for expanding collections, and for customizing the UI for each platform.

### Productive Development

* Flutter has a hot reload feature that helps you quickly and easily experiment, build UIs, add features, and fix bugs. Hot reload works by injecting updated source code files into the running Dart Virtual Machine (VM). After the VM updates classes with the new versions of fields and functions, the Flutter framework automatically rebuilds the widget tree, allowing you to quickly view the effects of your changes.

* Flutter provides static analysis which allows you to find problems before executing a single line of code. It’s a powerful tool used to prevent bugs and ensure that the code conforms to style guidelines.


### Fast on all Platforms

* Dart has an AOT (Ahead of Time) compiler, which compiles to fast, predictable, native code that allows almost all of Flutter to be written in Dart. This not only makes Flutter fast but ensures that virtually everything (including all the widgets) can be customized.
