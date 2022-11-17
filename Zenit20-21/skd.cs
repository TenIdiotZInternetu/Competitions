using System;
using System.Globalization;
using System.Runtime.InteropServices;
using System.Security.Cryptography;

namespace skd
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] inputs = new string[n];
            (int x, int y) position;
            bool canReach = true;

            for (int i = 0; i < n; i++)
            {
                inputs[i] = Console.ReadLine();
            }

            (int x, int y)[] positions = new (int, int)[9];
            int digit = 0;

            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    positions[digit] = (i, j);
                    digit++;
                }
            }

            for (int i = 0; i < n; i++)
            {
                int[] instruction = new int[inputs[i].Length];

                for (int j = 0; j < inputs[i].Length; j++)
                {
                    instruction[j] = int.Parse((inputs[i][j]).ToString());
                }

                position = positions[instruction[0] - 1];
                canReach = true;

                for (int j = 1; j < instruction.Length; j++)
                {
                    canReach = TryReach(position, positions[instruction[j] - 1]);
                    //Console.WriteLine(canReach);

                    if (canReach)
                    {
                        position = positions[instruction[j] - 1];
                    }
                    else
                    {
                        break;
                    }
                }

                if (canReach)
                {
                    Console.WriteLine("hijo, do toho!");
                }
                else
                {
                    Console.WriteLine("brrrr Konik, to nedavas...");
                }
            }
        }

        static bool TryReach((int x, int y) curPos, (int x, int y) newPos)
        {
            //Console.WriteLine(curPos);
            //Console.WriteLine(newPos);

            if ((curPos.Item1 == newPos.Item1 - 1 && curPos.Item2 == newPos.Item2 - 2) ||
                (curPos.Item1 == newPos.Item1 - 1 && curPos.Item2 == newPos.Item2 + 2) ||
                (curPos.Item1 == newPos.Item1 + 1 && curPos.Item2 == newPos.Item2 - 2) ||
                (curPos.Item1 == newPos.Item1 + 1 && curPos.Item2 == newPos.Item2 + 2) ||
                (curPos.Item1 == newPos.Item1 - 2 && curPos.Item2 == newPos.Item2 - 1) ||
                (curPos.Item1 == newPos.Item1 - 2 && curPos.Item2 == newPos.Item2 + 1) ||
                (curPos.Item1 == newPos.Item1 + 2 && curPos.Item2 == newPos.Item2 - 1) ||
                (curPos.Item1 == newPos.Item1 + 2 && curPos.Item2 == newPos.Item2 + 1))
            {
                return true;
            }

            return false;
        }
    }
}
