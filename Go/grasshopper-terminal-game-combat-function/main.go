//   Grasshopper - Terminal game combat function - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/go

package main

import (
	"fmt"
)

func combat(health, damage float64) float64 {
	if health-damage < 0 {
		return 0
	}
	return health - damage
}

func main() {
	fmt.Println(combat(100.0, 500.0))
}
