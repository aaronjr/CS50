#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

string winner(int a, int b);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");


    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    string champion = winner(score1, score2);

    // Print the winner
    printf("score 1 is: %i\n", score1);
    printf("score 2 is: %i\n", score2);
    printf("The winner is: %s\n", champion);
}

//compare scores & return winner
string winner(int a, int b)
{
    // check is a bigger than b then which player won
    if (a > b)
    {
        return "player 1 wins";
    }
    else if (a <  b)
    {
        return "player 2 wins";
    }
    else 
    {
        return "Tie";
    }
}

// compute the score
int compute_score(string word)
{
    int score = 0;

    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // check for capital and use ascii
        if (word[i] >= 'A' && word[i] <= 'Z')
        {
            score += POINTS[word[i] - 65];
        }
        // check for small letter and use ascii
        else if (word[i] >= 'a' && word[i] <= 'z')
        {
            score += POINTS[word[i] - 97];
        }
        
    }
    return score;   
}

