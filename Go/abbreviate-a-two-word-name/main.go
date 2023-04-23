//   Abbreviate a Two Word Name - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/go

package main

import (
	"fmt"
	"strings"
)

func AbbrevName(name string) string {
	names := strings.Split(name, " ")
	return strings.ToUpper(string(names[0][0])) + "." + strings.ToUpper(string(names[1][0]))
}

func main() {
	fmt.Println(AbbrevName("Nilton Junior"))
}
