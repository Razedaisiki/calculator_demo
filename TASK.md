# Task: Build a Modular Command Line Calculator with CI Validation

## Objective

Create a modular Python command-line calculator from scratch.

The calculator should support basic arithmetic operations, provide clear error handling, include automated tests, and configure GitHub Actions CI to automatically validate the project.

The final project should demonstrate a complete software delivery workflow:

Requirement → Implementation → Testing → CI Validation

---

# Requirements

## 1. Command Line Interface

Create a command line interface:

```

python calculator.py <operation> <number1> <number2>

```

The calculator must support:

- add
- subtract
- multiply
- divide


Examples:

Command:

```

python calculator.py add 10 5

```

Expected output:

```

15

```


Command:

```

python calculator.py multiply 4 6

```

Expected output:

```

24

```

---

# 2. Arithmetic Operations

Implement:

## Addition

```

a + b

```

## Subtraction

```

a - b

```

## Multiplication

```

a * b

```

## Division

```

a / b

```

---

# 3. Input Validation and Error Handling

The application must handle invalid inputs gracefully.

## Unsupported operation

Example:

```

python calculator.py power 2 3

```

Expected:

```

Error: unsupported operation

```


## Invalid number input

Example:

```

python calculator.py add abc 3

```

Expected:

```

Error: invalid number

```


## Division by zero

Example:

```

python calculator.py divide 10 0

```

Expected:

```

Error: cannot divide by zero

```


The application should not crash.

---

# 4. Code Structure

Separate responsibilities into different modules.

Recommended structure:

```

calculator.py
operations.py
validator.py
exceptions.py
tests/
.github/
workflows/
test.yml

```


Responsibilities:


## calculator.py

Responsible for:

- parsing command line arguments
- invoking calculator operations
- printing results


## operations.py

Responsible for:

- addition
- subtraction
- multiplication
- division


## validator.py

Responsible for:

- validating operations
- validating numeric inputs


## exceptions.py

Responsible for:

- custom error definitions


---

# 5. Automated Tests

Add automated tests using pytest.

Tests must cover:

## Arithmetic Operations

- addition
- subtraction
- multiplication
- division


## Error Handling

- unsupported operation
- invalid number input
- division by zero


## CLI Behavior

Verify command line execution behavior.

---

# 6. GitHub Actions CI Integration

Configure GitHub Actions to automatically run tests.

Create:

```

.github/workflows/test.yml

```

The CI workflow should:

1. Trigger on:

- push events
- pull request events


2. Setup Python environment.


3. Install required dependencies.


4. Run:

```

pytest

```


5. Fail the workflow when tests fail.


Example workflow behavior:

```

Code Push

```
↓
```

GitHub Actions Triggered

```
↓
```

Install Dependencies

```
↓
```

Run Tests

```
↓
```

Pass / Fail

```

---

# Acceptance Criteria

The task is complete when:

- [ ] Calculator supports four arithmetic operations.
- [ ] CLI commands work correctly.
- [ ] Invalid input is handled gracefully.
- [ ] Code is separated into logical modules.
- [ ] Automated tests are included.
- [ ] GitHub Actions workflow is configured.
- [ ] CI runs automatically on push and pull request.
- [ ] CI passes successfully.
- [ ] All tests pass.

---

# Validation

The following validations must succeed:

## Local Validation

Run:

```

pytest

```

Expected:

```

All tests pass.

```


## CI Validation

Push the repository to GitHub.

Verify:

```

GitHub Actions
|
↓
Test Workflow
|
↓
pytest PASS

```

---

# Constraints

- Use Python only.
- Use pytest for testing.
- Use GitHub Actions for CI.
- Do not use external dependencies unless necessary.
- Keep implementation simple and modular.
- Do not modify unrelated files.
```
