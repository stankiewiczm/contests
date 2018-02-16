using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeJam2017
{
    class ProbC
    {
        internal void Run()
        {
            Simulate(Create(50), 50);
        }

        private void Simulate(bool[] stalls, int visitors)
        {
            var Stalls = new Stall[stalls.Length];
            Stalls[0] = new Stall { Occupied = true };
            Stalls[Stalls.Length - 1] = new Stall { Occupied = true };

            for (int i = 1; i < Stalls.Length - 1; i++)
                Stalls[i] = new Stall { I = i, L = i - 1, R = Stalls.Length - i - 2 };

            using (var excel = new ProbCExcel("probc.xlsx"))
            {
                while (visitors-- > 0)
                {
                    var maxmin = Stalls.Max(s => s.MinLR);
                    var maxmax = Stalls.Where(s => !s.Occupied && s.MinLR == maxmin)
                        .OrderByDescending(s => s.MaxLR)
                        .ThenBy(s => s.I)
                        .First();

                    excel.Output(Stalls, maxmin, maxmax);                

                    maxmax.L = maxmax.R = 0;
                    maxmax.Occupied = true;

                    for (int l = maxmax.I - 1, o = 0; l >= 0; l--, o++)
                    {
                        if (Stalls[l].Occupied) break;
                        else Stalls[l].R = o;
                    }

                    for (int r = maxmax.I + 1, o = 0; r < Stalls.Length; r++, o++)
                    {
                        if (Stalls[r].Occupied) break;
                        else Stalls[r].L = o;
                    }

                    //excel.Output(Stalls, maxmin);
                }

                return;

                //while (visitors-- > 0)
                //{
                //    var maxlr = new int[stalls.Length];
                //    var minlr = new int[stalls.Length];
                //    for (int i = 1; i < stalls.Length - 1; i++)
                //    {
                //        if (stalls[i]) continue;

                //        int left = 0, right = 0;
                //        for (int l = i - 1; l >= 0 && !stalls[l]; l--, left++) ;
                //        for (int r = i + 1; r < stalls.Length && !stalls[r]; r++, right++) ;
                //        minlr[i] = Math.Min(left, right);
                //        maxlr[i] = Math.Max(left, right);
                //    }

                //    var maxmin = minlr.Max();

                //    var maxmax = 0;
                //    for (int i = 1; i < stalls.Length - 1; i++)
                //        if (minlr[i] == maxmin && maxlr[i] > maxmax)
                //            maxmax = maxlr[i];

                //    int selected = -1;

                //    for (int i = 1; i < stalls.Length; i++)
                //        if (!stalls[i] && minlr[i] == maxmin && maxmax == maxlr[i])
                //        {
                //            selected = i;
                //            stalls[i] = true;
                //            break;
                //        }

                    //excel.Output(stalls, minlr, maxlr, maxmin, selected);
                    //break;
                //}
            }
        }

        private bool[] Create(int p)
        {
            var stalls = new bool[p + 2];
            stalls[0] = stalls[p + 1] = true;
            return stalls;
        }
    }

    public class Stall
    {
        public bool Occupied = false;
        public int L, R;
        public int I;

        public int MinLR { get { return Math.Min(L, R); } }
        public int MaxLR { get { return Math.Max(L, R); } }
    }
}
