#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{

   char key[26] = "";
   
    // check 2 aruguments
   if (argc != 2){printf("Insert valid key\n"); return 1;}
   // check for 26 characters
   if(strlen(argv[1])!=26){printf("Insert 26 characters\n"); return 1;}
   // check for alphabeetical characters
   for(int i = 0, n = strlen(argv[1]); i < n; i++){
    if (argv[1][i] >= 'a' && argv[1][i] <= 'z'){
         strncat(key, &argv[1][i], 1);
       }
    else if(argv[1][i] >= 'A' && argv[1][i] <= 'Z'){
         char q = (argv[1][i] + 32);
         strncat(key, &q , 1);
      }
    
   else {printf("Insert 26 alphabetical characters\n"); return 1;}
   }

   //test for key
   printf("The key is %s\n", key);

    // get plain text
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");

    // to cipher - CURRENT ISSUE MATH PROBS NOT CORRECT
    for (int i = 0, n = strlen(plain); i < n; i++){
      if (plain[i] >= 'a' && plain[i] <= 'z'){
        //printf("%c", ((plain[i] - 'a') + (key[plain[i] - 'a']) % 26) + 'a');
        printf("%c", (plain[i] - 'a') + (key[plain[i] - 'a'] - 'a') % 26 + 'a' );
        }
      else if (plain[i] >= 'A' && plain[i] <= 'Z'){
        printf("%c", (plain[i] - 'A') + (key[plain[i] - 'a'] - 'a') % 26 + 'A' );
        }
      else {printf("%c", plain[i]);}
    }

    //print new line
    printf("\n");
    //return 0
    return 0;
}



