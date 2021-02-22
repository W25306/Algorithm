package main

import "fmt"

func main() {
	var test = []int{1, 3, 2, 4, 2}
	fmt.Println(solution(test))
}

func solution(answers []int) []int {
	var first = [5]int{1, 2, 3, 4, 5}
	var second = [8]int{2, 1, 2, 3, 2, 4, 2, 5}
	var third = [10]int{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
	first_score, second_score, third_score := 0, 0, 0
	for i := 0; i < len(answers); i++ {
		if answers[i] == first[i%5] {
			first_score++
		}
		if answers[i] == second[i%8] {
			second_score++
		}
		if answers[i] == third[i%10] {
			third_score++
		}
	}
	Max := func(a, b int) int {
		if a > b {
			return a
		} else {
			return b
		}
	}
	max := Max(Max(first_score, second_score), third_score)
	result := []int{}
	if first_score == max {
		result = append(result, 1)
	}
	if second_score == max {
		result = append(result, 2)
	}
	if third_score == max {
		result = append(result, 3)
	}
	return result
}
