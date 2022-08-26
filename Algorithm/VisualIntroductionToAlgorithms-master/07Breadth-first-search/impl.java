import java.util.LinkedList;
import java.util.Queue;

class BFSInfo {
  public BFSInfo() {
    this.distance = -1;
    this.predecessor = -1;
  }
  
  public BFSInfo(int distance, int predecessor) {
    this.distance = distance;
    this.predecessor = predecessor;
  }
  
  public int distance;
  public int predecessor;
};

class Solution {
  public static BFSInfo[] doBFS(int[][] graph, int source) {
    System.out.println(graph.length);
    BFSInfo[] bfsInfo = new BFSInfo[graph.length];

    bfsInfo[source] = new BFSInfo();
    bfsInfo[source].distance = 0;

    Queue<Integer> q = new LinkedList<Integer>();
    q.add(source);

    // Traverse the graph

    // As long as the queue is not empty:
    //  Repeatedly dequeue a vertex u from the queue.
    //  
    //  For each neighbor v of u that has not been visited:
    //     Set distance to 1 greater than u's distance
    //     Set predecessor to u
    //     Enqueue v
    //
    //  Hint:
    //  use graph to get the neighbors,
    //  use bfsInfo for distances and predecessors

    return bfsInfo;
  }
}











