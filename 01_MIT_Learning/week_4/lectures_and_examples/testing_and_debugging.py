Defensive Programming
- Write specs for funtions
- Modularize programs
- Check conditions on inputs/outputs

Testing & Validation
- Compare input and output to specs

Debugging
- How can I break my programs
- What should work, what should not work
- What events lead to program borking
- Break code into modules that can be tested individually
- Have a set of expected results to test against


Different types of test
- Unit Tests
    - Validate each piece of program
    - Test each function separately

- Regression Testing
    - Add test for bugs as you find them in a function
    - Catch reintroduced errors that were previously fixed

- Integration Testing
    - Test overall program
    - Do not rush this

# ###########################

Testing Approaches
- intuition about natural boundaries to the problem
- Random testing
- Black box testing - explore paths through specifications
- Glass box testing - explore all paths through code


Black Box Testing
- Designed without looking at the code, look at the specs only
- Avoids implicit biases, can be done by someone else
- Test can be reused if implementation changes

Glass Box Testing
- Use code directly to guide design of test cases
- Called path complete if every potential path through code
   is tested at least once. 
- Drawbacks include: 
    - can go through loops arbitrarily many times (recursion)
    - Missing paths
    Guidelines:
    - branches
    - for loops
    - while loops


Types of Bugs:
- Overt - clearly, obvious - code crashes or runs forever
- Covert - nothing obvious. Code returns a value, but might be incorrect
         - Might also be legal in one case, but illegal in another


# DEBUGGING 

- Steep learning curve
- Goal is to have a bug-free program
- Experienced programmers know what to look out for
    - based on prior experience
- Use IDEs for help in bug in tracking

- IndexError: trying to access beyond the limits of a limit
- TypeError: trying to convert inappropriate type
- NameError: referencing non-existent variable
- TypeError: mixing data types without proper coercion
- SyntaxError: forgetting to close parenth, or semicolon, etc.
- IOError: IO system reports malfunction, e.g. file not found
- AttributeError: Attribute reference fails
- AssertionError: raise an exception if assumption is not met


Logic Errors are tough to find
- Sketch out Logic
- Think before writing code
- Explain out your code (rubber duck)


DEBUGGING STEPS:
- study program code
    - ask how did you get unexpected result
    - dont ask what is wrong
    - is it part of a family of problems

- scientific method
    - study available data
    - come up with hypothesis
    - experiment
    - test experiments with simple tests

TEST AS YOU GO. 
BUILD INCREMENTALLY - starting large, and narrowing in



# DEALING WITH EXCEPTIONS / ERRORS
A Few General Options
1. Fail Silently
    - substitute default values or just continue
    - BAD BAD BAD BAD BAD BAD IDEA !!!!

2. Return "error" value
    - What value to choose?
    - Complicates code having to check for special value

3. Stop execution, signal error condition
    - Raise an exception
    - raise Exception("descriptive string")


AssertionError can raise erros based on if exception errors
are not met