package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	// Create secret number
	secret := getRandomNumber()
	// fmt.Println(secret)

	// Get user input
	guess := getUserInput()
	// fmt.Println(secret, guess)

	// Make comparison (secret vs guess)
	matching := isMatching(secret, guess)
	fmt.Println(matching)
}

func isMatching(secret, guess int) bool {
	if guess > secret {
		fmt.Println("Your guess is too big")
		return false
	} else if guess < secret {
		fmt.Println("Your guess is too small")
		return false
	} else {
		fmt.Println("YOU GOT IT!")
		return true
	}
}

func getUserInput() int {
	fmt.Println("Please input your guess: ")
	var input int
	_, err := fmt.Scan(&input)
	if err != nil {
		fmt.Println("Failed to parse your input")
	} else {
		fmt.Println("Your guessed", input)
	}
	return input
}

func getRandomNumber() int {
	rand.Seed(time.Now().Unix())
	return rand.Int() % 11
}
