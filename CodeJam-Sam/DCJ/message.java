import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.Semaphore;
// A program you submit to Distributed Code Jam will be compiled by Google, and
// will run on multiple computers (nodes). This library describes the interface
// needed for the nodes to identify themselves and to communicate.
//
// This is the version of the interface for programs written in Java. Your
// program doesn't need to import it and should always use a class name before
// accessing the static methods, e.g.:
// int n = message.NumberOfNodes();
class QW {
    public LinkedList<LinkedList<Object>> queue = new LinkedList<LinkedList<Object>>();
    public LinkedList<Object> currentWrite = new LinkedList<Object>();
    public LinkedList<Object> currentRead = new LinkedList<Object>();
}

  
public class message {
  public static void initialise(int n)
  {
    numNodes = n;
    semaphores = new Semaphore[n][n];
    messageQueues = new QW [n][n]; 

    for (int i=0; i<n; i++)
    {
      //semaphores[i] = new Semaphore[n];
      for (int j=0; j<n; j++) {
        semaphores[i][j] = new Semaphore(0);
        messageQueues[i][j] = new QW();
      }
    }    
  }

  static Semaphore[][] semaphores;
  static QW[][] messageQueues;

  // The number of nodes on which the solution is running.
  public static int numNodes;
  public static int NumberOfNodes()
  {
    return numNodes;
  }

  // Atomic integer containing the next thread ID to be assigned
     private static final AtomicInteger nextId = new AtomicInteger(0);

     // Thread local variable containing each thread's ID
     private static final ThreadLocal<Integer> threadId =
         new ThreadLocal<Integer>() {
             @Override protected Integer initialValue() {
                 return nextId.getAndIncrement();
         }
     };

  public static int MyNodeId()
  {
    return threadId.get();
  }

  // In all the functions below, if "target" or "source" is not in the valid
  // range, the behaviour is undefined.

  // The library internally has a message buffer for each of the nodes in
  // [0 .. NumberOfNodes()-1]. It accumulates the message in such a buffer through
  // the "Put" methods.

  // Append "value" to the message that is being prepared for the node with id
  // "target". The "Int" in PutInt is interpreted as 32 bits, regardless of
  // whether the actual int type will be 32 or 64 bits.
  public static void PutChar(int target, char value) {
    messageQueues[MyNodeId()][target].currentWrite.add(value);    
  }
  public static void PutInt(int target, int value) {
    messageQueues[MyNodeId()][target].currentWrite.add(value);    
  }
  public static void PutLL(int target, long value) {
    messageQueues[MyNodeId()][target].currentWrite.add(value);    
  }

  // Send the message that was accumulated in the appropriate buffer to the
  // "target" instance, and clear the buffer for this instance.
  //
  // This method is non-blocking - that is, it does not wait for the receiver to
  // call "Receive", it returns immediately after sending the message.
  public static void Send(int target){
    messageQueues[MyNodeId()][target].queue.add(messageQueues[MyNodeId()][target].currentWrite);    
    messageQueues[MyNodeId()][target].currentWrite = new LinkedList<Object>();    
  
    semaphores[MyNodeId()][target].release();
  }

  // The library also has a receiving buffer for each instance. When you call
  // "Receive" and retrieve a message from an instance, the buffer tied to this
  // instance is overwritten. You can then retrieve individual parts of the
  // message through the Get* methods. You must retrieve the contents of the
  // message in the order in which they were appended.
  //
  // This method is blocking - if there is no message to receive, it will wait for
  // the message to arrive.
  //
  // You can call Receive(-1) to retrieve a message from any source, or with
  // source in [0 .. NumberOfNodes()-1] to retrieve a message from a particular
  // source.
  //
  // It returns the number of the instance which sent the message (which is equal
  // to source, unless source is -1).
  public static int Receive(int source)
  {
    try {
      semaphores[source][MyNodeId()].acquire();
          
      messageQueues[source][MyNodeId()].currentRead = messageQueues[source][MyNodeId()].queue.remove();    
  
      return source;
    }
    catch (Exception e) { System.out.println(e.toString()); return -1; }
  }

  // Each of these methods returns and consumes one item from the buffer of the
  // appropriate instance. You must call these methods in the order in which the
  // elements were appended to the message (so, for instance, if the message was
  // created with PutChar, PutChar, PutLL, you must call GetChar, GetChar, GetLL
  // in this order).
  // If you call them in different order, or you call a Get* method after
  // consuming all the contents of the buffer, behaviour is undefined.
  // The "Int" in GetInt is interpreted as 32 bits, regardless of whether the
  // actual int type will be 32 or 64 bits.
  public static char GetChar(int source)
  {
    return (char)messageQueues[source][MyNodeId()].currentRead.remove();
  }
  public static int GetInt(int source)
  {
    return (int)messageQueues[source][MyNodeId()].currentRead.remove();
  }
  public static long GetLL(int source)
  {
    return (long)messageQueues[source][MyNodeId()].currentRead.remove();
  }
}
