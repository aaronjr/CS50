#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // TODO: Prompt for start size
int startSize;
do
{
    startSize = get_int("Choose starting populaiton, 9 or bigger: ");
}
while (startSize<9);

    // TODO: Prompt for end size
int endSize;
do
{
    endSize = get_int("Choose a final population size: ");
}
while (endSize < startSize)
;
// TODO: Calculate number of years until we reach threshold
int years = 0;


while (startSize<endSize)
    {
     startSize = startSize + (startSize / 3) - (startSize / 4);
     years++;
    }

 if (startSize == endSize)
    {
        printf("Years: 0");
    }
 else
    {
    // TODO: Print number of years
    printf("Years: %i\n ", years);
    }
}