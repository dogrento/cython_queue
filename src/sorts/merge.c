#include <stdio.h>
#include <stdlib.h>
#include "merge.h"

void merge(int arr[], int left, int mid, int right){
  int i, j, k;
  int n1 = mid - left + 1;
  int n2 = right - mid;

  // temp arrays
  int l_arr[n1], r_arr[n2];

  //cp data to temp arrays
  for(i = 0; i < n1; i++)
    l_arr[i] = arr[left + i];
  for(j = 0; j < n2; j++)
    r_arr[i] = arr[mid + 1 + j];

  // merge the temp arrays back into arr[l...r]
  i = 0;
  j = 0;
  k = l;
  while(i < n1 && j < n2){
    if(l_arr[i] < = r_arr[j]){
      arr[k] = l_arr[i];
      i++;
    }
    else{
      arr[k] = r_arr[j];
      j++;
    }
    k++;
  }

  // cp the remaining elements of r_arr[]/l_arr[],
  // if there are any
  while(i < n1){
    arr[k] = l_arr[i];
    i++;
    k++;
  }
  while(j < n2){
    arr[k] = r_arr[j];
    j++;
    k++;
  }
}

void c_mergeSort(int arr[], int left, int right){
  if(left < right){
    int mid = left + (right - left) / 2;
    
    c_mergeSort(arr, left, mid);
    c_mergeSort(arr, mid + 1, right);

    merge(arr, left, right);
  }
}
