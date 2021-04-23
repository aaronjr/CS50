#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int main(int argc, string argv[])
{
   if (argc != 2){printf("Insert valid key\n"); return 1;}
   for(int i = 0, n = strlen(argv[1]); i < n; i++)
   {
       if (isdigit(argv[1][i])){}
       else {printf("Usage: ./caesar key\n"); return 1; };
   };

   int key = atoi(argv[1]);
   //printf("%i\n", key);

    // get plain text
    string plain = get_string("plaintext: ");
    printf("Ciphertext: ");
    
    // convert to  ciphertext
    for (int i = 0, n = strlen(plain); i < n; i++){
      if (plain[i] >= 'a' && plain[i] <= 'z'){
         char c = plain[i] + key;
      printf("%c", c);}
      else if (plain[i] >= 'A' && plain[i] <= 'Z'){
         char c = plain[i] + key;
      printf("%c", c);}
      else if(plain[i] != (plain[i] >= 'a' && plain[i] <= 'z') || plain[i] != (plain[i] >= 'A' && plain[i] <= 'Z') ){
          printf("%c", plain[i]);
      }
      else if(i == strlen(plain) - 1){printf("\n");}
    }

}

