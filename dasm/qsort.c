#include <stdio.h>
#include <stdlib.h>

int partition(int* data, int low, int high)
{
    int pivot = data[high];
    int i = low - 1;
    int tmp;
    for (int j = low; j < high; j++)
    {
        if (data[j] <= pivot)
        {
            i++;
            tmp = data[i];
            data[i] = data[j];
            data[j] = tmp;
        }
    }

    tmp = data[i + 1];
    data[i + 1] = data[high];
    data[high] = tmp;

    return i + 1;
}


int partition2(int* data, int low, int high)
{
    int pivot = data[high];
    int i = low - 1;
    int tmp;
    int j = low;

swap_loop:
    if (j >= high)
        goto swap_loop_finish;

    if (data[j] > pivot)
        goto swap_loop_next;

    i++;
    tmp = data[i];
    data[i] = data[j];
    data[j] = tmp;

swap_loop_next:
    j++;
    goto swap_loop;

swap_loop_finish:
    tmp = data[i + 1];
    data[i + 1] = data[high];
    data[high] = tmp;

    return i + 1;
}

void quicksort(int* data, int low, int high)
{
    if (low >= high)
        return;
    int pivotIndex = partition2(data, low, high);
    quicksort(data, low, pivotIndex - 1);
    quicksort(data, pivotIndex + 1, high);
}


int main()
{
    int N = 100;
    int data[100];
    for (int i = 0; i < N; ++i)
    {
        data[i] = rand();
    }

    quicksort(data, 0, N - 1);

    for (int i = 0; i < N; ++i)
    {
        printf("%d ", data[i]);
    }

    printf("\n");
}
