The Standard Template Library has more than 100 algorithms for searching, counting, and manipulating ranges and their elements. With C++17, 69 of them are overloaded and 8 new ones are added. The overloaded and new algorithms can be invoked with a so-called execution policy.

### Execution Policies

The policy tag specifies whether a program should run sequentially, in parallel, or in parallel with vectorization.

* `std::parallel::seq:` runs the program sequentially

* `std::parallel::par:` runs the program in parallel on multiple threads

* `std::parallel::par_unseq:` runs the program in parallel on multiple threads and allows the interleaving of individual loops; this permits a vectorized version with SIMD (Single Instruction Multiple Data) extensions.

```c++
vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9};

// standard sequential sort
std::sort(v.begin(), v.end());

// sequential execution
std::sort(std::parallel::seq, v.begin(), v.end());

// permitting parallel execution
std::sort(std::parallel::par, v.begin(), v.end());

// permitting parallel and vectorised execution
std::sort(std::parallel::par_unseq, v.begin(), v.end());
```

# Parallel & Vectorized Execution

### Parallel & Vectorized Execution

Whether an algorithm runs in a parallel and vectorized way depends on many factors. For example, it depends on whether the CPU and the operating system support SIMD instructions. Additionally, it also depends on the compiler and​ the optimization level that you used to translate your code.

```c++
const int SIZE= 8;

int vec[] = {1, 2, 3, 4, 5, 6, 7, 8};
int res[] = {0, 0, 0, 0, 0, 0, 0, 0};
int main(){
   for (int i= 0; i < SIZE; ++i) {
     res[i]= vec[i]+5;
   }
}
```

# Algorithms

Here are the 69 algorithms with parallelised versions.



|                          |                    |             |             |
| :----------------------- | ------------------ | ----------- | ----------: |  
| std::adjacent_difference | std::adjacent_find | std::all_of |	std::any_of |
| std::copy	                    |std::copy_if	        |std::copy_n	                    | std::count |
| std::count_if	                |std::equal	            |std::fill	                    | std::fill_n |
| std::find	                    |std::find_end	        |std::find_first_of	            | std::find_if |
| std::find_if_not	            |std::generate	        |std::generate_n	                | std::includes |
| std::inner_product	            |std::inplace_merge	    |std::is_heap	                | std::is_heap_until |
| std::is_partitioned	            |std::is_sorted	        |std::is_sorted_until	        | std::lexicographical_compare |
| std::max_element	            |std::merge	            |std::min_element	            | std::minmax_element |
| std::mismatch	                |std::move	            |std::none_of	                | std::nth_element |
| std::partial_sort	            |std::partial_sort_copy	|std::partition	                | std::partition_copy |
| std::remove	                    |std::remove_copy	    |std::remove_copy_if	            | std::remove_if |
| std::replace	                |std::replace_copy	    |std::replace_copy_if	        | std::replace_if |
| std::reverse	                |std::reverse_copy	    |std::rotate	                    | std::rotate_copy |
| std::search	                    |std::search_n	        |std::set_difference	            | std::set_intersection |
| std::set_symmetric_difference	|std::set_union	        |std::sort	                    | std::stable_partition |
| std::stable_sort	            |std::swap_ranges	    |std::transform	                | std::uninitialized_copy |
| std::uninitialized_copy_n	    |std::uninitialized_fill	|std::uninitialized_fill_n	    | std::unique |
| std::unique_copy	|  |  | |


# The New Algorithms

The new algorithms are in the std namespace. std::for_each and std::for_each_n require the header <algorithm>, but the remaining 6 algorithms require the header <numeric>.

| Algorithm 	|	Description |
| :------------ | ----------------: |
| std::for_each | Applies a unary callable to the range. |

| std::for_each_n | Applies a unary callable to the first n elements of the range. |
| std::exclusive_scan |	Applies from the left a binary callable up to the ith (exclusive) element of the range. The left argument of the callable is the previous result. Stores intermediate results. |
| std::inclusive_scan |	Applies from the left a binary callable up to the ith (inclusive) element of the range. The left argument of the callable is the previous result. Stores intermediate results. |
| std::transform_exclusive_scan |	First applies a unary callable to the range and then applies std::exclusive_scan. |
| std::transform_inclusive_scan |	First applies a unary callable to the range and then applies std::inclusive_scan. |
| std::reduce  | 	Applies from the left a binary callable to the range. |
| std::transform_reduce |	Applies first a unary callable to the range and then std::reduce. |















