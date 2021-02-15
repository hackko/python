/* Este programa te pide la cantidad de digitos que deseas comparar y al final te entrega el numero menor de todos los digitos introducidos  */


#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main() {

  int N ;


  cout<<"Escoge entre 2 a 5 digitos ?: ";

  cin>>N;
  int numero ;
  int menor ;
  int num [N];



  for(int i = 0; i < N; i++)

  {

    cout<<"Ingrese un numero : " ;

    cin>>numero;
    num[i] = numero;

    if ( i == 0 )

    {

      menor  = numero  ;

    }else if ( numero   < menor  )

      {

        menor  = numero  ;

      }


  }

cout<<"\nLos numeros ingresados son : "<<endl;
for (int j = 0 ; j < N; j++){
        cout<< num [j]<<endl;

}
  cout<<"\nEl menor ingresado es: "<< menor  <<endl;



  ofstream file;
  file.open ("resultC.txt");
  if (file.is_open())
  {
      file<<"\nLos numeros ingresados son : "<<endl;
       for (int j = 0 ; j < N; j++){
        file<< num [j]<<endl;

}

  file << "\nEl menor ingresado es: "<<menor;
  file.close();
  }
  else cout << "No se puede abrir el archivo";


  return 0;

}
