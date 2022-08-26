package io.datajek.spring.basics.movierecommendersystem.lesson4;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;

class RecommenderImplementationUnitTest {

	@Test
	void testRecommendMovies_withCollaborativeFilter() {
		RecommenderImplementation recommenderImpl = new RecommenderImplementation(new CollaborativeFilter());
		assertArrayEquals(new String[] {"Finding Nemo", "Ice Age", "Toy Story"}, recommenderImpl.recommendMovies("Finding Dory"));
	}

	@Test
	void testRecommendMovies_withContentBasedFilter() {
		RecommenderImplementation recommenderImpl = new RecommenderImplementation(new ContentBasedFilter());
		assertArrayEquals(new String[] {"Happy Feet", "Ice Age", "Shark Tale"}, recommenderImpl.recommendMovies("Finding Dory"));
	}
}

