#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through rows
    for (int i = 0; i < height; i++)
    {
        //loop through columns
        for (int j = 0; j < width; j++)
        {
            // add all together and dived by 3
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            //assign the average
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
    //loop through rows
    for (int i = 0; i < height; i++)
    {
        //loop through columes
        for (int j = 0; j < width; j++)
        {
            //give value to int
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;
            
            //sepia algorithm
            int red = round(0.393 * r + 0.769 * g + 0.189 * b);
            int green = round(0.349 * r + 0.686 * g + 0.168 * b);
            int blue = round(0.272 * r + 0.534 * g + 0.131 * b);
            
            //create a cap
            if (red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else if (red < 0)
            {
                image[i][j].rgbtRed = 0;
            }
            else
            {
                image[i][j].rgbtRed = red;
            }
            
            if (green > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else if (red < 0)
            {
                image[i][j].rgbtGreen = 0;
            }
            else
            {
                image[i][j].rgbtGreen = green;
            }
        
            if (blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else if (red < 0)
            {
                image[i][j].rgbtBlue = 0;
            }
            else
            {
                image[i][j].rgbtBlue = blue;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through rows
    for (int i = 0; i < height; i++)
    {
        //loop through columns
        for (int j = 0; j < width / 2; j++)
        {
            //use place holder and switch around
            RGBTRIPLE buffer = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = buffer;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //variable to hold copy of height and width
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //initialise variables
            temp[i][j] = image[i][j];
            float counter = 0.0;
            int averageRed = 0;
            int averageGreen = 0;
            int averageBlue = 0;
            
            // check to make sure i + j of arrayare valid
            for (int h = -1; h < 2; h++)
            {
                for (int w = -1; w < 2; w++)
                {
                    if (i + h < 0 || i + h > (height - 1))
                    {
                        continue;
                    }
                    if (j + w < 0 || j + w > (width - 1))
                    {
                        continue;
                    }
                    else
                    {
                        counter++;
                        averageBlue += image[i + h][j + w].rgbtBlue;
                        averageGreen += image[i + h][j + w].rgbtGreen;
                        averageRed += image[i + h][j + w].rgbtRed;
                    }
                }
            }
            // copy attributes to temp array
            temp[i][j].rgbtBlue = round(averageBlue / counter);
            temp[i][j].rgbtGreen = round(averageGreen / counter);
            temp[i][j].rgbtRed = round(averageRed / counter);
            
        }
    }
    // copt exact details from temp to actualto then export
    for (int q = 0; q < height; q++)
    {
        for (int w = 0; w < width; w++)
        {
            image[q][w].rgbtRed = temp[q][w].rgbtRed;
            image[q][w].rgbtBlue = temp[q][w].rgbtBlue;
            image[q][w].rgbtGreen = temp[q][w].rgbtGreen;
        }
    }
    
    return;
}

