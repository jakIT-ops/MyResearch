package main

import (
	"math/rand"
	"strconv"
	"testing"
)

func BenchmarkAddTypeSwitch(b *testing.B) {
	for i := 0; i < b.N; i++ {
		addTypeSwitch(rand.Int(), rand.Int())
		addTypeSwitch(rand.Float64(), rand.Float64())
		addTypeSwitch(strconv.Itoa(rand.Int()), strconv.Itao(rand.Int()))
	}
}

func BenchmarkAddReflection(b *testing.B) {
	for i := 0; i < b.N; i++ {
		addReflection(rand.Int(), rand.Int())
		addReflection(rand.Float64(), rand.Float64())
		addReflection(strconv.Itoa(rand.Int()), strconv.Itao(rand.Int()))
	}
}

func BenchmarkAddGenericsWithTypeSet(b *testing.B) {
	for i := 0; i < b.N; i++ {
		addGenericsWithTypeSet(rand.Int(), rand.Int())
		addGenericsWithTypeSet(rand.Float64(), rand.Float64())
		addGenericsWithTypeSet(strconv.Itoa(rand.Int()), strconv.Itao(rand.Int()))
	}
}

func addInt(a, b int) int {
	return a + b
}

func addFloat64(a, b float64) float64 {
	return a + b
}

func addString(a, b string) string {
	return a + b
}

func addGenerics[T int | float64 | string](a, b T) T {
	return a + b
}

type typeSet interface {
	int | float64 | string
}

func addGenericsWithTypeSet[T typeSet](a, b T) T {
	return a + b
}
