#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
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
            
            float r = image[i][j].rgbtRed;
            float g = image[i][j].rgbtGreen;
            float b = image[i][j].rgbtBlue;
            
            image[i][j].rgbtRed = round(0.393 * r + 0.769 * g + 0.189 * b);
            if(image[i][j].rgbtRed > 255){
                image[i][j].rgbtRed = 255;
            }
            else if(image[i][j].rgbtRed < 0){
                image[i][j].rgbtRed = 0;
            }
            image[i][j].rgbtGreen = round(0.349 * r + 0.686 * g + 0.168 * b);
            if(image[i][j].rgbtGreen > 255){
                image[i][j].rgbtGreen = 255;
            }
            else if(image[i][j].rgbtGreen < 0){
                image[i][j].rgbtGreen = 0;
            }
            image[i][j].rgbtBlue = round(0.272 * r + 0.534 * g + 0.131 * b);
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
