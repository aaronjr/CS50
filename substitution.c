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
   
   
   // check for alphabetical characters & dupllicates and add to key
   for(int i = 0, n = strlen(argv[1]); i < n; i++){
    if (argv[1][i] >= 'a' && argv[1][i] <= 'z'){
        char c = argv[1][i];
        for(int j = 0, k = strlen(argv[1]); j<k; j++){
            if(c == argv[1][j]){
                printf("No duplicate characters\n");
                return 1;
            }
            else{strncat(key, &argv[1][i], 1);} }
       }
    else if(argv[1][i] >= 'A' && argv[1][i] <= 'Z'){
         char e = argv[1][i];
         for(int j = 0, k = strlen(argv[1]); j<k; j++){
            if(e == argv[1][j]){
                printf("No duplicate characters\n");
                return 1;
            }
            else{char q = (argv[1][i] + 32);
                 strncat(key, &q , 1);} }
         
      }
    
   else {printf("Insert 26 alphabetical characters\n"); return 1;}
   }

   //test for key
   //printf("The key is %s\n", key);

    // get plain text
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");

    // to cipher - CURRENT ISSUE MATH PROBS NOT CORRECT
    for ( int p = 0, q = strlen(plain); p < q; p++){
      if (plain[p] >= 'a' && plain[p] <= 'z'){
        printf("%c", key[plain[p] - 'a']);
        }
      else if (plain[p] >= 'A' && plain[p] <= 'Z'){
        printf("%c", (key[plain[p] - 'A'] - 32));
        }
      else {printf("%c", plain[p]);}
    }

    //print new line
    printf("\n");
    //return 0
    return 0;
}



