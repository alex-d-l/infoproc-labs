#include <stdio.h>
#include <string.h>
#define CHARLIM 256    // Maximum character length of what the user places in memory.  Increase to allow longer sequences
#define QUITLETTER '~' // Letter to kill all processing

void print_text(char *text, const int length)
{
    char *printMsg;
    asprintf(&printMsg, "<--> Detected %d characters: %s <--> \n %c", length, text, 0x4); // Print out the strings
    alt_putstr(printMsg);
    free(printMsg);
    memset(text, 0, 2 * CHARLIM); // Empty the text buffer for next input
}


int read_chars()
{
    char text[2 * CHARLIM]; // The buffer for the printing text
    char prevLetter = '!';
    int length = 0;
    int running = 1;

    while (running)
    {                                                                    // Keep running until QUITLETTER is encountered
        prevLetter = alt_getchar();                                      // Extract the first character (and create a hold until one arrives)
        prevLetter = generate_text(prevLetter, &length, text, &running); // Process input text
        print_text(text, length);                                        // Print input text
    }

    return 0;
}

int main()
{
    return read_chars();
}
