#include <stdio.h>
#include <stdlib.h>

int main() {
    int matrizA[5][4];
    int matrizB[4][3];
    int matrizC[5][3];
    int i, j, x, aux = 0, numeroRecebido;

    // =============== Recebe os números que preenchem as matrizes A e B ===============
    printf("Informe os numeros da matriz:\n");

    for(i = 0; i < 5; i++) {
        for(j = 0; j < 4; j++) {
            printf("MatrizA[%d][%d] =  ", i, j);
            scanf("%d", &numeroRecebido);
            matrizA[i][j] = numeroRecebido;
        }
    }

    for(i = 0; i < 4; i++) {
        for(j = 0; j < 3; j++) {
            printf("MatrizB[%d][%d] =  ", i, j);
            scanf("%d", &numeroRecebido);
            matrizB[i][j] = numeroRecebido;
        }
    }

    // ======================== Mostra na tela as Matrizes A e B =======================
    printf("===============MatrizA===============\n");

    for(i = 0; i < 5; i++) {
        for(j = 0; j < 4; j++) {
            printf("%d ", matrizA[i][j]);
            if(j == 3) {
                printf("\n");
            }
        }
    }

    printf("\n=====================================\n");

    printf("===============MatrizB===============\n");


    for(i = 0; i < 4; i++) {
        for(j = 0; j < 3; j++) {
            printf("%d ", matrizB[i][j]);
            if(j == 2) {
                printf("\n");
            }
        }
    }

    printf("\n=====================================\n");

    // ======= Calcula a multiplicação das Matrizes A e B, e insere na Matriz C ========
    for(i = 0; i < 5; i++) {
		for(j = 0; j < 4; j++) {
			
			matrizC[i][j] = 0;
			for(x = 0; x < 4; x++) {
				aux +=  matrizA[i][x] * matrizB[x][j];
			}

			matrizC[i][j] = aux;
			aux = 0;
		}
	}

    // =========================== Mostra na tela a Matriz C ===========================
    printf("===============MatrizC===============\n");


    for(i = 0; i < 5; i++) {
        for(j = 0; j < 3; j++) {
            printf("%d ", matrizC[i][j]);
            if(j == 2) {
                printf("\n");
            }
        }
    }

    printf("\n=====================================\n");

    

    return 0;
}