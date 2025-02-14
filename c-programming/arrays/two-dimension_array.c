#include <stdio.h>

#define ROWS 3
#define COLS 8

int main()
{
    int array[ROWS][COLS];

    // Reading elements
    printf("Enter elements of the array:\n");
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &array[i][j]);
        }
    }

    // Writing elements
    printf("\nThe array elements are:\n");
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }

    return (0);
}