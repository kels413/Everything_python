#include <stdio.h>
#include <string.h>



int main(void)
{

    int array[] = {1,2,3,4,5};
    
    int sum = 0;
    for (size_t i = 0; i < 5; i++)
    {
        /* code */


        printf("sum is %d\n", sum += array[i]);
    }
    

    return 0;
}