#include <stdio.h>
#include <stdlib.h>

// ==================== Faz a pesquisa do número dado ====================
int PesquisaPorNumero(int numeroPesquisar, int vetorC[50]) {
    int i;

    for(i = 0; i < 50; i++) {
        if(numeroPesquisar == vetorC[i]) {
            return i;
        }
    }
    return -1;
}

int main() {
    int vetorA[25], vetorB[25], vetorC[50], i, numeroPesquisar, resposta;

// ==================== Preenche os vetores A, B e C =====================
    for(i = 0; i < 25; i++) {
        vetorA[i] = (rand() % 100);
        vetorB[i] = (rand() % 100);
        vetorC[i] = vetorA[i];
        vetorC[i + 25] = vetorB[i];
    }
// ===================== Recebe o numero do Usuário ======================
    printf("Digite o numero que voce quer pesquisar: ");
    scanf("%d", &numeroPesquisar);

// ================= Chama a Função PesquisarPorNumero ===================
    resposta = PesquisaPorNumero(numeroPesquisar, vetorC);

    if(resposta == -1) {
            printf("Nao encontrato.\n\n");
    } else {
        printf("O numero existe e esta no indice -> %d\n\n", resposta);
    }

// ====================== Printa na tela o vetorC ========================
    for(i = 0; i < 50; i++) {
        if(i == 49) {
                printf("%d\n", vetorC[i]);
        } else {
            printf("%d ", vetorC[i]);
        }
    }

    return 0;
}