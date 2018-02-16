import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws InterruptedException  {
    long myNodeId = message.MyNodeId();
    long numNodes = message.NumberOfNodes();
    long N = oops.GetN();

    long interval = ((N + numNodes - 1) / numNodes);
    long start = interval * myNodeId;
    long end = Math.min(start + interval, N);
    
    long min = Long.MAX_VALUE, max = 0;
    for (long index = start; index < end; index++)
    {
      long number = oops.GetNumber(index);
      min = Math.min(min, number);
      max = Math.max(max, number);
    }

    if (message.MyNodeId() > 0) {
      message.PutLL(0, min);
      message.PutLL(0, max);      
      message.Send(0);
      return;
    }
    
    for (int node = 1; node < numNodes; node++)
    {
      message.Receive(node);
      min = Math.min(min, message.GetLL(node));
      max = Math.max(max, message.GetLL(node));
    }
    
    System.out.println(max - min);
  }
}
