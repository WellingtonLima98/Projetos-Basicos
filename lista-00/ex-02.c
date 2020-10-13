#include <stdio.h>
#include <stdlib.h>

int main() {
    int matrizA[5][3] = {{1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}, {13,14,15}};
    int matrizB[5][3] = {{16,17,18}, {19,20,21}, {22,23,24}, {25,26,27}, {28,29,30}};
    int matrizC[2][15];
    int i, j;
    int aux = 0;
    
    // ========== Insere os elementos da Matriz A e B na Matriz C ==========
    for(i = 0; i < 5; i++) {
        for(j = 0; j < 3; j++) {
            matrizC[0][aux] = matrizA[i][j];
            matrizC[1][aux] = matrizB[i][j];
            aux++;
        }
    }

    // ===================== Mostra a Matriz C na tela =====================
    for(i = 0; i < 2; i++) {
        for(j = 0; j < 15; j++) {
            printf("%d\n", matrizC[i][j]);
        }
    }

    return 0;
}