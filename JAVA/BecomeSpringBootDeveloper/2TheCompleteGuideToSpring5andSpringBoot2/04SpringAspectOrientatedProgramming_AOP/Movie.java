package io.datajek.springaop.movierecommenderaop.data;
import org.springframework.stereotype.Repository;

import io.datajek.springaop.movierecommenderaop.aspect.MeasureTime;

@Repository
public class Movie {

	@MeasureTime
	public String getMovieDetails() {
		return "movie details";		
	}
}
