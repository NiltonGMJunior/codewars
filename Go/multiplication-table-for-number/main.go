//   Multiplication table for number - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/go

package main

import (
	"fmt"
	"strings"
)

func MultiTable(number int) string {
	sb := strings.Builder{}
	for i := 1; i <= 10; i++ {
		sb.WriteString(fmt.Sprintf("%d * %d = %d\n", i, number, i*number))
	}
	return strings.TrimRight(sb.String(), "\n")
}

func main() {
	fmt.Println(MultiTable(10))
}
