#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int main(int argc, string argv[])
{
    // check 2 aruguments
   if (argc != 2){printf("Insert valid key\n"); return 1;}
   for(int i = 0, n = strlen(argv[1]); i < n; i++)
   {
       if (isdigit(argv[1][i])){}
       else {printf("Usage: ./caesar key\n"); return 1; };
   };
    
    //hold string as int
    //printf("%i\n", key);
   int key = atoi(argv[1]);
   

    // get plain text
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");
    
    // convert to  ciphertext
    for (int i = 0, n = strlen(plain); i < n; i++){
      if (plain[i] >= 'a' && plain[i] <= 'z'){
         char c = (((plain[i] - 'a') + key) % 26) + 'a';
      printf("%c", c);}
      else if (plain[i] >= 'A' && plain[i] <= 'Z'){
         char c = (((plain[i] - 'A') + key) % 26) + 'A';
      printf("%c", c);}
      else {printf("%c", plain[i]);}
     }
    
    //print new line
    printf("\n");
    //return 0
    return 0;
}