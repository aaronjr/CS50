#include <cs50.h>
#include <stdio.h>


int main(void)
{
    //get input
    int input;
    
    do
    {
        input = get_int("height of tower: ");
    }
    while (input > 8 || input < 1);
    
    // work out
    for (int i = 0; i < input; i++)
    {
        for (int j = input - 1; j > i; j--)
        {
            // print empty space
            printf(" ");
        }
        for (int h = -1; h < i; h++)
        {
            // print hash
            printf("#");
        }
        printf("  ");
        for (int k = i - 1; k > i; k--)
        {
            // print empty space
            printf(" ");
        }
        for (int l = -1; l < i; l++)
        {   
            // print another hash
            printf("#");
        }
        printf("\n");
    }

}