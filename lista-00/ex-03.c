#include <stdio.h>
#include <stdlib.h>

int main() {
    int numeroRecebido;
    int vetorAntessessor[2];
    int vetorSucessor[2];
    int i, numeroRecebidoAux;

    // Recebe um número do usuário
    printf("Informe um numero inteiro: ");
    scanf("%d", &numeroRecebido);

    // Insere os Antecessores e os Sucessores do número recebido nos vetores correspondentes
    numeroRecebidoAux = numeroRecebido;

    for(i = 0; i < 2; i++) {
        vetorAntessessor[i] = --numeroRecebido;
        vetorSucessor[i] = ++numeroRecebidoAux;
    }

    // Mostra os Antecessores e os Sucessores na tela
    printf("Os Antessessores são: %d e %d\n", vetorAntessessor[0], vetorAntessessor[1]);
    printf("Os Sucessores são: %d e %d\n", vetorSucessor[0], vetorSucessor[1]);

    return 0;
}