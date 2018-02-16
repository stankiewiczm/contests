using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeJam2016
{
    class Round11b : IComparer<int[]>
    {
        static void Main(string[] args)
        {
            new Round11b().Run("B-small-attempt2.in");
        }

        TextWriter sw, dw;
        int caseNo = 1;
        internal void Run(string p)
        {
            using (var sr = File.OpenText(p))
            using (sw = File.CreateText("B1-small.out"))
            using (dw = File.CreateText("B1-debug.out"))
            {
                int count = int.Parse(sr.ReadLine());

                for (int i = 0; i < count; i++)
                {
                    int n = int.Parse(sr.ReadLine());

                    var lists = new List<string>();
                    for (int j = 0; j < 2 * n - 1; j++)
                        lists.Add(sr.ReadLine());

                    sw.WriteLine("Case #{0}: {1}", caseNo++, Check(n, lists));
                    Console.WriteLine();
                }
            }
        }

        private object Check(int n, List<string> lists)
        {
            var ilists = lists.Select(l => l.Split(' ').Select(x => int.Parse(x)).ToArray()).ToList();

            return Sort(n, new List<int[]>(ilists));
        }

        private object Sort(int n, List<int[]> ilists)
        {
            var missing = 0;
            bool missingOrientation = false;
            var matrix = new int[n, n];
            var pairLists = new List<List<int[]>>();

            try
            {
                for (int i = 0; i < n; i++)
                {
                    var min = ilists.Min(l => l[i]);

                    var pairList = new List<int[]>();

                    for (int j = 0; j < ilists.Count; j++)
                    {
                        if (ilists[j][i] == min)
                            pairList.Add(ilists[j]);
                    }

                    foreach (var k in pairList)
                        ilists.Remove(k);

                    pairLists.Add(pairList);

                    if (pairList.Count > 2) throw new Exception();
                    else if (pairList.Count == 1)
                        missing = i;
                }

                Check(pairLists, 0, new Stack<int[]>(), n);
            }
            finally { Output(matrix, n); }

            return (GetMatrix(matrix, n, missing, missingOrientation));
        }

        private void Check(List<List<int[]>> pairLists, int p, Stack<int[]> stack, int n)
        {
            foreach (var list in pairLists[p])
            {
                stack.Push(list);
                if (p + 1 < n) Check(pairLists, p + 1, stack, n);
                else TestStack(pairLists, stack, n);
                stack.Pop();
            }
        }

        private void TestStack(List<List<int[]>> pairLists, Stack<int[]> stack, int n)
        {
            var matrix = new int[n,n];
            int i=0;
            foreach (var row in stack.Reverse())
                Set(matrix, row, true, n, i++);


        }

        private void Output(int[,] matrix, int n)
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                    dw.Write(matrix[i, j] + " ");
                dw.WriteLine();
            }
            dw.WriteLine();
        }

        private object GetMatrix(int[,] matrix, int n, int j, bool row)
        {
            var result = new List<int>();
            for (int i = 0; i < n; i++)
                if (row)
                    result.Add(matrix[j, i]);
                else result.Add(matrix[i, j]);

            return String.Join(" ", result);
        }

        private void Set(int[,] matrix, int[] list, bool row, int n, int index)
        {
            for (int i = 0; i < n; i++)
                if (row)
                    matrix[index, i] = list[i];
                else matrix[i, index] = list[i];
        }

        private bool Check(int[,] matrix, int[] list, bool row, int n, int index)
        {
            for (int i = 0; i < n; i++)
                if (row) { if (matrix[index, i] != list[i] && matrix[index, i] > 0) return false; }
                else { if (matrix[i, index] != list[i] && matrix[i, index] > 0) return false; }

            return true;
        }

        public object matrix { get; set; }
        public int Compare(int[] x, int[] y)
        {
            for (int i = 0; i < x.Length; i++)
                if (x[i] != y[i])
                    return x[i].CompareTo(y[i]);

            return 0;
        }

        public bool n { get; set; }
    }
}
