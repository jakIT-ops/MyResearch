package main
import (
  "fmt"
  "strconv"
  "strings"
)

func serviceTime(n int, logs []string) []int{
    var stack Stack;

    funcTimes := make([]int, n)
    delim := ":"
    funcStr := strings.Split(logs[0], delim)
    temp, _ := strconv.Atoi(funcStr[0])
    stack = stack.Push(temp)
    time, _ := strconv.Atoi(funcStr[2])
    for i := 0; i < len(logs); i++ {
        funcStr = strings.Split(logs[i], delim)
        if strings.Contains(funcStr[1], "start") {
            if !stack.Empty(){
                temp, _ = strconv.Atoi(funcStr[2])
                funcTimes[stack.Top()] += (temp - time)
            }
            temp, _ = strconv.Atoi(funcStr[0])
            stack = stack.Push(temp)
            time, _ = strconv.Atoi(funcStr[2])
        } else{
            temp, _ = strconv.Atoi(funcStr[2])
            funcTimes[stack.Top()] += (temp - time + 1)
            stack, _ = stack.Pop()
            time = temp + 1
        }
            
    } 
    
    return funcTimes
}

func main() {
    logs := []string{"0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"}
    print(serviceTime(2, logs))
}
