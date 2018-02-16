using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob1A
    {
        internal void Run()
        {
            using (var sw = File.CreateText("1A-large.out"))
            using (var sr = File.OpenText("1A-large.in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var parts = sr.ReadLine().Split(' ').Select(l => int.Parse(l)).ToArray();
                    int R = parts[0], C = parts[1];

                    char[,] matrix = new char[R, C];
                    var kids = new Dictionary<char, Facts>();
                    
                    for (int r = 0; r < R; r++)
                    {
                        var line = sr.ReadLine().ToUpper();
                        for (int c = 0; c < C; c++)
                        {
                            var k = line[c];

                            if (k != '?')
                            {
                                if (!kids.ContainsKey(k))
                                    kids[k] = new Facts();

                                var K = kids[k];

                                if (r > K.maxR) K.maxR = r;
                                if (r < K.minR) K.minR = r;
                                if (c > K.maxC) K.maxC = c;
                                if (c < K.minC) K.minC = c;
                            }

                            matrix[r, c] = k;
                        }
                    }

                    Solve(R, C, matrix, kids.Values.ToList());

                    Populate(matrix, kids);

                    sw.WriteLine("Case #{0}:", i);
                    for (int r = 0; r < R; r++)
                    {
                        for (int c = 0; c < C; c++)
                            sw.Write(matrix[r, c]);
                        sw.WriteLine();
                    }
                    
                }
            }
        }

        private void Populate(char[,] matrix, Dictionary<char, Facts> kids)
        {
            foreach (var kide in kids)
            {
                var kid = kide.Value;
                for (int r = kid.minR; r <= kid.maxR; r++)
                    for (int c = kid.minC; c <= kid.maxC; c++)
                        matrix[r, c] = kide.Key;
            }
        }

        private void Solve(int R, int C, char[,] matrix, List<Facts> kids)
        {
            foreach (var fact in kids.OrderByDescending(k => k.Rlen))
            {
                while (true)
                {
                    fact.minR -= 1;
                    if (!Check(R, C, kids))
                    {
                        fact.minR += 1;
                        break;
                    }
                }

                while (true)
                {
                    fact.maxR += 1;
                    if (!Check(R, C, kids))
                    {
                        fact.maxR -= 1;
                        break;
                    }
                }
            }

            foreach (var fact in kids.OrderByDescending(k => k.Clen))
            {
            
                while (true)
                {
                    fact.minC -= 1;
                    if (!Check(R, C, kids))
                    {
                        fact.minC += 1;
                        break;
                    }
                }

                while (true)
                {
                    fact.maxC += 1;
                    if (!Check(R, C, kids))
                    {
                        fact.maxC -= 1;
                        break;
                    }
                }
            }
        }

        private bool Check(int R, int C, List<Facts> kids)
        {
            foreach (var kid in kids)
                if (kid.minR < 0 || kid.minC < 0 || kid.maxR >= R || kid.maxC >= C)
                    return false;

            for (int i=0; i<kids.Count; i++)
                for (int j = i+1; j < kids.Count; j++)
                {
                    var r1 = kids[i];
                    var r2 = kids[j];
                    var intersect = !(r2.minC > r1.maxC
                        || r2.maxC < r1.minC
                        || r2.minR > r1.maxR
                        || r2.maxR < r1.minR
                    );
                    if (intersect) return false;
                }

            return true;
        }
    }
    public class Facts
    {
        public int minR = int.MaxValue, maxR = -1, minC = int.MaxValue, maxC = -1;

        public override string ToString()
        {
            return String.Format("R:{0} - {1}, C:{2} - {3}", minR, maxR, minC, maxC);
        }

        public int Rlen { get { return maxR - minR + 1; } }

        public int Clen { get { return maxC - minC + 1; } }
    }
}
