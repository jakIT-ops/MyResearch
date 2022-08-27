# PostgreSQL vs MySQL: Differences

My SQL нь хөнгөн учир өндөр хурд нарийн төвөгтэй байдалтай тул  `Вэб сайт болон онлайн гүйлгээнд` илүү сайн PostgreSQL илүү `аналитик` процесуудад сайн

### Speed?

PostgreSQL нь их хэмжээний өгөгдлийн багц, complicated queries, унших бичих үйлдлүүдтэй ажиллахад илүү хурдан байдаг. Нөгөөтэйгүүр, MySQL нь зөвхөн унших командуудад илүү хурдан байдаг.

### Data Indexing?

MySQL index types include:

* Indexes are stored on R-Trees, like indexes found on spatial data types.

* Hash indexes and inverted lists when using FULLTEXT indexes.

* Indexes stored on B-Trees, such as INDEX, FULLTEXT, PRIMARY KEY, and UNIQUE.

PostgreSQL index types on the other hand include:

* Hash indexes and B-Tree indexes.

* Partial indexes that only organize information from part of the table.

* Expression indexes create an index resulting from expression functions instead of column values.


## PostgreSQL vs MySQL: Coding Differences

1. Case Sensitivity

MySQL нь том жижиг жижиг жижиг үсгийг харгалздаггүй бол PostgreSQL нь том жижиг үсгээр ялгадаг. MySQL-д өгөгдлийн санд байгаа мөрүүдийг том үсгээр бичих шаардлагагүй, харин PostgreSQL-ийн хувьд өгөгдлийн санд байгаа мөрүүдийг яг томоор бичих шаардлагатай эсвэл query амжилтгүй болно.

2. Default Character Sets and Strings

MySQL-ийн хувилбаруудын хувьд character sets болон strings UTF-8 болгон хөрвүүлэх хэрэгтэй. PostgreSQL-ийн хувьд character sets болон strings UTF-8 болгон хөрвүүлэх албаггүй.

3. IF and IFNULL vs CASE Statements

MySQL-д IF болон IFNULL statement-үүдийг ашигладаг. PostgreSQL-д IF болон IFNULL statement ажиллахгүй тул та CASE -ийг ашиглах хэрэгтэй.

## PostgreSQL vs MySQL: Advantages

### Advantages of Using PostgreSQL

PostgreSQL supports modern application features like JSON, XML etc. It also supports Materialized Views.

* Хүснэгт хуваах, Transactional DDL, Point in Time Recovery гэх мэт ашигтай функцуудыг санал болгодог.

* Ability to utilize 3rd party Key Stores in a full KPI Infrastructure.

* Open-Source code can be modified by developers as it is licensed under BSD without the need to contribute back enhancements.

* Different users and roles can be assigned Object-Level privileges.

* AES болон 3DES зэрэг өгөгдлийн шифрлэлтийн алгоритмуудыг дэмждэг

### Advantages of Using MySQL

MySQL is a lightweight database that can be installed and used by developers on production application servers with large multi-tier applications.

* Master-Slave Replication болон Scale-Out зэрэг функцуудыг дэмждэг.

* Offload Reporting, Geographic Data Distribution дэмждэг.

* There’s a very low overhead with the MyISAM storage engine when used for read-only applications.

* For frequently used tables support is provided for the Memory Storage Engine.

* For repeatedly used statements there exists a Query Cache.

* MySQL is easy to learn and troubleshoot given a wide number of helpful sources like blogs, white papers, and books on the subject.

* MySQL is a highly flexible and scalable Database Management System.

## PostgreSQL vs MySQL: Disadvantages

### Disadvantages of Using PostgreSQL

* The current external solutions demand a high learning curve.

* Өгөгдлийг гаргах үед шинэ хувилбар руу хуулах эсвэл хуулбарлах шаардлагатай болно.

* Шинэчлэх явцад давхар хадгалах хэрэгцээ гардаг.

* Indexes in PostgreSQL cannot be used to directly return the results of a query.

* PostgreSQL дэх индексүүдийг query ашиглаж үр дүнг шууд буцаах боломжгүй.

* The query execution plans are not cached.

* Bulk loading operations may become bound by the CPU.

* Independent software vendor support is pretty sparse. /  Бие даасан програм хангамж нийлүүлэгчийн дэмжлэг маш ховор байдаг.

### Disadvantages of Using MySQL

* The transactions related to the system catalog are not ACID compliant.

* The server catalog can be corrupted by a single server crash at times.

* Нэг серверийн эвдрэлээс болж серверийн catalog эвдэрч болзошгүй.

* The stored procedures cannot be cached.

* The tables that are used for the procedure or trigger are always pre-locked.

* Maintaining privileges for many users is difficult since there is no support for the roles.

## Conclusion

| Parameters | PostgreSQL	 | MySQL  |
| :--------- | ----------------- | -----: |
| Governance | It is open-source, hence free, and is released under PostgreSQL license. | The source code for MySQL is available but Microsoft Corporation provides paid versions for commercial use. |
| SQL Compliance | PostgreSQL meets almost all core features of the SQL environment. | MySQL is partially SQL compliant and does not meet the full SQL standard |
| Supported Platforms |	It supports Solaris, Windows OS, Linux, OS X, Unix OS, and Hp-UX OS	| It supports Solaris, Windows OS, Linux, OS X, and FreeBSD OS |
| Programming Languages | It supports C/C++, Java, Perl, .Net, R, Python, JavaScript, and others |	It supports C/C++, Erlang, Perl, PHP, GO, Lisp, and others  |
| Security    |	It offers native SLL support for connections for encryptions	| MySQL is highly secure with a lot of many inbuilt security features |
| Replication | It can perform master-slave replication and other types of implementation can be put into practice using third-party extensions	 | It can perform master-master replications well as master-slave replication |
| Performance |	It is widely used in large systems where read and write speed is crucial and requires execution of complex queries | Widely chosen for web-based projects that require a database simply for data transactions |

#### Source:

* https://hevodata.com/learn/postgresql-vs-mysql/
