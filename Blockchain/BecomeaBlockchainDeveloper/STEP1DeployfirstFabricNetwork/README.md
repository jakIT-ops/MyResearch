# Network Concepts

Hyperledger Fabric forms a distributed network and in order to run on a single machine, we use docker containers to run individual distributed components. Each component runs in a separate container instance and connects to other containers to form a network.

## Understanding Docker

A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. Understanding docker and docker-compose is crucial to understanding the dev environment we will use in this course.

For development purposes we will run a small network on our machine in docker containers. This network configuration is called basic-network and is provided in official hyperledger fabric-samples repo (link: https://github.com/hyperledger/fabric-samples).

### Components of Network:

Lets get to know the components of a basic network.

#### 1. PEER:

- <b>peer container</b>: Runs the peer node
- <b>couch db container</b>: Stores the state database of peer node

#### 2. ORDERER:

- <b>orderer container:</b> Solo orderer node to keep dev environment simple. In a real-world network the ordering service is distributed with multiple nodes communicating with each other.

#### 3. CERTIFICATE AUTHORITY:

- <b>fabric-ca container</b>: root certificate authority for issuing membership certificates to all nodes and users. Since we will use single CA, our network is comprised of a single org called “example dot com”.

#### 4. TOOLING:

- <b>fabric-cli container</b>: This container has some cli tools that help us interact with network nodes to deploy chaincode etc.
