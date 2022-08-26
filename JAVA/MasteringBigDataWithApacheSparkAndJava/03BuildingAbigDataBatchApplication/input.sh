mvn install -DskipTests
java -jar /usercode/target/batch-app-0.0.1-SNAPSHOT.jar jobName=salesSummaryJob clientId=client1 sellerId=Joe,Beth date=20201111000000 product=Food