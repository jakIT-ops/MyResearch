# 1. What is MongoDB

* A NoSQL database 

* NoSQL documentDB

* Stored in collections

### Document

`A way to organize and store data as a set of field-value pairs`

### Collection

`An orgonized store of documents in MongoDB, usually with common fields between documents`

 
## Atlas is

* Your database in the cloud for this course and beyond

* MongoDB is used at the core of Atlas for data storage and retrieval

* Database as a service

### Cluster deployment

#### 1. Clusters 

a group of servers that stores your data

#### 2. Replica set

A few connected MongoDB instances that store the same data

#### 3. Single cluster in Atlas

Automatically configured as a replica set

### Services

* Manage cluster creation

* Run and maintain database deployment

* Use cloud service provider of your choice

* Experiment with new tools and features

### MongoDB Atlas

* Clusters are group of servers that store your data

* Replica Sets are a set of a few connected mongodb instances that store the same data

# 2. Importing Exporting and Querying Data

## How Does MongoDB Store Data?

### JSON

| Pros of JSON | Cons of JSON |
| :----------- | -----------: |
| Friendly     | Text-based |
| Readable     | Space-consuming |
| Familiar     | Limited | 

### BSON

Bridges the gap between binary representation and JSON format Optimizied for:

* Speed 

* Space 

* Flexibility

High performance

General-Purpose focus

| JSON | BSON  |
| :--- | ----: |
| `Encoding UTF-8` String | `Encoding` Binary |
| `Data support` String, boolean, Number, Array | `Data support` String, boolean, Number, Int, long, float, Array, Date, Raw binary |
| `Readability` Human and Machine | `Readability` Machine only |

### Summary 

* MongoDB stores data in BSON. internally and over the network.

* JSON can be nat ively stored and retrieved in MongoDB

* BSON provides additional features like speed and flexibility



# 2. Importing and Exporting Data

## Stored `BSON` vs. Viewed `JSON`

* Export to a local machine : JSON

* Export to a different system : BSON

* Backup cload data locally : BSON

* Import from a local machine

* Import from a different system

### command

| JSON | BSON |
| :---- | ------: |
| mongoimport | mongorestore |
| mongoexport | mongodump |

### Export

BSON
```
mongodump --uri "<Atlas Cluster URI>"
```
JSON
```
mongoexport --uri "<Atlas Cluster URI>"
	    --collection=<collection name>
 	    --out=<filename>.json
```

### Import

BSON

```
mongostore --uri "<Atlas Cluster URI>"
	   --drop dump
```

JSON

```
mongoimport --uri "<Atlas Cluster URI>"
 	    --drop=<filename>.json
```











