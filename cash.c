#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
// get return to customer amount
float get;
do{
    get = get_float("How much change to give in dollars?: $");
  }
while ( get <= 0 );
//get to decimals then rounded
int cents = round(get * 100);
//print answer of amount into cents
//printf ( "Total in cents: %i\n", cents);

int qcoin = 0;
int dcoin = 0;
int ncoin = 0;
int pcoin = 0;


do {
    if(cents < 25){break;}
    else{
    cents = cents - 25;
    qcoin++;}
      }
while (cents >= 25);

do {
    if(cents < 10){break;}
    else{
    cents = cents - 10;
    dcoin++;}
        }
while (cents >= 10);

do {
    if(cents < 5){break;}
    else{
    cents = cents - 5;
    ncoin++;}
    }
while ( cents >= 5);

do {
    if(cents < 1){break;}
    else{
    cents = cents - 1;
    pcoin++;}
    }
while ( cents >= 1);


int totalCoins = qcoin + pcoin + ncoin + dcoin;


// print amount of each coin.
printf ( "Quarters: %i\n", qcoin);
printf ( "Dimes: %i\n", dcoin);
printf ( "Nickles: %i\n", ncoin);
printf ( "Pennies: %i\n", pcoin);
//print remaining change.
printf ( "Total coins: %i\n", totalCoins);
}
