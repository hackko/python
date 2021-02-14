#include <iostream>

#include <stdlib.h>

using namespace std;

int main() {

  int N, menor, numero;

  cout<<"Escoge entre 2 a 5 digitos ?: ";

  cin>>N;



  for(int i = 0; i < N; i++)

  {

    cout<<"Ingrese un numero: ";

    cin>>numero;

    if ( i == 0 )

    {

      menor = numero;

    }else if ( numero < menor )

      {

        menor = numero;

      }

  }

  cout<<"\nEl menor ingresado es: "<<menor<<endl;

  return 0;

}
