#include <stddef.h>

int maxSequence(const int* array, size_t n) {
    int max_so_far = 0, max_ending_here = 0; 
   for (size_t i = 0; i < n; i++) { 
       max_ending_here = max_ending_here + array[i]; 
       if (max_ending_here < 0) 
           max_ending_here = 0;   
       else if (max_so_far < max_ending_here) 
           max_so_far = max_ending_here; 
   } 
   return max_so_far;    
}
