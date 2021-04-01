/*

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

Examples

 123 ->  321
-456 -> -654
1000 ->    1

Solution Below :

*/

function reverseNumber(n) {
    // ...
    if (n < 0) {
      const arr = n.toString()
      const new_str = arr.replace('-','')
      const next_str = new_str.split('')
      const reverseStr = next_str.reverse()
      const joinStr = next_str.join('')
      const finalStr = '-' + joinStr
      return parseInt(finalStr)
    }else{
      const arr = n.toString()
      const next_str = arr.split('')
      const reverseStr = next_str.reverse()
      const joinStr = next_str.join('')
      return parseInt(joinStr)
    }

  }