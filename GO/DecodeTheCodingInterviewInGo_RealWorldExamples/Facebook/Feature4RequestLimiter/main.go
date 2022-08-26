package main
import "fmt"

type RequestLimiter struct{
    requests map[string]int 
}

// Returns true if the request should be printed in the given timestamp, 
//otherwise returns false.
func (this *RequestLimiter) RequestApprover(timestamp int, request string) bool{

    if _, ok := this.requests[request]; !ok {
        this.requests[request] = timestamp
        fmt.Println("Request Accepted")
        return true
    }

    oldTimestamp := this.requests[request];

    if (timestamp - oldTimestamp >= 5) {
        this.requests[request] = timestamp
        fmt.Println("Request Accepted")
        return true
    } else {
        fmt.Println("Request Rejected")
        return false
    }

}

func main() {
    var obj RequestLimiter
    obj.requests = make(map[string]int)
    obj.RequestApprover(1, "send_message")
    obj.RequestApprover(2, "block")
    obj.RequestApprover(3, "send_message")
    obj.RequestApprover(8, "block")
    obj.RequestApprover(10, "send_message")
    obj.RequestApprover(11, "send_message")
}
