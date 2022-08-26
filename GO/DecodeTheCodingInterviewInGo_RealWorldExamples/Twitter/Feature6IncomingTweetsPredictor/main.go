package main
import (
  "fmt"
)

type TweetsPredictor struct {
     size int
     queue *Deque
     queueLen int
     windowSum int
}

func NewTweetsPredictor (size int) *TweetsPredictor {
     tp := new(TweetsPredictor)
     tp.size = size
     tp.queue = new(Deque)
     tp.queueLen = 0
     tp.windowSum = 0
     return tp
}


func (this *TweetsPredictor) PredictTweets(val int) float64{
     popVal := 0
     if this.queueLen == this.size {
          popVal =  this.queue.PopFront()
     } else {
          this.queueLen = this.queueLen + 1
          popVal = 0
     }
     this.queue.PushBack(val)
     this.windowSum = this.windowSum + val - popVal
     return float64(this.windowSum) / float64(this.queueLen)
}
func main() {
     // Driver Code
     values := []int{1,10,3,5}
     countTweets := NewTweetsPredictor(3)

     for _, i := range values{
          average := countTweets.PredictTweets(i)
          fmt.Println(average)
     }
}
