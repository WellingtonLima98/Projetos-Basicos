#include <stdio.h>
#include <stdlib.h>

void OrdenaVetor(int vetor[30]) {
    int i, j, aux;

    for(i = 0; i < 29; i++) {
        for(j = 0; j < 30; j++) {
            if(vetor[i] >= vetor[j]) {
                aux = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = aux;
            }
        }
    }
}

int PesquisaBinaria(int vetor[30], int numeroPesquisar) {
    int comeco = 0, final = 29, media;

    OrdenaVetor(vetor);

    while(comeco <= final) {
        media = (comeco + final) / 2;

        if(numeroPesquisar == vetor[media]) {
            return media;
        } else if(numeroPesquisar < vetor[media]) {
            final = media - 1;
        } else {
            comeco = media + 1;
        }
    }
    return -1;
}

int main() {
    int vetor[30], i, numeroPesquisar, resposta;

    for(i = 0; i < 30; i++) {
        if(i % 2 == 0) {
            vetor[i] = (rand() % 50) * 2;
        } else {
            vetor[i] = (rand() % 50) * 5;
        }
    }

    printf("Digite o numero a ser pesquisado: ");
    scanf("%d", &numeroPesquisar);

    resposta = PesquisaBinaria(vetor, numeroPesquisar);

    if(resposta == -1) {
        printf("Não Encontrado.\n");
    } else {
        printf("Numero encontrado foi %d\n", resposta);
    }

    return 0;
}