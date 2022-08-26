package io.datajek.springaop.movierecommenderaop.business;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import io.datajek.springaop.movierecommenderaop.aspect.MeasureTime;
import io.datajek.springaop.movierecommenderaop.data.Movie;

@Service
public class FilteringTechnique1 {

	@Autowired
	private Movie movie;
	
	@MeasureTime
	public String contentBasedFiltering() {
		String movieDetails = movie.getMovieDetails();
		return movieDetails;
	}
}
