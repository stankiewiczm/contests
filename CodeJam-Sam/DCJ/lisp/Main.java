import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws InterruptedException  {
    long myNodeId = message.MyNodeId();
    long numNodes = message.NumberOfNodes();
    long N = lisp_plus_plus.GetLength();

    long interval = ((N + numNodes - 1) / numNodes);
    long start = interval * myNodeId;
    long end = Math.min(start + interval, N);
    
    long net = 0, depth = 0;
    for (long index = start; index < end; index++)
    {
      net += (lisp_plus_plus.GetCharacter(index) == '(') 
        ? 1
        : -1;
      depth = Math.min(depth, net);
    }

    if (message.MyNodeId() > 0) {
      message.PutLL(0, net);
      message.PutLL(0, depth);      
      message.Send(0);
      return;
    }
    
    long netPreFailure = 0;
    int firstFailure = 1000;
    if (depth < 0)
      firstFailure = 0;

    for (int node = 1; node < numNodes; node++)
    {
      message.Receive(node);
      long delta_net = message.GetLL(node);
      long local_depth = message.GetLL(node);

      if ((node < firstFailure) && (net + local_depth < 0))
      {
        firstFailure = node;
        netPreFailure = net;
      }
      net += delta_net;
    }
    
    if (firstFailure == 1000)
    {
        // Nothing illegal
        if (net == 0)
          System.out.println(-1);
        else
          System.out.println(N);
        return;
    }

    // Failure exists in known section
    long intervalStart = interval * firstFailure;
    net = netPreFailure;
    for (long index = intervalStart; index < N; index++)
    {
      net += (lisp_plus_plus.GetCharacter(index) == '(') 
        ? 1
        : -1;

      if (net < 0)
      {
        System.out.println(index);
        return;
      }
    }
  }
}
