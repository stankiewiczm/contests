using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob12A
    {
        internal void Run()
        {
            using (var sw = File.CreateText("12A-large.out"))
            using (var sr = File.OpenText("A-large.in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var Q = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToArray();
                    var D = Q[0];
                    var N = Q[1];
                    var horses = new List<Horse>();

                    for (int j = 0; j < N; j++)
                    {
                        var l = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToList();
                        
                        horses.Add(new Horse
                        {
                            K = l[0],
                            S = l[1],
                            D = D,
                            R = D - l[0],

                        });                        
                    }

                    var maxt = horses.Max(h => h.T);

                    sw.WriteLine("Case #{0}: {1}", i, D / maxt);
                }
            }
        }
    }

    class Horse
    {
        public int K, S, D, R;
        public Decimal T { get { return R / (decimal)S; } }
    }
}