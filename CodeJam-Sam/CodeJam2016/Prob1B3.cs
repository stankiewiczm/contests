using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CodeJam2016
{
    class Prob1B3
    {
        int i;
        Dictionary<string, Node> dictL, dictR;
        Dictionary<string, LineNode> lineDict;
        internal void Run()
        {
            var lines = File.ReadAllLines("C-large-practice.in");

            var n = int.Parse(lines[0]);

            i = 1;
            using (var sw = File.CreateText("C.out"))
            {
                int index = 1;
                while (index < lines.Length)
                {
                    var count = int.Parse(lines[index++]);
                    dictL = new Dictionary<string, Node>();
                    dictR = new Dictionary<string, Node>();
                    lineDict = new Dictionary<string, LineNode>();

                    for (int j = 0; j < count; j++, index++)
                    {
                        var line = lines[index];
                        var words = line.Split(' ');
                        if (!dictL.ContainsKey(words[0]))
                            dictL[words[0]] = new Node { Key = words[0] };

                        var left = dictL[words[0]];
                        left.Links.Add(words[1]);
                        left.Lines.Add(line);

                        if (!dictR.ContainsKey(words[1]))
                            dictR[words[1]] = new Node { Key = words[1] };

                        var right = dictR[words[1]];
                        right.Links.Add(words[0]);
                        right.Lines.Add(line);

                        var lineNode = new LineNode
                        {
                            Line = line,
                            Left = words[0],
                            Right = words[1],
                        };
                        lineDict[line] = lineNode;

                        left.LineLinks.Add(lineNode);
                        right.LineLinks.Add(lineNode);
                    }

                    foreach (var linenode in lineDict.Values)
                    {
                        linenode.LeftLinks = dictL[linenode.Left].LineLinks.Where(ll => ll.Line != linenode.Line).ToList();
                        linenode.RightLinks = dictR[linenode.Right].LineLinks.Where(ll => ll.Line != linenode.Line).ToList();
                    }

                    duplicateCount = 0;
                    Process();

                    sw.WriteLine("Case #{0}: {1}", i++, duplicateCount);

                    foreach (var line in lineDict.Values.OrderByDescending(l => l.Unique).ThenBy(l => l.Line))
                        sw.WriteLine(String.Join(";", line.Line, line.Unique, line.LeftSource, line.RightSource, line.LeftLinks.Where(l => l.Unique == UniqueEnum.None).Count(), line.RightLinks.Where(l => l.Unique == UniqueEnum.None).Count(), string.Join(",", line.LeftLinks.Where(l => l.Unique == UniqueEnum.None).Select(l => l.Line)), string.Join(",", line.RightLinks.Where(l => l.Unique == UniqueEnum.None).Select(l => l.Line))));

                    break;
                }
            }
        }

        private void Process()
        {
            foreach (var node in dictL.Values)
                if (node.Links.Count == 1)
                {
                    node.Unique = true;
                    node.LineLinks[0].Unique |= UniqueEnum.Left;
                }

            foreach (var node in dictR.Values)
                if (node.Links.Count == 1)
                {
                    node.Unique = true;
                    node.LineLinks[0].Unique |= UniqueEnum.Right;
                }

            var uniques = lineDict.Values.Where(l => l.Unique == UniqueEnum.Both).ToArray();

            foreach (var uniq in uniques)
            {
                //lineDict.Remove(uniq.Line);
                dictL.Remove(uniq.Left);
                dictR.Remove(uniq.Right);
            }

            foreach (var lnode in lineDict.Values)
            {
                if (lnode.Unique == UniqueEnum.None) continue;

                if (lnode.Unique == UniqueEnum.Left)
                    foreach (var link in lnode.RightLinks)
                        if (link.Line != lnode.Line)
                        {
                            link.Unique |= UniqueEnum.DuplicateRight;
                            link.RightSource = lnode.Line;
                        }

                if (lnode.Unique == UniqueEnum.Right)
                    foreach (var link in lnode.LeftLinks)
                        if (link.Line != lnode.Line)
                        {
                            link.Unique |= UniqueEnum.DuplicateLeft;
                            link.LeftSource = lnode.Line;
                        }
            }
        }

        private void TraverseLeft(string p, Stack<string> stack)
        {
            var found = false;
            var left = dictL[p];
            foreach (var line in left.LineLinks)
                if (!line.Visited)
                {
                    found = true;
                    line.Visited = true;
                    line.Count++;
                    stack.Push(line.Line);
                    TraverseRight(line.Right, stack);
                    stack.Pop();
                    line.Visited = false;
                }

            if (!found)
                Console.WriteLine(String.Join("->", stack.Reverse()));
        }

        private void TraverseRight(string p, Stack<string> stack)
        {
            var found = false;
            var right = dictR[p];
            foreach (var line in right.LineLinks)
                if (!line.Visited)
                {
                    found = true;
                    line.Visited = true;
                    line.Count++;
                    stack.Push(line.Line);
                    TraverseLeft(line.Left, stack);
                    stack.Pop();
                    line.Visited = false;
                }

            if (!found)
                Console.WriteLine(String.Join("->", stack.Reverse()));
        }

        int duplicateCount = 0;
        private void Process(Dictionary<string, Node> dictL, Dictionary<string, Node> dictR)
        {
            foreach (var lnode in dictL.Values.OrderByDescending(n => n.Links.Count))
            {
                if (lnode.Links.Count < 2) continue;
                while (true)
                {
                    var links = lnode.Links.Select(rn => dictR[rn]).OrderByDescending(n => n.Links.Count).ToList();
                    Node duplicate = null;
                    foreach (var link in links)
                    {
                        if (link.Links.Count < 2) continue;
                        foreach (var lnode2 in link.Links.Select(l => dictL[l]).OrderByDescending(n => n.Links.Count))
                        {
                            if (lnode2.Links.Count < 2) continue;
                            foreach (var rnode in lnode2.Links.Select(l => dictR[l]).OrderByDescending(n => n.Links.Count))
                            {
                                if (rnode.Links.Count < 2) continue;
                                if (lnode2.Key != lnode.Key && link.Key != rnode.Key)
                                {
                                    duplicate = link;
                                    break;
                                }
                            }
                        }
                    }

                    if (duplicate != null)
                    {
                        lnode.Links.Remove(duplicate.Key);
                        duplicate.Links.Remove(lnode.Key);
                        duplicateCount++;
                    }
                    else break;
                }
            }
        }

        class Node
        {
            public string Key;
            public List<string> Links = new List<string>(), Lines = new List<string>();
            public bool Visited = false;
            public List<LineNode> LineLinks = new List<LineNode>();
            public bool Unique;
        }

        class LineNode
        {
            public string Line;
            public bool Visited;
            public int Count;
            public string Left, Right;
            public List<LineNode> LeftLinks = new List<LineNode>(), RightLinks = new List<LineNode>();

            public UniqueEnum Unique = UniqueEnum.None;
            public string RightSource;
            public string LeftSource;
        }

        [Flags]
        enum UniqueEnum
        {
            None = 0,
            Left = 2,
            Right = 1,
            Both = 3,
            DuplicateLeft = 4,
            DuplicateRight = 8,
            DuplicateBoth = 12
        }
    }
}
