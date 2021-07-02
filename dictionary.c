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
const unsigned int N = 256;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    bool rtrn = 0;
    int location = hash(word);
    node *cursor = malloc(sizeof(node));
    node *bucket = table[location];
    for(cursor = bucket; cursor == NULL; cursor = cursor->next)
    {
        if(strcasecmp(cursor->word, word)==0)
        {
            rtrn = true;
        }
    }
    
    return rtrn;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash = 5381;
    int c;
    
    // *str++ is going to the next address in memory, where the next char in the string is stored
    while ((c = *word++))        
    {
        if (isupper(c))
        {
            c = c + 32;
        }

        hash = ((hash << 5) + hash) + c; // hash * 33 + c   // hash << 5 = hash * 2^5
    }

    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    bool rtrn;
    // open file
    FILE *file = fopen(dictionary, "r");
    if(file == NULL)
    {
        fclose(file);
        rtrn = false;
    }
    //scan through each word, copy to a temp variable then use hash to give correct location
    char tmp[LENGTH + 1];
    while(fscanf(file, "%s", tmp) != EOF){
        node *n = malloc(sizeof(node));
        strcpy(n -> word, tmp);
        n -> next = NULL;
        int location = hash(tmp);
        counter++;
        //below could be wrong
        if(table[location]==NULL)
        {
            table[location] = n;
            rtrn = true;
        }
        else
        {
            n->next = table[location];
            table[location] = n;
            rtrn = true;
        }
        
        
    }
    // return bool value of rtrn
    return rtrn;
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
    // TODO
    return false;
}
