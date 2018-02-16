using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeJam2016
{
    class Round11a
    {
        static void Main(string[] args)
        {
            new Round11a().Run("A-large.in");
        }

        TextWriter sw;
        int caseNo = 1;
        internal void Run(string p)
        {
            using (var sr = File.OpenText(p))
            using (sw = File.CreateText("A1-large.out"))
            {
                Console.WriteLine(sr.ReadLine());

                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    sw.WriteLine("Case #{0}: {1}", caseNo++, Check((line)));
                }
            }
        }

        private object Check(string p)
        {
            var last = 'A';
            var sb = new StringBuilder();

            foreach (var c in p)
                if (c >= last)
                {
                    sb.Insert(0, c);
                    last = c;
                }
                else sb.Append(c);

            return sb.ToString();
        }        
    }
}
