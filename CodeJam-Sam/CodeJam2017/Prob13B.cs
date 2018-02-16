using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob13B
    {
        internal void Run()
        {
            using (var sw = File.CreateText(@"..\..\B-large.out"))
            using (var sr = File.OpenText(@"C:\Users\sperumal\Downloads\B-large-practice (2).in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var Q = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToArray();

                    var schedules = new List<Sched>();

                    for (int ac = 0; ac < Q[0]; ac++)
                    {
                        var c = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToArray();
                        schedules.Add(new Sched { S = c[0], E = c[1], C = true });
                    }

                    for (int aj = 0; aj < Q[1]; aj++)
                    {
                        var j = sr.ReadLine().Split(' ').Select(q => int.Parse(q)).ToArray();
                        schedules.Add(new Sched { S = j[0], E = j[1], C = false });
                    }

                    schedules = schedules.OrderBy(s => s.S).ToList();

                    var start = schedules[0].S;
                    var end = start + 24 * 60;

                    schedules.Add(new Sched { C = schedules[0].C, S = end, E = end });

                    var carePeriods = new List<Sched>();

                    Sched current = null;

                    foreach (var sched in schedules)
                    {
                        if (current != null && sched.C != current.C)
                        {
                            var gap = sched.S - current.E;

                            current.LE = current.E = sched.E;
                            if (gap > 0)
                                current.Gaps.Add(gap);
                            else if (gap < 0)
                                Debugger.Break();
                        }
                        else
                        {
                            if (current != null)
                            {
                                carePeriods.Add(current);
                                current = new Sched { C = !sched.C, S = current.E, E = sched.E, FS = sched.S, LE = sched.E };
                            }
                            else current = new Sched { C = !sched.C, S = sched.S, E = sched.E, FS = sched.S, LE = sched.E };
                        }
                    }

                    carePeriods.Add(current);

                    var C = carePeriods.Last().C;
                    int changes = 0;

                    foreach (var cp in carePeriods)
                    {
                        if (C != cp.C)
                        {
                            changes++;
                            C = cp.C;
                        }
                    }

                    var ccp = carePeriods.Where(cp => cp.C);
                    int sumC = ccp.Sum(cp => cp.D);
                    var ccj = carePeriods.Where(cp => !cp.C);
                    int sumJ = carePeriods.Where(cp => !cp.C).Sum(cp => cp.D);

                    var sumCSlack = ccp.Sum(cp => cp.Slack);
                    var sumJSlack = ccj.Sum(cp => cp.Slack);

                    if (sumC + sumJ != 1440) Debugger.Break();

                    if (sumC > 720)
                    {
                        var excess = sumC - 720 - sumCSlack;

                        if (excess > 0)
                        {
                            var gaps = ccp.SelectMany(cp => cp.Gaps).OrderByDescending(g => g).TakeWhile(g => (excess -= g) + g > 0);
                            changes += gaps.Count() * 2;
                        }
                    }
                    else if (sumJ > 720)
                    {
                        var excess = sumJ - 720 - sumJSlack;

                        if (excess > 0)
                        {
                            var gaps = ccj.SelectMany(cp => cp.Gaps).OrderByDescending(g => g).TakeWhile(g => (excess -= g) + g > 0);
                            changes += gaps.Count() * 2;
                        }
                    }

                    sw.WriteLine("Case #{0}: {1}", i, changes);
                }
            }
        }

        class Sched
        {
            public int S, E, FS, LE;
            public bool C;
            public List<int> Gaps = new List<int>();

            public int D { get { return E - S; } }
            public int Slack { get { return FS - S; } }

            public override string ToString()
            {
                return String.Format("S:{0}, E:{1}, FS:{2}, LE:{3}, Slack:{4}, C/J:{5}", S, E, FS, LE, Slack, C ? "Cam" : "Jam", " [" + String.Join(";", Gaps) + "]");
            }
        }

        class CarePeriod
        {
            public int S, D;
            public bool C;
        }
    }
}