import java.io.*;
import java.util.*;

public class Wrapper implements Runnable {
    public int nodeId;

    public void run() 
    {
        try {
            Main.main(new String[0]);
        }
        catch (Exception ex) {}
    }
}