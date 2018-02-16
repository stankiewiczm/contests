import java.io.*;
import java.util.*;

// This is a sample solution to the "Sum all integers" problem. Each node sums
// the elements that belong to it (that is, the ones with position equal to
// MyNodeId() modulo NumberOfNodes()).
//
// To showcase the communication a bit better, instead of sending all the
// results to a "master" node, each node sends its result to the next one,
// accumulating the result from the previous node. The last node prints the
// final result.
//
// Note: In Java solutions, you must name the main class "Main". Otherwise,
// you will get a compilation error.
public class WrapperMain {
  public static void main(String[] args) {
    message.initialise(Integer.parseInt(args[0]));
    for (int i=0; i<message.numNodes; i++)
    {
      Wrapper w = new Wrapper();
      w.nodeId = i;

      new Thread(w).start();
    }
  }
}