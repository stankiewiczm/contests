public class Main {
    static int MASTER_NODE = 0;
    static int ManualLimit = 1000;
    
    public static long StackStart(long nodeId)
    {
        long nodes = message.NumberOfNodes();
        long N = pancakes.GetStackSize();
        
        return (N / (nodes-1))*(nodeId-1);
    }

    public static void main(String[] args) {
        long N = pancakes.GetStackSize();
        
        long nodes = message.NumberOfNodes();
        long my_id = message.MyNodeId();

        if (my_id != MASTER_NODE)
        {
            if (N < ManualLimit)
                return;
            
            long start = StackStart(my_id) ;
            long end = StackStart(my_id + 1);
            
            if (my_id != 1)
                start -= 1;

            if (my_id == nodes-1)
                end = N;
            
            long last = 0;
            long revolutions = 0;
            
            for (long i = start; i < end; i++)
            {
                long next = pancakes.GetStackItem(i);
                if (next < last)
                    revolutions += 1;
                last = next;
            }

            message.PutLL(MASTER_NODE, revolutions);
            message.Send(MASTER_NODE);
            return;
        }
        
        else    // MASTER NODE
        {
            if (N < ManualLimit)
            {
                long ans = 1;
                long last = 0;
                for (long i = 0; i < N; i++)
                {
                    long next = pancakes.GetStackItem(i);
                    if (next < last)
                        ans += 1;
                    last = next;
                }
                System.out.println(ans);
                return;
            }
            
            long internalRevolutions = 1;
            for (int node = 1; node < nodes; node++) 
            {
                message.Receive(node);
                internalRevolutions += message.GetLL(node);
            }
            
            System.out.println(internalRevolutions);
            return;
        }
    }
}
