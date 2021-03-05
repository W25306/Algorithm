package main

import "fmt"

func main() {
	fmt.Println(1)
}

func solution(a []int, b []int) int {
    result := 0
	for i :=0 ; i < len(a); i++{
		result += a[i]*b[i]
	}
	return result
}

func _(a int, b int) string {
	// 프로그래머스 2016년
	month := [12]int{31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	day := 4 + b
	for _, days := range month[0 : a-1] {
		day += days
	}
	switch day % 7 {
	case 0:
		return "SUN"
	case 1:
		return "MON"
	case 2:
		return "TUE"
	case 3:
		return "WED"
	case 4:
		return "THU"
	case 5:
		return "FRI"
	case 6:
		return "SAT"
	default:
		return "UNKNOWN"
	}
}
func _(answers []int) []int {
	// 프로그래머스 모의고
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
