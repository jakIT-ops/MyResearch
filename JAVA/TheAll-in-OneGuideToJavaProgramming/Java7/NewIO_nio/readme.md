## Classes and interfaces of NIO API

Java 7 adds several new classes and interfaces for manipulating files and file systems. This new API allows developers to access many low-level OS operations that were not available in the Java API before, such as the WatchService and the ability to create links (in Nix operating systems).


The following list defines some of the most important classes and interfaces of the NIO API:

* Files: This class consists exclusively of static methods that operate on files, directories, or other types of files.

* FileStore: Storage for files.

* FileSystem: Provides an interface to a file system and is the factory for objects to access files and other objects in the file system.

* FileSystems: Factory methods for file systems.

* LinkPermission: The Permission class for link creation operations.

* Paths: This class consists exclusively of static methods that return a Path by converting a path string or URI.

* FileVisitor: An interface for visiting files.

* WatchService: An interface for watching various file-system events such as create, delete, modify.




