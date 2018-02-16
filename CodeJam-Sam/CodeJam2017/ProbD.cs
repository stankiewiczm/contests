using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;

namespace CodeJam2017
{
    class ProbD
    {
        internal void Run()
        {
            using (var excel = new ProbCExcel("probd.xlsx"))
            {
                var ws = excel.package.Workbook.Worksheets.Add("10");
                for (int r=1; r<=10; r++)
                    for (int c = 1; c <= 10; c++)
                    {
                        if ((r + c) % 2 == 1)
                        {
                            ws.Cells[r, c].Style.Fill.PatternType = OfficeOpenXml.Style.ExcelFillStyle.Solid;
                            ws.Cells[r, c].Style.Fill.BackgroundColor.SetColor(Color.SteelBlue);
                        }
                    }

                ws = excel.package.Workbook.Worksheets.Add("9");
                for (int r = 1; r <= 9; r++)
                    for (int c = 1; c <= 9; c++)
                    {
                        if ((r + c) % 2 == 0)
                        {
                            ws.Cells[r, c].Style.Fill.PatternType = OfficeOpenXml.Style.ExcelFillStyle.Solid;
                            ws.Cells[r, c].Style.Fill.BackgroundColor.SetColor(Color.SteelBlue);
                        }
                    }
            }
        }
    }
}
