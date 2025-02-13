
Files
Commands
__pycache__
.git
.github
.pytest_cache
main.py
README.md
Screenshot for Question 5 in README.png
test_main.py
Packager files
.pythonlibs
.upm
requirements.txt
Config files
.replit
replit.nix
File
Folder
Assistant
README.md
README.md
Open in Editor
CMPS 2200 Recitation 02
Name (Team Member 1): Samuel Kelly Name (Team Member 2): n/a
In this recitation, we will investigate recurrences. To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit main.py.
Running and testing your code
To run tests, from the command-line shell, you can run
pytest test_main.py will run all tests
pytest test_main.py::test_one will just run test_one
We recommend running one test at a time as you are debugging.
Turning in your work
Once complete, click on the "Git" icon in the left pane on repl.it.
Enter a commit message in the "what did you change?" text box
Click "commit and push." This will push your code to your github repository.
Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.
Recurrences
In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on recurrences of the form:
$$ W(n) = aW(n/b) + f(n) $$
where $W(1) = 1$.
 1. (2 point) In main.py, you have stub code which includes a function simple_work_calc. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.
 2. (2 point) Test that your function is correct by calling from the command-line pytest test_main.py::test_simple_work by completing the test cases and adding 3 additional ones.
 3. (2 point) Now implement work_calc, which generalizes the above so that we can now input $a$, $b$ and a function $f(n)$ as arguments. Test this code by completing the test cases in test_work and adding 3 more cases.
 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
Using the Master Theorem for $W(n) = 2W(n/2) + f(n)$:
For f(n) = 1:
Compare n^{\log_2(2)} = n^1 with f(n) = 1
Since (n) is polynomially smaller than n^1
Therefore, W(n) = O(n)
For f(n) = log n:
Compare $n^{\log_2(2)} = n^1$ with $f(n) = \log n$
Case 2 applies since $f(n) = \log n$ is not polynomially smaller/larger
Therefore, $W(n) = \Theta(n \log n)$
For f(n) = n:
Compare $n^{\log_2(2)} = n^1$ with $f(n) = n$
Case 3 applies since they are equal
Therefore, $W(n) = \Theta(n \log n)$

The empirical results from the test_asymptotic() in test_main.py confirm these theoretical bounds, showing that f(n) = 1 grows linearly while both f(n) = log n and f(n) = n exhibit n log n growth, with f(n) = n having larger constants.

 5. (4 points) Now that you have a nice way to empirically generate values of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify test_compare_work to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

Using the Master Theorem for W(n) = aW(n/b) + n^c with a=4, b=$ (thus \log_b a = 2):
When c < \log_b a:
W(n) = O(n^{\log_b a}) =O(n^2)
When c = \log_b a:
W(n) = O(n^c \log n) = O(n^2 \log n)
When c > \log_b a:
W(n) = O(n^c)
Our empirical results confirm these bounds. When testing with c=1 (less than \log_2(4)=2), the growth is quadratic. When c=2 (equal), we see n^2\log n growth. When c=3 (greater), we see cubic growth, matching our theoretical analysis.

Evidence with screenshot proof is attached in the files


 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function span_calc to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement test_compare_span to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should.

For f(n) = 1: S(n) = S(n/2) + 1 This gives us S(n) = Θ(log n)

For f(n) = log n: S(n) = S(n/2) + log n This gives us S(n) = Θ(log² n)

For f(n) = n: S(n) = S(n/2) + n This gives us S(n) = Θ(n)

