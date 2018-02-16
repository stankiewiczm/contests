using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob13C
    {
        internal void Run()
        {
            using (var sw = File.CreateText(@"..\..\C-small.out"))
            using (var sr = File.OpenText(@"C:\Users\sperumal\Downloads\C-small-1-attempt1.in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var K = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToArray()[0];
                    var U = double.Parse(sr.ReadLine());
                    var ps = sr.ReadLine().Split(' ').Select(q => double.Parse(q)).ToArray();

                    var p = ps.Sum();

                    var po = ps.Select(pp => 1 - pp).ToArray();
                    var pos = po.Sum();

                    var mult = 1.0;
                    for (int j = 0; j < K; j++)
                    {
                        ps[j] += U * po[j] / pos;

                        mult *= ps[j];
                    }

                    sw.WriteLine("Case #{0}: {1}", i, Math.Pow(ps.Average() + U / K, K));
                }
            }
        }
    }
}