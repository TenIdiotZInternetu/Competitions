using System;
using System.Security.Cryptography;
using System.Text;

namespace skb
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] pochodujuci = new int[n];
            StringBuilder output = new StringBuilder();
            int curVeduci = 0;

            string[] input = Console.ReadLine().Split();

            for (int i = 0; i < n; i++)
            {
                pochodujuci[i] = Convert.ToInt32(input[i]);
            }

            for (int i = 0; i < n; i++)
            {
                if (pochodujuci[n - i - 1] > curVeduci)
                {
                    output.Append(n - i + " ");
                    curVeduci = pochodujuci[n - i - 1];
                }
            }

            Console.WriteLine(output.ToString().TrimEnd());
        }
    }
}
