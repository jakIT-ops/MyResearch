from Queue import Queue

class BFSInfo():
  def __init__(self, srcDistance = None, predecessor = None):
    self.srcDistance = srcDistance
    self.predecessor = predecessor
    
def doBFS(graph, source):
  bfsInfo = []
  for i in xrange(len(graph)):
    bfsInfo.append(BFSInfo())
    
  bfsInfo[source].srcDistance = 0
  
  q = Queue()
  q.put(source)
  
  # Traverse the graph

  # As long as the queue is not empty:
  #  Repeatedly dequeue a vertex u from the queue.
  #  
  #  For each neighbor v of u that has not been visited:
  #     Set distance to 1 greater than u's distance
  #     Set predecessor to u
  #     Enqueue v
  #
  #  Hint:
  #  use graph to get the neighbors,
  #  use bfsInfo for distances and predecessors 
    
  return bfsInfo























