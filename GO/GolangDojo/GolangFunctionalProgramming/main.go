package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

func main() {
	// .filter() .map() .reduce()
	// positiveStreamVariable = someStreamVariable.filter(v -> v > 0)
	intSlice := []int{1, 4, -3, 5, -9, 3, -1}
	postiveIntSlice := Filter[int](intSlice, isPositive[int])
	fmt.Println(postiveIntSlice)

	intStream := Stream[int]{insSlice}
	intStream.filter(isPositive[int]).filter(isEven[int])
	fmt.Println(intStream)
}

type Stream[T Number] struct {
	s []T
}

func (s *Stream[T]) filter(f func(T) bool) *Stream[T] {
	s.s = Filter(s.s, f)
	return s
}


type Number interface {
	constraints.Integer | constraints.Float
}

func Filter[T Number](s []T, f func(T) bool) []T {
	var r []T
	for _, v := range s {
		if f(v) > 0 {
			r = append(r, v)
		}
	}
	return r
}

func isPositive(T number)(v T) bool {
	return v > 0
}

func isEven[T constraints.Integer](a T) bool {
	return (a % 2) == 0
}
