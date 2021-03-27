/*
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints. Each pipe should be connecting, since the levels ascend, you can assume every number in the sequence after the first index will be greater than the previous and that there will be no duplicates.

Task
Given the a list of numbers, return the list so that the values increment by 1 for each index up to the maximum value.

Example
Input: 1,3,5,6,7,8

Output: 1,2,3,4,5,6,7,8

FUNDAMENTALS LOOPS CONTROL FLOW BASIC LANGUAGE FEATURES LISTS DATA STRUCTURES OBJECTS

Solution Below :

*/

function pipeFix(numbers){
  
    let newArray = (Array.from(numbers));
    const firstNum = newArray[0]
    const secondNum = newArray[newArray.length - 1]
    
    let ans = []
    for(let i = firstNum ; i <= secondNum; i++) {
       ans.push(i )
    }
      return ans;
  }

