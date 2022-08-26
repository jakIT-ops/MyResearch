# 1 Slack

## [Why We Switched from Python to Go](https://softwareengineeringdaily.com/2021/03/03/why-we-switched-from-python-to-go/)

### Reason 1 - Performance

Go is fast! Go is extremely fast. The performance is similar to that of java or C++, For our use case, Go is Typically 40 times faster than Python.

### Reason 2 - Language Performance Matters 

For many applications, the programming language is simply the glue between the app and the database. The performance of the language itself usually doesn't matter much.
We've been optimizing Cassandra, PostgreSQL, Redis, etc, for years, but eventually, you reach the limits of the language you're using,

### Reason 3 - Developer Productivity & Not Getting Too Creative

# 2 [Repustate](https://www.repustate.com/)

* We migrated our entire API stack from Python (First Django then Falcon) to Go reducing the mean response time of an API call from 100ms to 10ms
* We reduced the number of EC2 instacnes required by 85%

# 3 Khan Academy

## From Python to 500,000 lines of Go, how one organization is making a big switch

With half a million lines of Go code now in production. Dangoor has given and update on the Khan Academy's Go migration for its backend services

