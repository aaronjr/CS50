#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }
    
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Invalid file\n");
        return 1;
    }
    
    //Declare buffer
    BYTE buffer[512];
    //keep track of current JPEGS found
    int counter = 0;
    //make new file to copy into
    FILE *output = NULL;
    char filename[8];
   
    
    //loop through file - 512 bytes at a time store in buffer
    while (fread(buffer, sizeof(char), 512, file) != 0)
    {
        //check first 4 bytes
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) 
        {
            //make name
            sprintf(filename, "%03i.jpg", counter);
            //open to write
            output = fopen(filename, "w");
            //write to file
            fwrite(buffer, sizeof(buffer), 1, output);
            //counter++
            counter++;
        }
           
        else if (output != NULL)
        {
            fwrite(buffer, sizeof(buffer), 1, output);
        }
    }
    
      

 
    fclose(file, output);
 
    return 0;
}