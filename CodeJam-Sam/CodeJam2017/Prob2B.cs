using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class Prob2B
    {
        TextReader sr;
        TextWriter sw;

        int R, C;

        internal void Run()
        {
            using (sw = File.CreateText(@"..\..\C-small.out"))
            using (sr = File.OpenText(@"C-small-attempt0.in"))
            {
                var T = int.Parse(sr.ReadLine());
                for (int i = 1; i <= T; i++)
                {
                    var parts = sr.ReadLine().Split(' ').Select(l => int.Parse(l)).ToArray();
                    R = parts[0]; C = parts[1];

                    var matrixh = new char[R, C];
                    var matrixv = new char[R, C];

                    for (int r = 0; r < R; r++)
                    {
                        var line = sr.ReadLine();
                        for (int c = 0; c < C; c++)
                        {
                            if (line[c] == '|') 
                                matrixh[r, c] = '-';
                            else matrixh[r, c] = line[c];

                            if (line[c] == '-')
                                matrixv[r, c] = '|';
                            else matrixv[r, c] = line[c];
                        }
                    }

                    var horiz = Fill(matrixh);
                    var vert = Fill(matrixv);

                    if (Check(horiz)) { sw.WriteLine("Case #{0}: {1}", i, "POSSIBLE"); Write(sw, Fill(matrixh)); }
                    else if (Check(vert)) { sw.WriteLine("Case #{0}: {1}", i, "POSSIBLE"); Write(sw, Fill(matrixv)); }
                    else { sw.WriteLine("Case #{0}: {1}", i, "IMPOSSIBLE"); Write(sw, Fill(matrixh)); }
                    
                }
            }
        }

        private char[,] Fill(char[,] matrix)
        {
            var check = new char[R, C];
            Array.Copy(matrix, check, check.LongLength);

            for (int r = 0; r < R; r++)
                for (int c = 0; c < C; c++)
                {
                    if (check[r, c] == '|')
                    {
                        for (int r2 = r - 1; r2 >= 0; r2--)
                        {
                            if (check[r2, c] == '.' || check[r2, c] == '*')
                                check[r2, c] = '*';
                            else
                            {
                                if (check[r2, c] == '|' || check[r2, c] == '-')
                                    check[r2, c] = 'X';
                                break;
                            }
                        }

                        for (int r2 = r + 1; r2 < R; r2++)
                        {
                            if (check[r2, c] == '.' || check[r2, c] == '*')
                                check[r2, c] = '*';
                            else
                            {
                                if (check[r2, c] == '|' || check[r2, c] == '-')
                                    check[r2, c] = 'X';
                                break;
                            }
                        }
                    }
                    else if (check[r, c] == '-')
                    {
                        for (int c2 = c - 1; c2 >= 0; c2--)
                        {
                            if (check[r, c2] == '.' || check[r, c2] == '*')
                                check[r, c2] = '*';
                            else
                            {
                                if (check[r, c2] == '|' || check[r, c2] == '-')
                                    check[r, c2] = 'X';
                                break;
                            }
                        }

                        for (int c2 = c + 1; c2 < C; c2++)
                        {
                            if (check[r, c2] == '.' || check[r, c2] == '*')
                                check[r, c2] = '*';
                            else
                            {
                                if (check[r, c2] == '|' || check[r, c2] == '-')
                                    check[r, c2] = 'X';
                                break;
                            }
                        }
                    }
                }

            return check;
        }

        private bool Check(char[,] matrix)
        {
            for (int r = 0; r < R; r++)
                for (int c = 0; c < C; c++)
                    if (matrix[r, c] == '.' || matrix[r, c] == 'X')
                        return false;
            return true;
        }        

        private void CheckPossible(char[,] matrix)
        {
            var check = new char[R, C];
            Array.Copy(matrix, check, check.LongLength);

            for (int r = 0; r < R; r++)
                for (int c = 0; c < C; c++)
                {
                    if (check[r, c] == '|' || check[r, c] == '-')
                    {
                        for (int r2 = 0; r2 < R; r2++)
                        {
                            if (check[r2, c] == '.')
                                check[r2, c] = '*';
                        }

                        for (int c2 = 0; c2 < C; c2++)
                        {
                            if (check[r, c2] == '.')
                                check[r, c2] = '*';
                        }
                    }
                }
        }

        public static void Write(TextWriter tw, char[,] a)
        {
            for (int r = 0; r < a.GetLength(0); r++)
            {
                for (int c = 0; c < a.GetLength(1); c++)
                    tw.Write(a[r, c]);
                tw.WriteLine();
            }
        }
    }
}
