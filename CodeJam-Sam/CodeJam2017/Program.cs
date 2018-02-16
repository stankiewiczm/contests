using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeJam2017
{
    class Program
    {
        static void Main(string[] args)
        {
            //Generate();
            new Prob2B()
                //.Generate();
                .Run();
        }

        private static void Generate()
        {
            var rand = new Random();
            using (var sw = File.CreateText("C-small0.in"))
            {
                sw.WriteLine(100);
                for (int t = 0; t < 100; t++)
                {
                    var R = rand.Next(1, 6);
                    var C = rand.Next(1, 51);
                    sw.WriteLine("{0} {1}", R, C);

                    for (int r = 0; r < R; r++)
                    {
                        for (int c = 0; c < C; c++)
                        {
                            var rn = rand.NextDouble();
                            char o = '.';
                            if (r == 0 || r + 1 == R || c == 0 || c + 1 == C)
                            {
                                if (rn < 0.5)
                                    o = '#';
                                else if (rn < 0.6)
                                    o = '|';
                                else if (rn < 0.7)
                                    o = '-';
                            }
                            else
                            {
                                if (rn < 0.1)
                                    o = '#';
                                else if (rn < 0.2)
                                    o = '|';
                                else if (rn < 0.3)
                                    o = '-';
                            }
                            sw.Write(o);
                        }
                        sw.WriteLine();
                    }
                }
            }
        }
    }
}
