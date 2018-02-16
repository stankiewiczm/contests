using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob1ATest
    {
        internal void Run()
        {
            using (var sw = File.CreateText("1A-test.in"))
            {
                var rnd = new Random();
                sw.WriteLine(100);
                for (int i = 1; i <= 100; i++)
                {
                    sw.WriteLine("25 25");
                    var matrix = new char[25, 25];
                    for (int c = 0; c < 26; c++)
                    {
                        matrix[rnd.Next(0, 25), rnd.Next(0, 25)] = (char)('A' + c);
                    }
                    for (int r = 0; r < 25; r++)
                    {
                        for (int c = 0; c < 25; c++)
                            if (matrix[r, c] != 0)
                                sw.Write(matrix[r, c]);
                            else sw.Write('?');
                        sw.WriteLine();
                    }
                }
            }
        }
    }
}
