package io.datajek.spring.basics.movierecommendersystem.lesson4;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class RecommenderImplementationSpringBootTest {

	@Autowired
	private RecommenderImplementation recommenderImpl;
	
	@Test
	void testRecommendMovies() {
		assertArrayEquals(new String[] {"Finding Nemo", "Ice Age", "Toy Story"}, recommenderImpl.recommendMovies("Finding Dory"));
	}	
}
