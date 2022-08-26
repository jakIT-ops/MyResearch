class Solution {
  public static List<List<String>> findDuplicateTweets(String[] tweetsInfo) {
    // create a hashmap to store the duplicate people names for a hashtag
    HashMap <String, List<String>> map = new HashMap < > ();

    // iterate over each tweet information
    for (int j = 0; j < tweetsInfo.length; j++) {
      String tweet = tweetsInfo[j];

      // obtain the days, people names, and hashtags 
      // separately by splitting based on the space
      String[] values = tweet.split(" ");

      for (int i = 1; i < values.length; i++) {
        // split the person name and the hashtag appropriately to get the hashtag
        String[] name_cont = values[i].split("\\(");
        name_cont[1] = name_cont[1].replace(")", "");

        // check if the hashtag already exists in the map
        // if it exists, then return its value and add the hashmap path to it,
        // otherwise create a new list and add the hashmap path to it
        List<String> list = map.getOrDefault(name_cont[1], new ArrayList < String > ());
        list.add(values[0] + "/" + name_cont[0]);
        map.put(name_cont[1], list);
      }
    }
    
    // check if each hashtag has a list that consists of at least 
    // two hashtag paths, and add such lists to the output and return it
    List <List<String>> output = new ArrayList < > ();
    for (String key: map.keySet()) {
      if (map.get(key).size() > 1) {
        output.add(map.get(key));
      }
    }
    return output;
  }

  public static void main(String[] args) {
    // Driver code
    String[] tweetsInfo = {"Monday Joe(t20) Jack(chevrolet) Charlie(ev)", "Tuesday Alice(cake) Bob(chevrolet)", "Wednesday Joe(boeing) Jack(ev) Alice(t20)"};

    List < List < String >> output = findDuplicateTweets(tweetsInfo);
    System.out.println(output);
  }
}

