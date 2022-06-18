/* Crie um vetor com ponteiros utilizando aloca��o din�mica na linguagem C, que:

- use a fun��o realloc;
- use a fun��o sizeof;
- que tenha tamanho 22 de vetor;
- depois libere o bloco utilizando a fun��o free.
*/

#include <stdio.h>
#include <stdlib.h>
#define TAM  22
 
//Aloca um vetor do tamanho pedido
int* alocaVetor (int tam){
 
    //� criado um ponteiro
    int *v;
 
    //A mem�ria � alocada e o ponteiro recebe o endere�o de mem�ria dele
    v = (int *) malloc ( tam * sizeof (int) ) ;
 
    //Esse ponteiro � retornado
    return v;
}

 
int main(){
 
    //Ponteiro que vai apontar para o vetor criado
    int *vetor;
 
    vetor = alocaVetor(TAM) ;
 
 
    //Preenchendo e Imprimindo o vetor na tela
    for(int i=0;i<TAM;i++){
		vetor[i]= i+1;
        printf("%d ", vetor[i]);
    }
    printf("\n");
    // mudando o tamnho do vetro usando realloc
    
    vetor = (int *) realloc(vetor, 10 * sizeof (int)); 
        
    //Preenchendo e Imprimindo o novo vetor na tela
    for(int i=0;i<10;i++){
		vetor[i]= i+1;
        printf("%d ", vetor[i]);
    }
 
    //Libera a mem�ria ap�s usar o vetor
    free ( vetor ) ;
 
    return 0;
}
