//   Enumerable Magic #20 - Cascading Subsets - CodeWars
//   Nilton Gomes Martins Junior
//   23/04/2023
//   https://www.codewars.com/kata/545af3d185166a3dec001190/go

package main

import (
	"fmt"
)

func EachCons(arr []int, n int) [][]int {
	s := make([][]int, 0)
	for i := 0; i < len(arr)-n+1; i++ {
		s = append(s, arr[i:i+n])
	}
	return s
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	fmt.Println(EachCons(arr, 2))
}
