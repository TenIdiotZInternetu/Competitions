using System;
using System.Diagnostics.CodeAnalysis;
using System.Runtime.ConstrainedExecution;

namespace ske
{
    class Program
    {
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            int[] finalArray = new int[t];

            for (int c = 0; c < t; c++)
            {
                int n = int.Parse(Console.ReadLine());
                string[] interInput = Console.ReadLine().Split();
                int[] input = new int[n];
                int[] checkSum = new int[n - 1];
                

                for (int i = 0; i < n; i++)
                {
                    input[i] = int.Parse(interInput[i]);
                }

                int sum = input[0];

                for (int i = 0; i < n - 1; i++)
                {
                    sum += input[i + 1];
                    checkSum[i] = sum;
                }

                sum = 0;

                for (int i = 0; i < checkSum.Length; i++)
                {
                    sum += checkSum[i];
                }

                finalArray[c] = sum;
            }

            foreach (int result in finalArray)
            {
                Console.WriteLine(result);
            }
        }
    }
}
