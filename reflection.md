# Reflection – Lab 5: Static Code Analysis

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were the style-related ones, such as formatting errors, missing spaces, and old-style 
string formatting. These only required simple code cleanups or replacing `%` formatting with f-strings. The 
hardest issues were those related to mutable default arguments and missing input validation. They required 
a deeper understanding of Python’s behavior and the correct approach to ensure the code remains functional 
and bug-free after the changes.

### 2. Did the static analysis tools report any false positives? If so, describe one example.
Yes, there were a few false positives. For example, Pylint flagged the use of a global variable as a potential 
design flaw. In this program, however, `stock_data` is intentionally global because it represents a shared 
inventory state used across multiple functions. Hence, while Pylint’s warning is valid in general, in this 
specific context it was acceptable and necessary.

### 3. How would you integrate static analysis tools into your actual software development workflow?
I would integrate static analysis tools like Pylint, Flake8, and Bandit into a Continuous Integration (CI) 
pipeline so that code is automatically checked whenever new commits are pushed. Additionally, I would run 
them locally before committing changes to ensure the code follows best practices and is free from common 
bugs or security issues. This would help maintain consistent quality across the development lifecycle.

### 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?
After applying the fixes, the code became more robust, readable, and secure. The new version follows 
PEP 8 style guidelines, includes detailed logging for easier debugging, and avoids insecure practices such 
as using `eval()`. Using context managers and input validation improved reliability, and the addition of 
docstrings made the code easier to understand and maintain.
