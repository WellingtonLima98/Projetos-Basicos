#include <stdio.h>
#include <stdlib.h>

void main() {
    int vetorA[5] = {1,2,3,4,5};
    int vetorB[5] = {6,7,8,9,10};
    int vetorC[10];
    int i, n;

    // ========== Insere os números dos vetores A e B no vetor C ==========
    for(i = 0; i < 5; i++) {
        vetorC[i] = vetorA[i];
        vetorC[i + 5] = vetorB[i];
    }

    // ===================== Mostra o vetor C na tela =====================
    for(n = 0; n < 10; n++) {
        printf("%d\n", vetorC[n]);
    }

}
