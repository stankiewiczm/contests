using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob13A
    {
        internal void Run()
        {
            using (var sw = File.CreateText(@"..\..\A-large.out"))
            using (var sr = File.OpenText(@"C:\Users\sperumal\Downloads\A-large (1).in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var Q = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToArray();
                    var N = Q[0];
                    var K = Q[1];

                    var pancakes = new List<P>();
                    for (int j = 0; j < N; j++)
                    {
                        var PS = sr.ReadLine().Split(' ').Select(q => long.Parse(q)).ToArray();
                        pancakes.Add(new P { R = PS[0], H = PS[1] });
                    }

                    var pradii = pancakes.OrderByDescending(p => p.R).ToList();
                    var pheight = pancakes.OrderByDescending(p => p.H * p.R).ToList();

                    long maxArea = 0;

                    foreach (var pcake in pradii)
                    {
                        var others = pheight.Where(p2 => p2.Id != pcake.Id && p2.R <= pcake.R).Take(K - 1).ToList();

                        var area = pcake.VertArea() + pcake.HorizArea() + others.Sum(p2 => p2.VertArea());

                        if (area > maxArea)
                            if (others.Count != K - 1)
                                continue;
                            else maxArea = Math.Max(maxArea, area);
                    }

                    //var maxArea2 = test(pancakes, K);

                    //var list = test2(pancakes, K);

                    //var maxArea3 = list.Sum(p3 => p3.VertArea()) + list.Peek().HorizArea();

                    //if (maxArea != maxArea2) Debugger.Break();

                    sw.WriteLine("Case #{0}: {1}", i, maxArea * (decimal)Math.PI);
                }
            }
        }

        private Stack<P> test2(List<P> pancakes, int K, int d = 0, long maxR = 0)
        {
            long maxArea = 0;

            if (K > 0)
            {
                var len = pancakes.Count;
                Stack<P> localStack = new Stack<P>();
                for (int i = 0; i < len; i++)
                {
                    var p = pancakes[i];
                    var area = p.VertArea();
                    if (d == 0)
                        area += p.HorizArea();
                    else if (p.R > maxR)
                        continue;

                    pancakes.RemoveAt(i);
                    var stack = test2(pancakes, K - 1, d + 1, p.R);
                    pancakes.Insert(i, p);

                    stack.Push(p);

                    if (stack.Sum(p2 => p2.VertArea()) > maxArea)
                    {
                        maxArea = stack.Sum(p2 => p2.VertArea());
                        localStack = stack;
                    }
                }

                return localStack;
            }
            else return new Stack<P>();
        }

        private long test(List<P> pancakes, int K, int d = 0, long maxR = 0)
        {
            long maxArea = 0;

            if (K > 0)
            {
                var len = pancakes.Count;
                for (int i = 0; i < len; i++)
                {
                    var p = pancakes[i];
                    var area = p.VertArea();
                    if (d == 0)
                        area += p.HorizArea();
                    else if (p.R > maxR)
                        continue;

                    pancakes.RemoveAt(i);
                    area += test(pancakes, K - 1, d + 1, p.R);
                    pancakes.Insert(i, p);

                    maxArea = Math.Max(area, maxArea);
                }
            }

            return maxArea;
        }

        class P
        {
            static int IdGen = 0;
            public int Id = IdGen++;
            public long R, H;

            public override string ToString()
            {
                return String.Format(String.Join(", ", R.ToString("N"), H.ToString("N"), HorizArea() + VertArea(), Id));
            }

            public long VertArea()
            {
                return checked(2 * R * H);
            }

            public long HorizArea()
            {
                return checked(R * R);
            }
        }
    }
}