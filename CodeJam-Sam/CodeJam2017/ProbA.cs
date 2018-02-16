using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class ProbA
    {
        Random r = new Random();
        TextWriter tw = Console.Out;
        internal void Run()
        {
            int K;
            int S;
            bool[] P;

            int count = 1; tw = TextWriter.Null;

            using (var sw = File.CreateText("A-large.out"))
                foreach (var parts in File.ReadAllLines("A-large.in").Skip(1).Select(l => l.Split(' ')))
                {
                    var p = parts[0].Select(c => c == '+').ToArray();
                    var result = Solve(p.Length, int.Parse(parts[1]), p);
                    sw.WriteLine("Case #{0}: {1}", count++, result == int.MaxValue ? "IMPOSSIBLE" : result.ToString());
                }
            //int count = 1;
            //using (tw = File.CreateText("PA.txt"))
            //using (var sw = File.CreateText("A-small.out"))
            //for (K = 2; K <= S; K++)
            //{
            //    var result = Solve(S, K, P);
            //    sw.WriteLine("Case #{0}: {1}", count++, result);
            //}
        }

        public ProbA Generate()
        {
            int K;
            int S, count = 0;
            bool[] P;

            using (var test = File.CreateText("A-large.in"))
            {
                test.WriteLine();
                while (true)
                {
                    S = r.Next(2, 1001);
                    P = new bool[S];

                    Randomise(P);
                    tw = Console.Out;
                    Write(P);
                    tw = TextWriter.Null;

                    var found = false;
                    for (K = 9; K <= S; K++)
                        if (Solve(S, K, P) < int.MaxValue)
                        {
                            tw = test;
                            Write(P, K);
                            tw = TextWriter.Null;
                            found = true;
                        }

                    if (found && count++ > 200) break;
                }
            }

            return this;
        }

        private int Solve(int S, int K, bool[] P)
        {
            tw.WriteLine(String.Join(",", S, K, Count(P)));
            Write(P);

            var l = SolveLeft(S, K, P.ToList().ToArray());
            var r = SolveRight(S, K, P.ToList().ToArray());

            if (l != r) Console.WriteLine("{0} {1}", l, r);

            return Math.Max(l, r);
        }

        private bool Check(bool[] P)
        {
            foreach (var p in P) if (!p) return false;

            return true;
        }

        private int Count(bool[] P)
        {
            var count = 0;
            foreach (var p in P) if (!p) count++;

            return count;
        }

        private int SolveLeft(int S, int K, bool[] P)
        {
            tw.WriteLine("L");
            var flips = 0;
            for (int i = 0; i + K <= P.Length; i++)
                if (!P[i])
                {
                    for (int j = i, c = 0; c < K && j < P.Length; j++, c++)
                        P[j] = !P[j];
                    flips++;
                    Write(P);
                }

            if (Check(P))
                return flips;
            else return int.MaxValue;
        }

        private int SolveRight(int S, int K, bool[] P)
        {
            tw.WriteLine("R");
            var flips = 0;
            for (int i = P.Length - 1; i - K + 1 >= 0; i--)
                if (!P[i])
                {
                    for (int j = i, c = 0; c < K && j >= 0; j--, c++)
                        P[j] = !P[j];
                    flips++;
                    Write(P);
                }

            if (Check(P))
                return flips;
            else return int.MaxValue;
        }

        private void Write(bool[] P, object k = null)
        {
            foreach (var p in P)
                tw.Write(p ? "+" : "-");
            tw.WriteLine(" " + k);
        }

        private void Randomise(bool[] P)
        {
            for (int i = 0; i < P.Length; i++)
                P[i] = (r.Next(0, 2) == 1);
        }

        internal ProbA Generate2()
        {
            using (var sw = File.CreateText("A-large.in"))
            {
                sw.WriteLine();
                for (int i = 0; i < 1000; i++)
                {
                    for (int j = 0; j < 1000; j++)
                        sw.Write(r.Next(2) == 0 ? "+" : "-");
                    sw.WriteLine(" 2");
                }
            }

            return this;
        }
    }
}
