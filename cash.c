#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // get return to customer amount
    float get;
    do
    {
        get = get_float("How much change to give in dollars?: $");
    }
    while (get <= 0);
    //get to decimals then rounded
    int cents = round(get * 100);
    //print answer of amount into cents
    //printf ( "Total in cents: %i\n", cents);
    
    // initialise int variables
    int qcoin = 0;
    int dcoin = 0;
    int ncoin = 0;
    int pcoin = 0;
    
    // check for 25 coin
    do
    {
        if (cents < 25)
        {
            break;
        }
        else
        {
            cents = cents - 25;
            qcoin++;
        }
    }
    while (cents >= 25);
    
    // check for 10 coin
    do
    {
        if (cents < 10)
        {
            break;
        }
        else
        {
            cents = cents - 10;
            dcoin++;
        }
    }
    while (cents >= 10);
    
    // check for 5 coin
    do
    {
        if (cents < 5)
        {
            break;
        }
        else
        {
            cents = cents - 5;
            ncoin++;
        }
    }
    while (cents >= 5);
    
    //check for 1 coin
    do
    {
        if (cents < 1)
        {
            break;
        }
        else
        {
            cents = cents - 1;
            pcoin++;
        }
    }
    while (cents >= 1);
    
    // count total coins
    int totalCoins = qcoin + pcoin + ncoin + dcoin;
    
    
    // print amount of each coin.
    printf("Quarters: %i\n", qcoin);
    printf("Dimes: %i\n", dcoin);
    printf("Nickles: %i\n", ncoin);
    printf("Pennies: %i\n", pcoin);
    //print total coins.
    printf("Total coins: %i\n", totalCoins);
}
