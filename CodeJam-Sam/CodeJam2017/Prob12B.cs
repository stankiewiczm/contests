using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob12B
    {
        TextWriter sw;
        internal void Run()
        {
            using (var sw = File.CreateText(@"..\..\B-large.out"))
            using (var sr = File.OpenText("B-large-practice (1).in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var list = sr.ReadLine().Split(' ').Select(v => int.Parse(v)).ToList();

                    var stallSize = list[0];
                    var colours = list.Skip(1).ToList();
                    var horses = new List<char>();
                    var horseCount = colours.Sum();

                    //if (horseCount > stallSize) { sw.WriteLine("Case #{0}: {1}", i, "IMPOSSIBLE"); break; }

                    bool impossible = false;

                    var colourLookup = new[] { 'R', 'O', 'Y', 'G', 'B', 'V' };
                    for (int j = 0; j < colours.Count; j++)
                        for (int k = 0; k < colours[j]; k++)
                            horses.Add(colourLookup[j]);

                    var mostCommon = horses.GroupBy(h => h).Select(g => new Rainbowcorn { K = g.Key, C = g.Count() }).OrderByDescending(g => g.C).ToList();
                    var dict = colourLookup.ToDictionary(h => h, h => 0);

                    foreach (var mc in mostCommon)
                        dict[mc.K] = mc.C;

                    //if (2 * dict['G'] > dict['R']) impossible = true;
                    //if (2 * dict['V'] > dict['Y']) impossible = true;
                    //if (2 * dict['O'] > dict['B']) impossible = true;

                    
                    string result = null;

                    var dict3 = dict.ToDictionary(d => d.Key);
                    if (dict['G'] == dict['R'] && dict['G'] + dict['R'] == stallSize) result = Generate('G', 'R', stallSize);
                    else if (dict['V'] == dict['Y'] && dict['V'] + dict['Y'] == stallSize) result = Generate('V', 'Y', stallSize);
                    else if (dict['O'] == dict['B'] && dict['O'] + dict['B'] == stallSize) result = Generate('O', 'B', stallSize);
                    else if (dict['G'] > dict['R']) impossible = true;
                    else if (dict['V'] > dict['Y']) impossible = true;
                    else if (dict['O'] > dict['B']) impossible = true;
                    else
                    {
                        //var dict2 = dict.ToDictionary(d => d.Key, d => Generate(d.Key, d.Value));

                        var reds = Generate('G', dict['G']).Concat(Generate('R', dict['R'] - (dict['G'] > 0 ? dict['G'] + 1 : 0))).ToList();
                        var yellows = Generate('V', dict['V']).Concat(Generate('Y', dict['Y'] - (dict['V'] > 0 ? dict['V'] + 1 : 0))).ToList();
                        var blues = Generate('O', dict['O']).Concat(Generate('B', dict['B'] - (dict['O'] > 0 ? dict['O'] + 1 : 0))).ToList();

                        var lists = new List<List<string>> { reds, yellows, blues }.OrderByDescending(l => l.Count).ToList();
                        //if (lists[0].Count > lists.Sum(l => l.Count) / 2)
                        //    Fix(
                        var ultraList = lists.SelectMany(l => l).ToList();

                        var sb = new StringBuilder();
                        var half = ultraList.Count / 2;
                        for (int g = 0; g < half; g++)
                        {
                            sb.Append(ultraList[g]);
                            if (g + half < ultraList.Count) sb.Append(ultraList[g + half]);
                        }

                        result = sb.ToString();
                    }
                    
                    if (!impossible && !String.IsNullOrWhiteSpace(result) && Check(result))
                        sw.WriteLine("Case #{0}: {1}", i, result);
                    else sw.WriteLine("Case #{0}: {1}", i, "IMPOSSIBLE");
                }
            }
        }

        private string Generate(char p1, char p2, int stallSize)
        {
            var sb = new StringBuilder();
            for (int i = 0; i < stallSize; i += 2)
            {
                sb.Append(p2); sb.Append(p1);
            }

            return sb.ToString();
        }

        private object Generate(KeyValuePair<char, int> m, KeyValuePair<char, int> s)
        {
            //if (m.Value > 2 * s.Value)
            //    return Generate(m.Key, m.Value).Concat(Generate(s.Key, s.Value - m.Value * 2));
            //else return Generate(
            return null;
        }

        private List<string> Generate(char p1, int p2)
        {
            string s = p1.ToString();
            if (p1 == 'G') s = "RG";
            if (p1 == 'V') s = "YV";
            if (p1 == 'O') s = "BO";

            if (s.Length == 1)
            {
                var list = new List<string>();
                for (int i = 0; i < p2; i++)
                    list.Add(s);

                return list;
            }
            else if (p2 > 0)
            {
                var sb = new StringBuilder();
                for (int i = 0; i < p2; i++)
                    sb.Append(s);
                sb.Append(s[0]);

                return new List<string> { sb.ToString() };
            }
            else return new List<string>();
        }

        private bool Check(string result)
        {
            for (int i = 1; i < result.Length; i++)
                if (result[i - 1] == result[i]) return false;

            if (result[0] == result[result.Length - 1]) return false;

            return true;
        }

        private int Populate(char[] stalls, Rainbowcorn r, int startIndex)
        {
            int j;

            for (j = 0; j < r.C; j++, startIndex += 2)
            {
                if (startIndex >= stalls.Length) startIndex = 1;
                stalls[startIndex] = r.K;
            }

            return startIndex;
        }

        internal Prob12B Generate()
        {
            using (var sw = File.CreateText("B-large.in"))
            {
                var r = new Random();
                sw.WriteLine(20);
                for (int i = 0; i < 20; i++)
                {
                    var list = new List<int>();
                    for (int j = 0; j < 6; j++)
                        list.Add(r.Next(5, 20));
                    list.Insert(0, list.Sum());
                    sw.WriteLine(String.Join(" ", list));
                }                
            }
            return this;
        }
    }

    class Rainbowcorn
    {
        public Char K;
        public int C;
    }
}