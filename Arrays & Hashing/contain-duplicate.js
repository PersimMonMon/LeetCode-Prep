/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.


Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
*/


// function takes in array (nums) and return true if value appears twice, else false 
let containsDuplicate = function(nums) {

  // use Set() to only take in a value once 
  let oneValue = new Set();

  //get each value in nums, check if already in nums
  for (let num of nums) {
    if (oneValue.has(num)) {
      return true
    } else {
      oneValue.add(num)
    }
  }
  return false;
};

// try to shorten runtime
let containsDuplicate2 = function(nums) {
  if (new Set(nums).size === nums.length) {
    return false;  // no duplicates
  } else {
    return true;   // duplicates exist
  }
};


