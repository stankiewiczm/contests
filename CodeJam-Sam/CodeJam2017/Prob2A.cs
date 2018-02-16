using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob2A
    {
        TextReader sr;
        TextWriter sw;

        internal void Run()
        {
            using (sw = File.CreateText(@"..\..\A-small.out"))
            using (sr = File.OpenText(@"A-small.in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var parts = sr.ReadLine().Split(' ').Select(l => int.Parse(l)).ToArray();
                    int N = parts[0], P = parts[1];

                    var groups = sr.ReadLine().Split(' ').Select(l => int.Parse(l)).ToArray();

                    int result = 0;
                    if (P == 2)
                    {
                        var remGroups = groups.GroupBy(g => g % 2).OrderBy(r => r.Key).ToArray();
                        result = remGroups[0].Count() + (int)Math.Ceiling(remGroups[1].Count() / 2.0);
                    }
                    else if (P == 3)
                        result = Solve3(groups);

                    sw.WriteLine("Case #{0}: {1}", i, result);
                }
            }
        }

        private int Solve3(int[] groups)
        {
            var result = 0;
            var remGroups = groups.GroupBy(g => g % 3).ToDictionary(g => g.Key, g => g.Count());

            var dict = new Dictionary<int, int>();
            for (int i = 0; i < 3; i++)
                if (remGroups.ContainsKey(i))
                    dict[i] = remGroups[i];
                else dict[i] = 0;

            result += dict[0];

            var rem1 = dict[1];
            var rem2 = dict[2];

            var match = Math.Min(rem1, rem2);
            result += match;

            var others = Math.Max(rem1, rem2) - match;
            result += (int)Math.Ceiling(others / 3.0);

            return result;
        }

        private int Solve4(int[] groups)
        {
            var result = 0;
            var remGroups = groups.GroupBy(g => g % 4).ToDictionary(g => g.Key, g => g.Count());

            var dict = new Dictionary<int, int>();
            for (int i = 0; i < 4; i++)
                if (remGroups.ContainsKey(i))
                    dict[i] = remGroups[i];
                else dict[i] = 0;

            result += dict[0];

            var rem1 = dict[1];
            var rem2 = dict[2];
            var rem3 = dict[3];

            var match = Math.Min(rem1, rem3);
            result += match;

            result += rem2 / 2;

            rem2 = rem2 % 2;

            var rem13 = Math.Max(rem1, rem3) - match;

            if (rem2 == 1)
            {
                if (rem13 >= 2)
                {
                    result++;
                    rem13 -= 2;
                }
                else { result += 1; rem13 = 0; }
            }
            
            result += (int)Math.Ceiling(rem13 / 4.0);

            return result;
        }
    }
}
