#Este programa recorre los números del 1 al 100. Muestra los números pares o divisibles entre 3.


using System;

namespace numeros
{
    class MainClass
    {
        public static void Main(string[] args)
        {

            for (int i = 1; i<=100 ;i++)
            {
                if (i%2==0 || i%3==0)
                {
                    Console.WriteLine(i);
                }

            }

            Console.ReadLine();
        }
    }
}
