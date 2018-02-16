using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2015
{
    class Round1B
    {
        internal void Solve()
        {
            var primes = Primes(100);

            using (var sw = new StreamWriter(@"F:\work\codejam\2015\B-small-practice.out"))
            using (var sw2 = new StreamWriter(@"F:\work\codejam\2015\B-small-practice.out.debug"))
            using (var sr = new StreamReader(@"F:\work\codejam\2015\test.int"))
            {
                sr.ReadLine();

                string line;

                int caseNo = 1;
                while ((line = sr.ReadLine()) != null)
                {
                    sw2.WriteLine("Case {0}", caseNo);
                    var numbers = line.Split(' ').Select(i => int.Parse(i)).ToArray();
                    int B = numbers[0], N = numbers[1];

                    line = sr.ReadLine();

                    int pos = 1;
                    var blist = line.Split(' ').Select(i => new Barber { Time = int.Parse(i), Index = pos++ }).OrderBy(b => b.Index).ThenBy(b => b.Time).ToList();

                    foreach (var b in blist)
                        b.CalculateFactors(primes);

                    var gcd = 1;
                    foreach (var p in primes)
                    {
                        var count = 0;
                        foreach (var b in blist)
                        {
                            var bcount = 0;
                            foreach (var pb in b.factors)
                                if (pb == p)
                                    bcount++;

                            if (bcount > count)
                                count = bcount;
                       }

                        if (count > 0)
                            for (int i=0; i<count; i++)
                            gcd *= p;
                    }

                    int cycleCount = 0;
                    foreach (var b in blist)
                        cycleCount += gcd / b.Time;

                    var rem = N % cycleCount;

                    int answer = 0;
                    if (rem == 0)
                        rem = cycleCount;
                    //else
                    {
                        var barbers = new PQueue(blist);

                        for (int i = 1; i < rem; i++)
                        {
                            var index = barbers.Allocate();
                            sw2.WriteLine(index);
                        }

                        answer = barbers.Allocate();
                        sw2.WriteLine(answer);
                    }
                    
                    sw.WriteLine("Case #{0}: {1}", caseNo++, answer);
                }
            }
        }

        private List<int> Primes(int max)
        {
            var list = new List<int> { 2, 3, 5, 7 };

            for (int i = 11; i < max; i+=2)
            {
                foreach (var p in list)
                    if (i % p == 0)
                        continue;

                list.Add(i);
            }

            return list;
        }
    }

    class Barber
    {
        public int Time, Index, BusyFor = 0;
        public List<int> factors = new List<int>();

        public override string ToString()
        {
            return String.Format("{0} {1} {2}", Index, Time, BusyFor);
        }

        internal void CalculateFactors(List<int> primes)
        {
            var t = Time;
            foreach (var p in primes)
                while (t % p == 0)
                {
                    factors.Add(p);
                    t /= p;

                    if (t == 1) break;
                }
        }
    }

    class PQueue
    {
        List<Barber> barbers;

        public PQueue(List<Barber> barbers) { this.barbers = barbers; }


        internal int Allocate()
        {
            var top = barbers[0];
            barbers.RemoveAt(0);

            top.BusyFor = top.Time;
            
            int j = 0;
            for (; j < barbers.Count; j++)
            {
                var currentBusy = barbers[j].BusyFor;
                // Move behind all free barbers
                if (currentBusy == 0) continue;
                // Skip those who will finish first
                if (currentBusy < top.BusyFor) continue;
                // Skip those who will finish at the same time, but are lower indexed
                if (currentBusy == top.BusyFor && barbers[j].Index < top.Index) continue;

                break;
            }

            barbers.Insert(j, top);

            // Pass time

            var time = barbers[0].BusyFor;

            if (time > 0)
                foreach (var barber in barbers)
                    barber.BusyFor -= time;

            return top.Index;
        }
    }
}
