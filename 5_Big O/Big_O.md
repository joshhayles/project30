1. What is Big O?
    - Example: A dentist takes 30 minutes to treat each patient. As the list of her patients grows, the time it takes her to treat all patients will scale linerally because it takes her a constant amount of time to treat each individual patient
    - In other words, as the size of the input grows, how drastically do the space / time requirements grow with it?
    - This is written as O(n) where N is equal to the number of patients
    - A constant is any step that doesn't scale with the function input

    O(n) Code Example:
    
    function linearFunc(arr) {
        for (let i = 0; i < arr.length; i++) {
            console.log(1000 * 1000000);
        };
    };

    - When determining the efficiency of an algorithm, we only care about the worst case. So that means that the worst, or the highest order operation, trumps the operations that have better performance. 
        - Example: O(n) + O(1) + O(1) = O(n) The constants get cancelled out because O(n) is the worst case

2. O(n2) and O(n3)
    - Nested for loops
    
    O(n2) Code Example:

    function square(n) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                console.log(i, j);
            };
        };
    };

3. Logarithms
    - A logarithm is the power a number needs to be reaised to, to get some other number
    - For example, 8:
        - We want to raise [some number] to [some power] to get 8. In computer science, unless specified otherwise, we can assume this other number is 2
        - 2 ? = 8 (2 is always the base in computer science)
            - 2 power of 3 = 8 | Log 2 of 8 = 3

4. O (log n) - Recursive Example
    - Example: n = 8

    O(log n) Recursive Code Example:

    function logFunc(n) {
        if (n === 0) return "Done";
        n = Math.floor(n / 2);
        return logFunc(n);
    };

    - When we pass a number into this function it divides n by 2, or splits in half, and then calls itself with the new half, or divided number
    - This has a time complexity of O (log n) because our n is 8, and in cs our base is always 2. And we must have our n 3 times, or three levels deep in the function to get to a point where can no longer reasonably have our input n. Which is another way of saying; Log based 2 of 8 = 3
    - Division is the inverse of multiplication. That means 2 * 2 * 2 = 8 also means we should be able to divide 8 by 2, three times to get 1. The "three iterations" is what's important
    - In the function when we pass in a value for n, we're always going to need to divide this value "n" by two, Log n times before we can get 1

5. O(log n) Binary Search Example (cutting down the array by half)
    - In order for Binary Search to work the Array mush be an ordered Array (ascending or descending)
    1. Find the midpoint of the array in a sorted Array
        - values to the left are "less than" or decreasing, and the right elements are "more than" or increasing.
        - is the number we're searching for "less than" or "more than" the midpoint of the array?

6. O(n log n) | O of n, Log n
    - O of n really means: O(n * log n) | O(4 * 2)

Link(s)
1. https://www.youtube.com/watch?v=Mo4vesaut8g