import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws InterruptedException  {
    long myNodeId = message.MyNodeId();
    long numNodes = message.NumberOfNodes();
    long N = majority.GetN();

    long interval = ((N + numNodes - 1) / (numNodes - 1));
    long start = interval * (myNodeId - 1);
    long end = Math.min(start + interval, N);
    
    long min = Long.MAX_VALUE, max = 0;
	String voteList = "";
    for (long index = start; index < end; index++)
	{
		long vote = majority.GetVote(index);
		voteList = voteList + Objects.toString(vote) + " ";
 //     long number = majority.GetNumber(index);
 //     min = Math.min(min, number);
 //     max = Math.max(max, number);
    }

	System.out.println(myNodeId + " " + start + " " + end + " -> " + voteList);

    if (message.MyNodeId() > 0) {
//      message.PutLL(0, min);
 //     message.PutLL(0, max);      
      message.Send(0);
      return;
    }
    
    for (int node = 1; node < numNodes; node++)
    {
      message.Receive(node);
//      min = Math.min(min, message.GetLL(node));
//      max = Math.max(max, message.GetLL(node));
    }
    
    System.out.println(max - min);
  }
}
	