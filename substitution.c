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
            for(int j = 0, k = strlen(key); j < k; j++){
                if (argv[1][i] == key[j]){
                    printf("No duplicate characters.");
                    
            }
         else {strncat(key, &argv[1][i], 1);}
            }
        }
        else if(argv[1][i] >= 'A' && argv[1][i] <= 'Z'){
                for(int e = 0, r = strlen(key); e < r; e++){
                    if (argv[1][i] == key[e]){
                        printf("No duplicate characters.");
                        
                    }
                
            else {char q = (argv[1][i] + 32);strncat(key, &q , 1);}
                }
            }
       else {printf("Insert 26 alphabetical characters\n"); return 1;}
   }

   //test for key
   printf("The key is %s\n", key);

    // get plain text
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");

    // to cipher 
    for(int p = 0, q = strlen(plain); p < q; p++){
      if (plain[p] >= 'a' && plain[p] <= 'z'){
        printf("%c", key[plain[p] - 'a']);
        }
      else if (plain[p] >= 'A' && plain[p] <= 'Z'){
        printf("%c", key[plain[p] - 'A'] - 32);
        }
      else { printf("%c", plain[p]);}
    }
    
    //print new line
    printf("\n");
    //return 0
    return 0;
}



