# CMPS 2200  Recitation 02

**Name (Team Member 1):** Samuel Kelly 
**Name (Team Member 2):** n/a

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [x] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

Using the Master Theorem for W(n) = 2W(n/2) + f(n):

For f(n) = 1:
   Compare n^{\log_2(2)} = n^1 with f(n) = 1
   Since (n) is polynomially smaller than n^1
   Therefore, W(n) = O(n)

For f(n) = log n:
   Compare n^{\log_2(2)} = n^1 with f(n) = \log n
   Case 2 applies since f(n) = \log n is not polynomially smaller/larger
   Therefore, =W(n) = O(n \log n)

For f(n) = n:
   Compare n^{\log_2(2)} = n^1 with f(n) = n
   Case 3 applies since they are equal
   Therefore, W(n) = O(n \log n)

The empirical results from the test_asymptotic() in test_main.py confirm these theoretical bounds, showing that f(n) = 1 grows linearly while both f(n) = log n and f(n) = n exhibit n log n growth, with f(n) = n having larger constants.





- [x] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

Using the Master Theorem for W(n) = aW(n/b) + n^c with a=4, b=2 (thus \log_b a = 2):

When c < \log_b a:
W(n) = O(n^{\log_b a}) 

When c = \log_b a:
W(n) = O(n^c \log n) 

When c > \log_b a:
W(n) = O(n^c)

Our empirical results confirm these bounds. When testing with c=1 (less than \log_2(4)=2), the growth is quadratic and the recurrence is dominated by the leaves. When c=2 (equal), we see n^2\log n growth and the recurrence is balanced. When c=3 (greater), we see cubic growth, and the recurrence is dominated by the root level, matching our theoretical analysis.

test_main.py 
Comparing c < log_b(a) vs c = log_b(a)
|   n |   W_1 |   W_2 |
|-----|-------|-------|
|  10 |   126 |   328 |
|  20 |   524 |  1712 |
|  40 |  2136 |  8448 |
|  80 |  8624 | 40192 |

Comparing c = log_b(a) vs c > log_b(a)
|   n |   W_1 |     W_2 |
|-----|-------|---------|
|  10 |   328 |    1692 |
|  20 |  1712 |   14768 |
|  40 |  8448 |  123072 |
|  80 | 40192 | 1004288 |


- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

For f(n) = 1:
S(n) = S(n/2) + 1
This gives us S(n) = Θ(log n)

For f(n) = log n:
S(n) = S(n/2) + log n
This gives us S(n) = Θ(log² n)

For f(n) = n:
S(n) = S(n/2) + n
This gives us S(n) = Θ(n)

test_main.py::test_compare_span 
Comparing span with f(n)=1 vs f(n)=log n
|   n |   W_1 |    W_2 |
|-----|-------|--------|
|  10 |     4 |  7.644 |
|  20 |     5 | 11.966 |
|  50 |     6 | 19.043 |
| 100 |     7 | 25.686 |

Comparing span with f(n)=log n vs f(n)=n
|   n |    W_1 |   W_2 |
|-----|--------|-------|
|  10 |  7.644 |    18 |
|  20 | 11.966 |    38 |
|  50 | 19.043 |    97 |
| 100 | 25.686 |   197 |

