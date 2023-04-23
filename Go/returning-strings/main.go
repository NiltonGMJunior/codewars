//   Returning Strings - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/55a70521798b14d4750000a4/train/go

package main

import (
	"fmt"
)

func Greet(name string) string {
	return fmt.Sprintf("Hello, %s how are you doing today?", name)
}

func main() {
	fmt.Println(Greet("Nilton Junior"))
}
