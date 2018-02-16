using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2015
{
    class Round1A
    {
        internal void Solve()
        {
            using (var sw = new StreamWriter(@"F:\work\codejam\2015\A-large-practice.out"))
            using (var sr = new StreamReader(@"F:\work\codejam\2015\A-large-practice.in"))
            {
                var count = int.Parse(sr.ReadLine());
                
                string l;
                int caseCount = 1;
                while ((l = sr.ReadLine()) != null)
                {
                    var values = sr.ReadLine().Split(' ').Select(i => int.Parse(i)).ToList();

                    int mcount = values[0], totalEaten1 = 0, maxRate = 0;
                    for (int i=1; i<values.Count; i++)
                    {
                        var m = values[i];
                        if (m < mcount)
                        {
                            var eaten = mcount - m;
                            totalEaten1 += eaten;
                            if (maxRate < eaten)
                                maxRate = eaten;
                        }

                        mcount = m;                        
                    }

                    int totalEaten2 = 0;

                    for (int i = 0; i < values.Count - 1; i++)
                    {
                        totalEaten2 += Math.Min(values[i], maxRate);
                    }
                    
                    sw.WriteLine("Case #{0}: {1} {2}", caseCount++, totalEaten1, totalEaten2);
                }
            }
        }
    }
}
