# 1. Aspect Oriented Programming

### What is AOP?

Aspect Oriented Programming (AOP) is the best approach for implementing cross-cutting concerns. Applications are divided into layers like web, business, data, etc. Each layer works independently. There are some concerns that are common across layers. These include security, logging, transaction management, auditing, error handling, performance tracking, etc. These concerns are present in all the layers and are thus called cross-cutting concerns…

<br>
<div align="center">
	<img src="../img/ccc.png">
</div>
<br>

AOP provides an easy way to add concerns like printing logs or tracking performance of methods across layers. For example, we may want to print logs of methods that provide a certain feature. These methods may belong to the web, business, or data layer. Using the OOP approach, we can call the logger from these methods. The problem with such an approach is that in future, if the logs are not needed anymore, or if they are needed for another group of methods, we will have to make changes to the source code. By following the AOP approach, such changes are easy to maintain. Instead of changing the source code, concerns are implemented separately. Thus, any cross-cutting concern can be added and removed without recompiling the complete code by only changing the config files. The logging functionality can be defined separately and applied to any method belonging to any layer easily.

<br>
<div align="center">
	<img src="../img/oopVSaop.png">
	<br>
	<code>Difference between OOP and AOP</code>
</div>
<br>


#### `spring-aop`

spring-aop is a popular implementation of AOP provided by Spring. It is not as powerful as AspectJ. spring-aop can be used to intercept any calls to the beans managed by Spring. Once method calls are intercepted, cross-cutting concerns can be applied before, after, or around the method logic.





