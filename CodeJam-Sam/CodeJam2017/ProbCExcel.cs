using OfficeOpenXml;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeJam2017
{
    class ProbCExcel : IDisposable
    {
        Stream s;
        public ExcelPackage package;
        ExcelWorksheet ws;

        public ProbCExcel(string p)
        {
            s = File.Create(p);
            package = new ExcelPackage(s);
            ws = package.Workbook.Worksheets.Add("Data");
            ws.Cells.Style.Fill.PatternType = OfficeOpenXml.Style.ExcelFillStyle.Solid;
            ws.Cells.Style.Fill.BackgroundColor.SetColor(Color.Transparent);
            ws.DefaultColWidth = 4;
        }

        public void Dispose()
        {

            package.Save();

            if (package != null) package.Dispose();
            if (s != null) s.Dispose();
        }

        int row = 1;
        internal void Output(bool[] stalls, int[] minlr, int[] maxlr, int maxmin, int selected)
        {
            for (int i = 0, c = 1; i < stalls.Length; i++, c++)
            {
                if (row == 1)
                    ws.Column(c).Width = 6;

                ws.Cells[row, c].Value = String.Format("{0},{1}", minlr[i], maxlr[i]);

                if (minlr[i] == maxmin)
                    ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(Color.LightSteelBlue);

                if (stalls[i])
                    ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(Color.Red);

                if (i == selected)
                    ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(Color.LightSeaGreen);


            }

            row++;
        }

        internal void Output(Stall[] Stalls, int maxmin, Stall selected)
        {
            for (int i = 0, c = 1; i < Stalls.Length; i++, c++)
            {
                if (row == 1)
                    ws.Column(c).Width = 6;

                var stall = Stalls[i];

                //ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(stalls[i] ? Color.Red : Color.Green);
                ws.Cells[row, c].Value = String.Format("{0},{1}", stall.L, stall.R);

                if (stall.MinLR == maxmin)
                    ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(Color.LightSteelBlue);

                if (stall.Occupied)
                    ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(Color.Red);

                if (stall == selected)
                    ws.Cells[row, c].Style.Fill.BackgroundColor.SetColor(Color.LightSeaGreen);


            }

            row++;
        }

        public void Output(ProbC2.Node node)
        {
            Output(node, 1);
            row++;
        }

        public int Output(ProbC2.Node node, int startCell)
        {
            if (node.IsSplit)
            {
                if (node.Left.Size > 0)
                    startCell = Output(node.Left, startCell);
                ws.Cells[row, startCell].Style.Fill.BackgroundColor.SetColor(Color.Red);
                ws.Cells[row, startCell].Value = String.Format("{0},{1}", node.SL, node.SR);
                startCell++;
                if (node.Right.Size > 0) 
                    startCell = Output(node.Right, startCell);
                return startCell;
            }
            else
            {
                ws.Cells[row, startCell, row, startCell + node.Size - 1].Style.Border.BorderAround(OfficeOpenXml.Style.ExcelBorderStyle.Thick);
                return startCell + node.Size;
            }
        }

        internal void SizeColumns(int p)
        {
            for (int i = 1; i <= p; i++)
            {
                ws.Column(i).Width = 6;
                ws.Column(i).Style.Border.BorderAround(OfficeOpenXml.Style.ExcelBorderStyle.Thin);
            }
        }

        internal void Output(int[,] matrix)
        {
            HashSet<int> diagonalsdown = new HashSet<int>();
            HashSet<int> diagonalsup = new HashSet<int>();

            var rowc = matrix.GetLength(0);
            var colc = matrix.GetLength(1);

            for (int i = rowc - 1; i >= 0; i--)
                for (int j = colc - 1; j >= 0; j--)
                {
                    ws.Cells[i+1, j+1].Value = matrix[i, j];
                    if (matrix[i, j] == 1)
                    {
                        diagonalsdown.Add(i + j);
                        diagonalsdown.Add(i - j);

                        for (int r = 0; r < rowc; r++)
                            ws.Cells[r + 1, j + 1].Style.Fill.BackgroundColor.SetColor(Color.Green);

                        for (int c = 0; c < colc; c++)
                            ws.Cells[j + 1, c + 1].Style.Fill.BackgroundColor.SetColor(Color.Yellow);
                    }
                }

            for (int i=rowc - 1; i >= 0; i--)
                for (int j = colc - 1; j >= 0; j--)
                {
                    if (diagonalsdown.Contains(i + j))
                        ws.Cells[i + 1, j + 1].Style.Fill.BackgroundColor.SetColor(Color.SteelBlue);
                    if (diagonalsdown.Contains(i - j))
                        ws.Cells[i + 1, j + 1].Style.Fill.BackgroundColor.SetColor(Color.SteelBlue);
                }
        }
    }
}
