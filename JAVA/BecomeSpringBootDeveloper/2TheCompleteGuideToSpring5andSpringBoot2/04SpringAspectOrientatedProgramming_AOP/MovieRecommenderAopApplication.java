package io.datajek.springaop.movierecommenderaop;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import io.datajek.springaop.movierecommenderaop.business.FilteringTechnique1;
import io.datajek.springaop.movierecommenderaop.business.FilteringTechnique2;

@SpringBootApplication
 public class MovieRecommenderAopApplication implements CommandLineRunner{

	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	@Autowired
	private FilteringTechnique1 filter1;
	
	@Autowired
	private FilteringTechnique2 filter2;
		
	public static void main(String[] args) {
		SpringApplication.run(MovieRecommenderAopApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		logger.info("{}",filter1.contentBasedFiltering());
		logger.info("{}",filter2.collaborativeFiltering());
		
	}
}
