#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
   if (argc != 2){printf("Insert valid key\n"); return 1;}
   for(int i = 0, n = strlen(argv[1]); i < n; i++)
   {
       if (isdigit(argv[1][i])){return 0; printf("is digit\n");}
       else {return 1; printf("Usage: ./caesar key\n");};
   };
   
 string plaintext = get_string("plaintext: ");
 // output ciphertext 
}