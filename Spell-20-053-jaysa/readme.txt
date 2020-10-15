SPELL CHECKER:

INPUT : -  mistaken word

OUTPUT : - CORRECT WORD
             Test cases given and predicted output

Space and time complexity :- O(n)

Implementation:

we have taken peternorvigs pseudo code as basis and analysed it

but in that we have results that are not appropriate so we extended

it to increase the accuracy like 1)reductions 2) swapping vowels

3) both reductions and swapping

1)Reductions
       if we have the word “Jjoobbbb” then it will convert it to job(which is the correct word)

2)Vowel insertions 
      if  we have the word  “weke” then it will convert it to wake(which is the correct word)

3)Both reduction and vowel
    if  we have the word “cunspirrancy” then it will convert it to conspirancy(which is the correct word)

In this we get the correct words with different probabilities and then we sort them  in reverse order and return it
and we print the one with maximum probability .

Speciality :
No inbuilt libraries are used .Everthing is implemented from scratch.









