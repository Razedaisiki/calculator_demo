# Task: Build a Modular Command Line Calculator

## Objective

Create a modular Python command-line calculator from scratch.

The calculator should support basic arithmetic operations and provide clear error handling.

The final application should be easy to understand, maintain, and test.

---

## Requirements

### 1. Command Line Interface

Create a command line interface:

```

python calculator.py <operation> <number1> <number2>

```

The calculator must support the following operations:

- add
- subtract
- multiply
- divide


Examples:

Command:

```

python calculator.py add 10 5

```

Output:

```

15

```


Command:

```

python calculator.py multiply 4 6

```

Output:

```

24

```

---

### 2. Arithmetic Operations

Implement the following operations:

#### Addition

Calculate:

```

a + b

```


#### Subtraction

Calculate:

```

a - b

```


#### Multiplication

Calculate:

```

a * b

```


#### Division

Calculate:

```

a / b

```

---

### 3. Input Validation

The application must validate user input.

The following cases must be handled:

#### Unsupported operation

Example:

```

python calculator.py power 2 3

```

Expected behavior:

```

Error: unsupported operation

```


#### Invalid number input

Example:

```

python calculator.py add abc 3

```

Expected behavior:

```

Error: invalid number

```


#### Division by zero

Example:

```

python calculator.py divide 10 0

```

Expected behavior:

```

Error: cannot divide by zero

```

The application should not crash.

---

### 4. Code Structure

The implementation should separate different responsibilities.

Recommended structure:

```

calculator.py
operations.py
validator.py
exceptions.py
tests/

```

Responsibilities:

#### calculator.py

Responsible for:

- command line parsing
- calling calculator functions
- displaying results


#### operations.py

Responsible for:

- addition
- subtraction
- multiplication
- division


#### validator.py

Responsible for:

- validating operations
- validating numeric input


#### exceptions.py

Responsible for:

- custom error definitions

---

### 5. Automated Tests

Add automated tests.

Tests should cover:

#### Arithmetic Operations

- addition
- subtraction
- multiplication
- division


#### Error Handling

- unsupported operation
- invalid number input
- division by zero


#### CLI Behavior

Verify that command line usage works correctly.

---

## Acceptance Criteria

The task is complete when:

- [ ] Calculator supports addition, subtraction, multiplication, and division.
- [ ] CLI commands work correctly.
- [ ] Invalid input is handled gracefully.
- [ ] Division by zero is prevented.
- [ ] Code is separated into logical modules.
- [ ] Automated tests are included.
- [ ] All tests pass.

---

## Validation

Run:

```

pytest

```

Expected result:

```

All tests pass.

```

---

## Constraints

- Use Python only.
- Do not use external dependencies.
- Keep the implementation simple.
- Follow clean code practices.
- Do not modify unrelated files.
```