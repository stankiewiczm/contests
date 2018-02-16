using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class ProbC2
    {
        internal void Run()
        {
            var node = new Node { Size = 24 };

            int visitors = node.Size;

            //using (var excel = new ProbCExcel("probc.xlsx"))
            {
                //excel.SizeColumns(node.Size);
                int count = 1;
                while (visitors-- > 1)
                {
                    node.Split(count++, null);
                    //excel.Output(node);
                    //break;
                }


            }
        }

        TextWriter sw;
        int i = 1;
        internal void RunFinal()
        {
            using (sw = File.CreateText("C-small2.out"))
            foreach (var pair in File.ReadAllLines("C-small-2-attempt0.in").Skip(1).Select(l => l.Split(' ').Select(i => int.Parse(i)).ToArray()))
            {
                Run(pair[0], pair[1]);
            }
        }

        internal void Run(int N, int K)
        {
            var node = new Node { Size = N };
            while (K-- > 1) node.Split(0, null);
            node.Split(0, delegate(int a, int b)
            {
                sw.WriteLine("Case #{2}: {0} {1}", Math.Max(a, b), Math.Min(a, b), i++);
            });
        }

        public class Node
        {
            public bool IsSplit = false;
            public int Size, MaxLeft, MaxRight, Id;
            public Node Left, Right;

            public int SL, SR;

            internal int Split(int id, Action<int, int> StallTaken)
            {
                if (!IsSplit)
                {
                    Id = id;
                    var half = (int)Math.Floor((Size - 1) / 2.0);
                    if (Size == 2) half = 1;

                    Left = new Node { Size = half };
                    SL = MaxLeft = Left.Size;
                    Right = new Node { Size = Size - half - 1 };
                    SR = MaxRight = Right.Size;
                    IsSplit = true;

                    if (StallTaken != null)
                        StallTaken(Left.Size, Right.Size);

                    return Math.Max(Left.Size, Right.Size);
                }
                else if (MaxRight > MaxLeft)
                    return Math.Max(MaxRight = Right.Split(id, StallTaken), MaxLeft);
                else return Math.Max(MaxLeft = Left.Split(id, StallTaken), MaxRight);
            }

            public override string ToString()
            {
                return String.Join(", ", IsSplit, MaxLeft, Size, MaxRight);
            }
        }
    }
}
