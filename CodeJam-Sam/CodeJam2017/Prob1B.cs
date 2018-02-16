using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob1B
    {
        internal void Run()
        {
            using (var sw = File.CreateText("B-large-practice.out"))
            using (var sr = File.OpenText("B-large-practice.in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    Console.WriteLine(i + ":");
                    var parts = sr.ReadLine().Split(' ').Select(l => int.Parse(l)).ToArray();
                    int N = parts[0], P = parts[1];
                    var recipe = sr.ReadLine().Split(' ').Select(l => int.Parse(l)).ToArray();
                    var packages = new List<Stack<Package>>();

                    for (int n = 0; n < N; n++)
                    {
                        packages.Add(new Stack<Package>(sr.ReadLine().Split(' ')
                            .Select(l => new Package { W = int.Parse(l), T = recipe[n] })
                            .Where(p => p.IsValid())
                            .OrderByDescending(p => p.minn)
                            .ToList()));

                        Console.WriteLine(String.Join(", ", packages[n]));
                    }

                    int result = 0, pass = 0;
                    while (true)
                    {
                        var empty = false;
                        foreach (var stack in packages)
                            empty |= stack.Count == 0;
                        if (empty) break;

                        int min = packages[0].Peek().minn, max = packages[0].Peek().maxn, absMin = int.MaxValue;;
                        foreach (var stack in packages)
                        {
                            min = Math.Max(min, stack.Peek().minn);
                            max = Math.Min(max, stack.Peek().maxn);
                            absMin = Math.Min(absMin, stack.Peek().minn);
                        }

                        if (min <= max)
                        {
                            int matchCount = 0;
                            foreach (var stack in packages)
                            {
                                var p = stack.Peek();
                                if (p.minn <= min && p.maxn >= max)
                                    matchCount++;
                            }

                            if (matchCount == N) result++;

                            foreach (var stack in packages)
                                stack.Pop();
                        }
                        else
                        {
                            var minStacks = new List<Stack<Package>>();
                            foreach (var stack in packages)
                                if (absMin == stack.Peek().minn) minStacks.Add(stack);

                            var minMax = minStacks.Min(s => s.Peek().maxn);

                            foreach (var stack in minStacks)
                                if (stack.Peek().maxn == minMax)
                                    stack.Pop();
                            //minStacks.OrderBy(s => s.Peek().maxn).FirstOrDefault().Pop();
                        }

                        //Console.WriteLine("Pass: {0}", pass++);
                        //foreach (var package in packages)
                        //    Console.WriteLine(String.Join(", ", package));
                    }

                    sw.WriteLine("Case #{0}: {1}", i, result);
                }
            }
        }

        public class Package
        {
            public int W;
            public int T;
            public int minn, maxn;
            public bool v;

            public override string ToString()
            {
                return string.Format("W:{0}, T:{1}, ({2}-{3})", W, T, minn, maxn);
            }

            internal bool IsValid()
            {
                var min = W / 1.1;
                var max = W / 0.9;

                maxn = (int)Math.Floor(max / T);
                minn = (int)Math.Ceiling(min / T);

                v = minn > 0 && minn <= maxn;

                if (v)
                for (int i = minn; i <= maxn; i++)
                {
                    var check = Math.Abs((int)(W / (i * T)) - ((double)W / (i * T)));
                    if (check > 0.1 && check < 0.9) Debugger.Break();
                }

                return v;
            }
        }
    }
}
