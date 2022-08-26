package main
import (
  "fmt"
  "math"
)

func FindGlobalProfile(tweets [][]int) [][]int {
    // Finding the lenght of the tweets list
    TweetsLen := len(tweets)
    // If the tweets list is empty, return an empty list.
    if TweetsLen == 0{
        return [][]int{}
    }
    // If there is only tweet in the list, return the required coordinates 
    if TweetsLen == 1 {
        StartXCoordinate := tweets[0][0] 
        EndXCoordinate := tweets[0][1]
        PeakMentions := tweets[0][2]
        //output := [][]int, 0
        return [][]int{{StartXCoordinate, PeakMentions}, {EndXCoordinate, 0}}
    }
    //If there is more than one tweet, keep dividing the tweets recurssively into two parts.
    StartTweets := FindGlobalProfile(tweets[: int(TweetsLen / 2)])
    EndTweets := FindGlobalProfile(tweets[int(TweetsLen / 2) :])

    // Merge the divided tweets together.
    return MergeGlobalProfiles(StartTweets, EndTweets)
}

func UpdateGlobalProfile(xCoordinate int, yCoordinate int, globalProfile [][]int) [][]int{
    // Updating and returning our global profile 

    // add a new point if our global profile has not changed vertically.
    if len(globalProfile) == 0 || 
    globalProfile[len(globalProfile) - 1][0] != xCoordinate {
        globalProfile = append(globalProfile, []int{xCoordinate, yCoordinate})
        // update the last point if our global profile has changed vertically
    } else{
        globalProfile[len(globalProfile) - 1][1] = yCoordinate
    }
    return globalProfile
}
func AppendGlobalProfile(currIndex int, tweetsList [][]int, tweetsListLen int, 
yCoordinate int, cMentions int,globalProfile [][]int) [][]int {
    // From our current index, append the rest of the elements to our final global profile.
    for currIndex < tweetsListLen{
        xCoordinate, yCoordinate := tweetsList[currIndex][0], tweetsList[currIndex][1]
        currIndex += 1
        if cMentions != yCoordinate {
            globalProfile = UpdateGlobalProfile(xCoordinate, yCoordinate,globalProfile)
            cMentions = yCoordinate
        }
    }
    return globalProfile
}

func MergeGlobalProfiles(startTweets [][]int, endTweets [][]int) [][]int {
    // Storing the lengths of both global profiles i.e., starting tweets and ending tweets.
    lenStart, lenEnd := len(startTweets), len(endTweets)

    // initializing the variables.
    iStart, iEnd := 0, 0
    cMentions, startY, endY, xCoordinate := 0, 0, 0, 0
    globalProfile := make([][]int, 0)

    // while we're in the region where both globalProfiles are present
    for iStart < lenStart && iEnd < lenEnd {
        startPoint, endPoint := startTweets[iStart], endTweets[iEnd]

        // pick up the smallest x
        if startPoint[0] < endPoint[0]{
            xCoordinate, startY = startPoint[0], startPoint[1]
            iStart += 1
        } else {
            xCoordinate, endY = endPoint[0], endPoint[1]
            iEnd += 1
        }
        // max height (i.e. y) between both globalProfiles
        maxPeakMentions := int(math.Max(float64(startY), float64(endY)))

        // if there is a globalProfile change
        if cMentions != maxPeakMentions{
            globalProfile = UpdateGlobalProfile(xCoordinate, maxPeakMentions, globalProfile)
            cMentions = maxPeakMentions
        }
    }
    // there is only startTweets globalProfile
    globalProfile = AppendGlobalProfile(iStart, startTweets, lenStart, startY, cMentions, globalProfile)

    // there is only endTweets globalProfile
    globalProfile = AppendGlobalProfile(iEnd, endTweets, lenEnd, endY, cMentions, globalProfile)

    return globalProfile
}

func main() {
    tweets := [][]int{{2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8}}
    fmt.Print(FindGlobalProfile(tweets))
}
