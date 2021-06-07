#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            float average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;
            
            image[i][j].rgbtRed = round(.393 * r + .769 * g + .189 * b);
            if(image[i][j].rgbtRed > 255){
                image[i][j].rgbtRed = 255;
            }
            else if(image[i][j].rgbtRed < 0){
                image[i][j].rgbtRed = 0;
            }
            image[i][j].rgbtGreen = round(.349 * r + .686 * g + .168 * b);
            if(image[i][j].rgbtGreen > 255){
                image[i][j].rgbtGreen = 255;
            }
            else if(image[i][j].rgbtGreen < 0){
                image[i][j].rgbtGreen = 0;
            }
            image[i][j].rgbtBlue = round(.272 * r + .534 * g + .131 * b);
            if(image[i][j].rgbtBlue > 255){
                image[i][j].rgbtBlue = 255;
            }
            else if(image[i][j].rgbtBlue < 0){
                image[i][j].rgbtBlue = 0;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
