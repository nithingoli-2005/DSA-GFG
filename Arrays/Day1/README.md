The above code explain finds the second Largest element of array.

First, it checks whether the list has at least two elements. If it doesn’t, it immediately returns -1 because it’s impossible to have a second-largest value with fewer than two numbers.

It keeps track of two values while going through the list:

  The largest number found so far

  The second largest number found so far

As it examines each number:

  If the number is bigger than the current largest, it updates the second largest to be the old largest, and sets the largest to the new number.

  If the number is not the largest but is bigger than the current second largest, and it’s different from the largest, it becomes the new second largest.

After checking all the numbers:

  If a valid second largest value was found, it returns that number.

  Otherwise, it returns -1 to indicate there’s no second largest number (e.g. all numbers were the same).

