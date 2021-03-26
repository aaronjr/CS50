#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
int startSize;
do
{
    startSize = get_int("Choose starting populaiton, bigger than 9: ");
}
while (startSize<9);

    // TODO: Prompt for end size
int endSize;
{
    endSize=get_int("Choose a final population size: ");
}
while (endSize < startSize)
;
    // TODO: Calculate number of years until we reach threshold
    int i;
    int years = 0;
 for(i = startSize; i<=endSize; i++){
     i = i + ((float)i/3) - ((float)i/4);
     years++;

 }
    // TODO: Print number of years
    printf("Years: %i\n ", years);
}