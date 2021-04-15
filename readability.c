#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// functions for each type
float letters (string input);
float words (string input);
float sentences (string input);

int main(void){

//get input
string input = get_string("Text: ");

//calculate each type
float letter = letters(input);
float word = words(input);
float sentence = sentences(input);

//printf("Letters: %f\nWords: %f\nSentences: %f\n", letter, word, sentence);

//calculation for coleman liau
float l = (letter / word) * 100;
float s = (sentence / word) * 100;
int index = 0.0588 * l - 0.296 * s - 15.8;

printf("Grade %i\n", index);

}

float letters (string input){
    int letter = 0;
    for (int i = 0, n=strlen(input); i < n; i++){
        if ((input[i] >= 'A' && input[i] <= 'Z') || (input[i] >= 'a' && input[i] <= 'z' )){
             letter++;}
    }
    return letter;
}

float words (string input){
    int word = 0;
    for (int i = 0, n=strlen(input); i < n; i++){
         if (input[i] == 32){
            word++;}
    }
    return word+=1;
}

float sentences (string input){
    int sentence = 0;
    for (int i = 0, n=strlen(input); i < n; i++){
         if ( input[i] == 46 || input[i] == 33 || input[i] == 63 ){
            sentence ++;}
    }
    return sentence;
    }