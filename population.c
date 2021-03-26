#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
int startsize;
    
do
{
    startsize = get_int("Choose starting populaiton, bigger than 9: ");
}
while (startsize<9);

int startSize = (float)startsize;

    // TODO: Prompt for end size
int endsize;


do
{
    endsize = get_int("Choose a final population size: ");
}
while (endsize < startSize)
;
int endSize = (float)endsize;

    // TODO: Calculate number of years until we reach threshold
    int i;
    int years = 0;
    
     if (startSize == endSize)
    {
        printf("Years: 0");
    }
    
 for(i = startSize; i<=endSize; i++){
     i = i + (i/3) - (i/4);
     years++;

 }
    // TODO: Print number of years
    printf("Years: %i\n ", years);
}