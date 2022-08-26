# 1.  Creating a JDBC Starter Project

Spring JDBC makes talking to databases easy by eliminating the need for establishing a connection, handling expectations, and closing connections. Spring provides a template class called JdbcTemplate to interact with databases which offers a wide array of methods to perform storage and retrieval of data. The JdbcTemplate class hides all the boilerplate code for connection management and error handling whereby the developer can focus on the SQL query.

### Spring Boot JDBC

Spring Boot simplifies development and makes JDBC programming easy. JDBC with Spring Boot offers the following advantages over JDBC with Spring:

* When using Spring Boot, only one dependency (spring-boot-starter-jdbc) is needed in the pom.xml file as compared to multiple dependencies in Spring (spring-context, spring-jdbc, etc.).

* Spring Boot automatically initializes the datasource bean whereas it needs to be created using XML or Java configuration in Spring.

* Spring Boot also autoconfigures the JdbcTemplate and other template beans that need to be explicitly registered in Spring.

* Lastly, Spring Boot automatically creates the database schema specified in the schema.sql file. The schema needs to be explicitly configured if Spring is used.

# 2. Setting up the H2 database

### Configuring database connection

1. The in-memory database H2 has automatically been configured in our application. The URL can be found from the console log. This value is randomly generated each time the server is restarted. To make the database URL a constant, we need to configure this in application.properties as follows:

```
spring.datasource.url=jdbc:h2:mem:testdb
```

2. The next task is connecting to the H2 database. One of the reasons for using Spring Boot is that its autoconfiguration feature looks at the H2 dependency and automatically configures a connection to the H2 database. The H2 console can be enabled in the application.properties file as follows:
```
spring.h2.console.enabled=true
```
3. The database can be viewed in the web browser by typing localhost:8080/h2-console or http://127.0.0.1:8080/h2-console. In the login page that shows up, make sure that the JDBC URL is the same as the one that we provided in the applications.properties file (jdbc:h2:mem:testdb). If not, change it to jdbc:h2:mem:testdb and click connect to go to the database console.

### Creating a table 

```java
  CREATE TABLE Player (
     ID INTEGER NOT NULL,
     Name VARCHAR(255) NOT NULL,
     Nationality VARCHAR(255) NOT NULL,
     Birth_date TIMESTAMP,
     Titles INTEGER,
     PRIMARY KEY (ID)
  );

```
### Inserting data

```
INSERT INTO Player (ID, Name, 
Nationality, Birth_date, Titles)
VALUES(1, 'Djokovic', 'Serbia', '1987-05-22', 81);

INSERT INTO Player (ID, Name, 
Nationality, Birth_date, Titles)
VALUES(2, 'Monfils', 'France', '1986-09-01', 10);

INSERT INTO Player (ID, Name, 
Nationality, Birth_date, Titles)
VALUES(3, 'Isner', 'USA', '1985-04-26', 15);
```

# Query

JDBC involves a lot of boilerplate code that is required just to get the application working. It is a tedious task to write a simple query using JDBC. There are a number of steps that are required to interact with the database.

* The first step is establishing a connection

* The second step is creating a prepared statement or query

* The third step is to execute the query

* The fourth step is looping through the result set to get the objects

* The fifth and final step is to close the connection

<br>
<div align="center">
	<img src="../img/jdbctemplate.png">
	<br>
	<code>Spring JdbcTemplate and RowMapper simplify database operations</code>
</div>
<br>

### Defining Player bean

```java
public class Player{
    private int id;
    private String name;
    private String nationality;
    private Date birthDate;
    private int titles;
    //. . .
}
```

### Creating DAO class

```java
@Repository
public class PlayerDao {

}
```

## Select * query 

```java
@Autowired
JdbcTemplate jdbcTemplate;
```

```java
public List<Player> getAllPlayers() {
    String sql = "SELECT * FROM PLAYER";
    return jdbcTemplate.query(sql, new BeanPropertyRowMapper<Player> (Player.class));
}
```


### Executing the query

```java
@SpringBootApplication
public class TennisPlayerApplication implements CommandLineRunner {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    PlayerDao dao;
 
    public static void main(String[] args) {
        SpringApplication.run(TennisPlayerApplication.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        logger.info("All Players Data: {}", dao.getAllPlayers());
    }
}
```

## Insert query

```java
public int insertPlayer(Player player)
{
    String sql = "INSERT INTO PLAYER (ID, Name, Nationality,Birth_date, Titles) " + 
                                                                  "VALUES (?, ?, ?, ?, ?)";
    return jdbcTemplate.update( sql, new Object[] 
                               { player.getId(), player.getName(), player.getNationality(), 
                                 new Timestamp(player.getBirthDate().getTime()), 
                                 player.getTitles()  
                               });
}
```

## Update query

```java
public int updatePlayer(Player player){
    String sql = "UPDATE PLAYER " +
                 "SET Name = ?, Nationality = ?, Birth_date = ? , Titles = ? " +
                 "WHERE ID = ?";

    return jdbcTemplate.update( sql, new Object[] { 
                                   player.getName(), 
                                   player.getNationality(), 
                                   new Timestamp(player.getBirthDate().getTime()), 
                                   player.getTitles(), 
                                   player.getId() }
                              );
}
```

## Delete query

```java
public int deletePlayerById(int id) {
    String sql="DELETE FROM PLAYER WHERE ID = ?";
    return jdbcTemplate.update(sql, new Object[] {id});
}
```


## DDL queries

```java
public void createTournamentTable() {
    String sql = "CREATE TABLE TOURNAMENT (ID INTEGER, NAME VARCHAR(50), 
                                           LOCATION VARCHAR(50), PRIMARY KEY (ID))";
    jdbcTemplate.execute(sql);
    System.out.println("Table created");
}
```

# Connectiong to Other Databases

## Replacing the H2 dependency

```xml
<dependency>
   <groupId>mysql</groupId>
   <artifactId>mysql-connector-java</artifactId>
</dependency>
```

### Configuring property values

```
spring.jpa.hibernate.ddl-auto=none 
spring.datasource.url = jdbc:mysql://localhost:3306/movie_example
spring.datasource.username = demo
spring.datasource.password = demo
```





