using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class ProbB
    {
        internal void Run()
        {
            for (int i = 0; i < 100; i++)
                Process(Generate(18));
        }

        internal void Run(string p)
        {
            int count = 1;

            using (var sw = File.CreateText("B-large.out"))
                foreach (var line in File.ReadAllLines(p).Skip(1))
                    sw.WriteLine("Case #{0}: {1}", count++, Process(line.Select(c => int.Parse(c.ToString())).ToArray()));
        }

        private string Process(int[] n)
        {
            
            int max = 0, maxPos = 0;
            var output = new int[n.Length];

            for (int i = 0; i < n.Length; i++)
            {
                if (n[i] < max)
                {
                    // backtrack
                    output[maxPos] = n[maxPos] - 1;
                    for (int j = maxPos + 1; j < n.Length; j++)
                        output[j] = 9;
                    break;
                }
                if (n[i] > max) { max = n[i]; maxPos = i; }
                output[i] = n[i];
            }

            Print(n);
            Print(output);

            return new String(output.Select(d => d.ToString()[0]).SkipWhile(c => c == '0').ToArray());
        }

        private void Print(int[] n)
        {
            Console.WriteLine(new String(n.Select(d => d.ToString()[0]).SkipWhile(c => c == '0').ToArray()));
        }

        Random r = new Random();
        private int[] Generate(int p)
        {
            var cs = new int[p];
            for (int i = 0; i < p; i++)
                cs[i] = r.Next(0, 10);

            return cs;
        }
    }
}
