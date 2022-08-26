package io.datajek.springaop.movierecommenderaop.aspect;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Configuration;

@Aspect
@Configuration
public class ExecutionTimeAspect {

	private Logger logger = LoggerFactory.getLogger(this.getClass());

	@Around("io.datajek.springaop.movierecommenderaop.aspect.JoinPointConfig.measureTimeAnnotation()")
	public Object calculateExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
		//note start time
		long startTime = System.currentTimeMillis();
		//allow method call to execute
		Object returnValue = joinPoint.proceed();
		//time taken = end time - start time
		long timeTaken = System.currentTimeMillis() - startTime;
		
		logger.info("\n\n>>Time taken by {} \nto complete execution is: {}\n", joinPoint, timeTaken);
		return returnValue;
	}
}
