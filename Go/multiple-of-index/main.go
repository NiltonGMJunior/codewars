//   Multiple of index - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/5a34b80155519e1a00000009/go

package main

import (
	"fmt"
)

func multipleOfIndex(ints []int) []int {
	s := make([]int, 0)
	for i, v := range ints {
		if i != 0 && v%i == 0 {
			s = append(s, v)
		}
	}
	return s
}

func main() {
	arr := []int{22, -6, 32, 82, 9, 25}
	fmt.Println(multipleOfIndex(arr))
}
