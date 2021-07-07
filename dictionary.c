// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

//counter
int counter = 0;
// Number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    char tmp[LENGTH + 1];
    for (int i = 0; i <= strlen(word); i++)
    {
        tmp[i] = tolower(word[i]);
    }
    
    node *cursor = table[hash(tmp)];
    while(cursor != NULL)
    {
        if(strcasecmp(word, cursor->word)==0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    
    return false;
}

/**
*Returnes hash value.
* this hash function was found on the internet but there was no author mentioned
*/
unsigned int hash(const char *word)
{
   unsigned int hash = 0;
    for (int i=0; word[i]!= '\0'; i++)
    {
        hash = 31*hash + word[i];
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open file
    FILE *file = fopen(dictionary, "r");
    if(file == NULL)
    {
        fclose(file);
        printf("Could not open file\n");
        return false;
    }
    //scan through each word, copy to a temp variable then use hash to give correct location
    char tmp[LENGTH + 1];
    int location = 0;
    while(fscanf(file, "%s", tmp) != EOF){
        
        location = hash(tmp);
        
        node *n = malloc(sizeof(struct node));
        if(n == NULL)
        {
            return false;
        }
        strcpy(n -> word, tmp);
        
        n -> next = table[location];
        table[location] = n;
        counter++;
    
    }
    // return bool value of rtrn, close file
    fclose(file);
    return true;
}

// Returns counter - if dictionary did not load it will return 0
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i=0; i<N; i++)
    {
        node *cursor=table[i];
        
        while(cursor != NULL)
        {
            node *tmp = cursor;
            cursor=cursor->next;
            free(tmp);
        }
    }
    return true;
}
