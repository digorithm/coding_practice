#include <stdio.h>
#include <stdlib.h>


int main(){
        int i = 0;
        int num = scanf("%d", &num);
        while (num != 42){
                printf("%d\n", num);
                scanf("%d", &num);
        }
        return 0;
}
