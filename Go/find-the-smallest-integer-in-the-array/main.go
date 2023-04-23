//   Find the smallest integer in the array - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/55a2d7ebe362935a210000b2/go

package main

import (
	"fmt"
	"math"
)

func SmallestIntegerFinder(numbers []int) int {
	smallest := math.MaxInt64
	for _, n := range numbers {
		if n < smallest {
			smallest = n
		}
	}
	return smallest
}

func main() {
	fmt.Println(SmallestIntegerFinder([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
}
