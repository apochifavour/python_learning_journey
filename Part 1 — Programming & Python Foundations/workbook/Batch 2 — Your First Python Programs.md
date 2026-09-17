# 🐍 Python Learning Journey

## Part 1 — Programming & Python Foundations

### Batch 2 — Your First Python Programs

> **Theme:** From Programmer Thinking → Executable Python
> **Level:** Beginner
> **Projects:** 💰 Wallet App + 🛒 Store App
> **Prerequisite:** Batch 1 — Thinking Like a Programmer

---

# 😎 Welcome Back, Apprentice

In Batch 1, you learned something more important than syntax:

> **How to think before you code.**

You learned to take a problem and break it down.

You learned:

```text
Problem
   ↓
Break it down
   ↓
Input → Process → Output
   ↓
Algorithm
   ↓
Pseudocode
   ↓
Code
```

Now we cross the first major bridge.

You're going from:

> "I know what the program should do."

to:

> **"I can make Python do it."** 🐍

But don't rush.

This batch is **not** about learning everything Python can do.

It's about becoming comfortable with the basic shape of a Python program.

By the end of this batch, you should be able to look at simple Python code and understand:

* what Python is executing
* what `print()` does
* what a string is
* what numbers are
* how Python evaluates simple expressions
* what comments are
* why indentation matters
* what syntax errors look like
* how to read simple error messages
* how to run a Python file
* how to debug basic mistakes

And most importantly:

> **You should stop being afraid of seeing Python code.**

---

# 🧭 Where You Are

Your journey currently looks like this:

```text
BATCH 1
Thinking Like a Programmer
        ↓
BATCH 2 ← YOU ARE HERE
Your First Python Programs
        ↓
BATCH 3
Variables & Data
        ↓
BATCH 4
Operators & Expressions
        ↓
BATCH 5
Input & Output
        ↓
BATCH 6
Strings
        ↓
BATCH 7
Conditionals
        ↓
BATCH 8
Loops
        ↓
PART 1 BOSS FIGHT
```

Notice something important:

### We are intentionally separating concepts.

You will see some operators in this batch because Python programs need them.

But **Batch 4** will study operators and expressions properly.

You will also see values that could eventually be stored in variables.

But **Batch 3** is where variables become a major topic.

This is deliberate.

We're building the foundation layer by layer.

---

# 🎯 Batch 2 Mission

By the end of this batch, you should be able to:

### Core Understanding

* Explain what a Python program is.
* Explain what Python's interpreter does.
* Understand what an instruction is.
* Understand `print()`.
* Recognize strings.
* Recognize integers and decimals.
* Understand comments.
* Understand basic indentation.
* Recognize common syntax mistakes.

### Practical Skills

You should be able to:

* create a `.py` file
* run a Python program
* use `print()`
* print text
* print numbers
* print simple calculations
* write comments
* read basic error messages
* locate simple syntax mistakes
* fix basic indentation problems

### Programmer Skill

Most importantly:

> **You should be able to read a small Python program line by line and explain what Python will do.**

---

# 🛠️ SETUP & RUN GUIDE

Before doing the exercises, make sure your Python environment works.

You need:

* Python 3
* a text editor or IDE
* a terminal/command prompt

---

## Option A — Check Python in the Terminal

Open your terminal.

Try:

```bash
python --version
```

If that doesn't work, try:

```bash
python3 --version
```

You should see something similar to:

```text
Python 3.x.x
```

The exact version is not important for this batch as long as you're using Python 3.

---

# 📁 Create Your Practice Folder

Create a folder for this batch:

```text
python_learning/
└── batch_2/
```

Inside it, create:

```text
batch_2/
├── practice.py
├── wallet.py
└── store.py
```

You don't have to create all three immediately, but this will eventually be our structure.

---

# ▶️ Running a Python File

Put this inside `practice.py`:

```python
print("Hello, Python!")
```

Save the file.

Then run:

```bash
python practice.py
```

Or:

```bash
python3 practice.py
```

Expected output:

```text
Hello, Python!
```

Congratulations.

You have now written and executed a Python program. 🐍🔥

It may look tiny.

That's exactly the point.

Every serious Python application is ultimately built from small instructions like this.

---

# 🧠 BATCH 2 — BIG IDEA #1

# What Is a Python Program?

A program is a collection of instructions that a computer executes.

For example:

```python
print("Hello")
print("Welcome")
print("Goodbye")
```

Python reads the instructions and executes them.

The result:

```text
Hello
Welcome
Goodbye
```

Notice the order.

Python normally executes these instructions from top to bottom.

That connects directly to something you learned in Batch 1:

> **Sequence**

---

# 🧩 Sequence in Python

Remember:

```text
Instruction 1
      ↓
Instruction 2
      ↓
Instruction 3
```

Python:

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

The order matters.

If you change the order:

```python
print("Third")
print("First")
print("Second")
```

You get:

```text
Third
First
Second
```

Python isn't guessing your intentions.

It follows the instructions you give it.

---

# 🥋 Apprentice Rule #1

> **Python executes instructions. It does not read your mind.**

If the instruction is wrong, Python doesn't automatically fix your thinking.

That is why Batch 1 matters.

---

# 🧠 BIG IDEA #2

# `print()`

One of the first Python tools you'll learn is:

```python
print()
```

It tells Python:

> **Display something on the screen.**

Example:

```python
print("Hello")
```

Output:

```text
Hello
```

Another:

```python
print("Welcome to Python")
```

Output:

```text
Welcome to Python
```

---

# 🔍 Reading `print()`

Look at:

```python
print("Hello")
```

Break it apart:

```text
print
  ↓
the function being called

"Hello"
  ↓
the value being given to print
```

You don't need to master functions yet.

That comes later.

For now, understand:

```python
print(...)
```

means:

> **Show this thing on the screen.**

---

# 🧪 Practice 1 — First Commands

Write a program that displays:

```text
Hello, World!
I am learning Python.
I will become a Python programmer.
```

Use three `print()` statements.

Do not copy the answer immediately.

Try it yourself first.

---

# 🧠 BIG IDEA #3

# Strings

A string is text.

Examples:

```python
"Hello"
"Python"
"Wallet"
"Store"
"₦10,000"
"I am learning Python"
```

Strings are surrounded by quotation marks.

For example:

```python
print("Python")
```

Python understands `"Python"` as text.

---

# 🔤 Single and Double Quotes

You can commonly write strings using:

```python
"Hello"
```

or:

```python
'Hello'
```

Both represent text.

For now, choose one style and stay consistent.

Examples:

```python
print("Hello")
print('Hello')
```

Both produce:

```text
Hello
```

---

# ⚠️ Quotes Matter

This:

```python
print("Hello")
```

is valid.

But this:

```python
print(Hello)
```

is different.

Python does not automatically know that `Hello` is supposed to be text.

You will learn why in the Variables & Data batch.

For now:

> **Text → put it inside quotes.**

---

# 🧪 Practice 2 — Text Recognition

For each item, identify whether it is **text**:

```text
1. "Wallet"
2. 5000
3. "5000"
4. "Store"
5. 250.5
```

Think carefully.

Especially about:

```text
5000
```

versus:

```text
"5000"
```

They may look similar to a human.

Python treats them differently.

---

# 🧠 BIG IDEA #4

# Numbers

Python can work with numbers.

For example:

```python
print(10)
```

Output:

```text
10
```

You can also print decimals:

```python
print(10.5)
```

Output:

```text
10.5
```

For now, recognize two common forms:

### Integer

A whole number:

```python
10
500
2000
100000
```

### Float

A number containing a decimal point:

```python
10.5
2500.75
0.5
99.99
```

You'll study data types more deeply later.

For now:

> **Python can represent numbers directly.**

---

# 🧪 Practice 3 — Numbers

Write Python statements that display:

```text
500
2500
99.99
0
```

Use `print()`.

---

# 🧠 BIG IDEA #5

# Python Can Calculate

Python isn't only a language for displaying text.

It can also perform calculations.

Example:

```python
print(2 + 3)
```

Output:

```text
5
```

Another:

```python
print(10 - 4)
```

Output:

```text
6
```

Another:

```python
print(5 * 2)
```

Output:

```text
10
```

And:

```python
print(20 / 4)
```

Output:

```text
5.0
```

Don't worry about memorizing every operator yet.

That's coming properly in Batch 4.

For now, recognize the pattern:

```python
print(expression)
```

Python evaluates the expression and displays the result.

---

# 💰 Wallet Example

Suppose a wallet has:

```text
₦10,000
```

and we want to represent a deposit of:

```text
₦5,000
```

For now, without variables:

```python
print(10000 + 5000)
```

Output:

```text
15000
```

The thinking came from Batch 1:

```text
Input:
₦10,000
₦5,000

Process:
Add them

Output:
₦15,000
```

Now we're translating that thinking into Python.

---

# 🛒 Store Example

A product costs:

```text
₦2,000
```

A customer buys:

```text
4
```

products.

You already solved this in Batch 1.

The process is multiplication:

```text
₦2,000 × 4
```

Python:

```python
print(2000 * 4)
```

Output:

```text
8000
```

Notice the bridge:

```text
Real-world problem
        ↓
Mathematical process
        ↓
Python expression
```

This is programming.

---

# 🧠 BIG IDEA #6

# Code Is Precise

Humans can understand:

> "Calculate the total price of four products costing ₦2,000 each."

Python needs an actual instruction:

```python
print(2000 * 4)
```

This is why programming requires precision.

Your brain supplies the meaning.

Your code must supply the exact instruction.

---

# 🥋 Apprentice Rule #2

> **If your thinking is vague, your code will probably be vague.**

Batch 1 trained the thinking.

Batch 2 begins translating that thinking.

---

# 📝 BIG IDEA #7

# Comments

Sometimes you want to write a note inside your code.

Python provides comments.

A comment begins with:

```python
#
```

Example:

```python
# Display a welcome message
print("Welcome")
```

Python ignores the comment.

It executes:

```python
print("Welcome")
```

---

# Why Comments Matter

Comments can explain:

* what a section does
* why something is being done
* what you're testing
* information that helps another programmer understand the code

Example:

```python
# Display the store name
print("My Store")
```

---

# ⚠️ Don't Comment Everything

Bad:

```python
# Print hello
print("Hello")

# Print welcome
print("Welcome")

# Print goodbye
print("Goodbye")
```

The comments don't add much value.

The code already makes the purpose obvious.

A useful comment explains something that isn't immediately obvious.

---

# 🧪 Practice 4 — Comments

Write a small program containing:

1. One useful comment.
2. A `print()` displaying your wallet name.
3. A `print()` displaying a starting balance.

Don't use variables yet.

---

# 🧠 BIG IDEA #8

# Indentation

Python uses indentation to organize code.

For now, you only need to understand one important rule:

> **Indentation can affect how Python interprets your program.**

Example:

```python
if True:
    print("Hello")
```

The indented line belongs to the `if` block.

You don't need to master `if` yet.

That comes later.

For now, notice:

```python
if True:
    print("Hello")
```

versus:

```python
if True:
print("Hello")
```

The second version has an indentation problem.

---

# 🥋 Apprentice Rule #3

When you see:

```python
:
```

at the end of a statement that begins a block, Python often expects an indented block underneath it.

You'll learn this properly when we reach conditionals and loops.

---

# 🧠 BIG IDEA #9

# Syntax

Syntax means the rules for writing valid code.

Think about human language.

This:

> I am learning Python.

follows normal English structure.

Something like:

> Python learning am I.

might still be understandable to a human.

Computers are far less forgiving.

Python expects its syntax to be correct.

---

# Example Syntax Error

This is valid:

```python
print("Hello")
```

This is not:

```python
print("Hello"
```

The closing `)` is missing.

Python will complain.

That complaint is useful.

It tells you:

> "Something about your code doesn't follow Python's rules."

---

# 🧠 Error Messages Are Not Enemies

Beginners often see:

```text
SyntaxError
```

and think:

> "I broke Python." 😭

No.

You didn't break Python.

Python is telling you:

> **"I don't understand this instruction."**

Your job is to investigate.

---

# 🔎 Debugging Method

When Python gives you an error:

### Step 1 — Don't panic.

Read it.

### Step 2 — Find the error type.

For example:

```text
SyntaxError
```

### Step 3 — Look at the line number.

Python often tells you where it encountered the problem.

### Step 4 — Inspect that line.

Look for:

* missing quotes
* missing parentheses
* extra characters
* incorrect spelling
* indentation problems

### Step 5 — Read the surrounding lines too.

Sometimes the actual mistake is just before the line Python highlights.

### Step 6 — Fix one thing.

Run the program again.

---

# 🧪 Debugging Lab 1 — Missing Parenthesis

You are given:

```python
print("Welcome to the Wallet"
```

### Your mission

Identify the problem.

Then fix it.

---

# 🧪 Debugging Lab 2 — Broken String

Find the problem:

```python
print("Welcome)
```

What is missing?

Fix it.

---

# 🧪 Debugging Lab 3 — Incorrect Indentation

Find the problem:

```python
if True:
print("Python")
```

Fix the indentation.

---

# 🧪 Debugging Lab 4 — Multiple Lines

Find the mistakes:

```python
print("Welcome to the Store"
print("Products available")
print("Thank you)
```

There is more than one problem.

Don't fix everything randomly.

Use your debugging method.

---

# 🧠 TRACE TRAINING

Remember tracing from Batch 1?

Let's use it.

Consider:

```python
print("Start")
print(2 + 3)
print("End")
```

Trace it.

### Line 1

```python
print("Start")
```

Output:

```text
Start
```

### Line 2

```python
print(2 + 3)
```

Python calculates:

```text
2 + 3 = 5
```

Output:

```text
5
```

### Line 3

```python
print("End")
```

Output:

```text
End
```

Final output:

```text
Start
5
End
```

---

# 🥋 Apprentice Rule #4

> **Before running code, train yourself to predict the output.**

This is one of the simplest ways to become better at programming.

Don't always depend on the computer to tell you what your code does.

Try to know first.

Then run it.

Then compare.

---

# 🧪 Practice 5 — Predict Before Running

What will this produce?

```python
print("Wallet")
print(10000)
print(5000)
print(10000 + 5000)
```

Write the expected output before running it.

Then run it.

Compare your prediction with Python's output.

---

# 🧪 Practice 6 — Predict the Sequence

What will this output?

```python
print("Store")
print("Products")
print(2000)
print(2000 * 4)
print("Done")
```

Don't run it immediately.

Trace it first.

---

# 🧠 VALUE VS TEXT

This is an important distinction.

Compare:

```python
print(5000)
```

with:

```python
print("5000")
```

Both display:

```text
5000
```

But they are not the same kind of value.

The first is a number.

The second is text.

This distinction becomes extremely important later.

For example:

```python
print(5000 + 1000)
```

produces:

```text
6000
```

But treating text like numbers introduces different rules.

We'll study this much more in later batches.

For now, remember:

> **What something looks like on the screen isn't necessarily what it is internally.**

---

# 💰 MINI PROJECT — Wallet App v0.1

It's time to make the first tiny version of one of your long-term projects.

Remember:

> This is **not** the final Wallet App.

This is Version 0.1.

We're intentionally keeping it tiny.

---

## 🎯 Goal

Create a program that displays:

```text
====================
     MY WALLET
====================

Starting Balance:
₦10000

Deposit:
₦5000

Balance After Deposit:
₦15000
```

You can implement the calculations with `print()`.

For example:

```python
print(10000 + 5000)
```

---

## Constraints

For this version:

### Allowed

* `print()`
* strings
* numbers
* basic arithmetic
* comments

### Not yet required

* variables
* `input()`
* conditionals
* loops
* functions
* classes
* files

Why?

Because we're learning to build progressively.

---

# 🛒 MINI PROJECT — Store App v0.1

Now create a tiny store program.

The scenario:

```text
Product:
Notebook

Price:
₦2000

Quantity:
4

Total:
₦8000
```

Your program should display the information.

Then calculate the total using Python.

Example:

```python
print(2000 * 4)
```

Again:

> Don't worry about making it interactive yet.

The interactive version comes later.

---

# 🧠 PROJECT THINKING

Notice how our projects are evolving.

### Batch 1

We designed the logic.

```text
Input
Process
Output
```

### Batch 2

We're implementing tiny static versions.

```text
print()
numbers
calculations
```

### Batch 3

We'll introduce:

```text
variables
```

Then our programs can start storing information.

Eventually:

```text
price = ...
quantity = ...
```

Then:

```text
total = ...
```

Then later:

```text
input()
```

And eventually:

```text
functions
collections
objects
files
testing
```

That's how the projects grow.

---

# 🧨 CHALLENGE ZONE

These are deliberately harder.

Don't immediately look for solutions.

---

## 🔥 Challenge 1 — Wallet Calculation

A wallet contains:

```text
₦25,000
```

The user deposits:

```text
₦7,500
```

Write a Python program that displays:

```text
Starting balance
Deposit
New balance
```

Calculate the new balance with Python.

---

## 🔥 Challenge 2 — Store Checkout

A customer buys:

```text
5 shirts
```

Each shirt costs:

```text
₦6,000
```

Write a program that displays:

```text
Product
Price
Quantity
Total
```

Calculate the total.

---

## 🔥 Challenge 3 — Multiple Products

A customer buys:

```text
3 notebooks at ₦2,000 each
2 pens at ₦500 each
```

Your program should calculate the combined total.

Think about the algorithm first.

Don't just start typing.

Use:

```text
Input:
Process:
Output:
```

Then translate your thinking into Python.

---

# 🧠 DEBUGGING BOSS — The Broken Store

You inherit this code:

```python
# Store checkout

print("Welcome to the Store"

print("Notebook")
print(2000)

print("Quantity")
print(4)

print("Total")
print(2000 * 4
```

Your mission:

1. Identify every syntax problem.
2. Fix them.
3. Run the program.
4. Verify the output.
5. Explain what each correction fixed.

Don't simply make it work.

Understand **why** it was broken.

---

# 🧠 COMPREHENSION CHECK

Answer these without running Python.

### 1.

What does `print()` do?

### 2.

What is a string?

### 3.

What is the difference between:

```python
5000
```

and:

```python
"5000"
```

### 4.

What is a comment?

### 5.

What symbol begins a Python comment?

### 6.

What does indentation do?

### 7.

What does `SyntaxError` generally mean?

### 8.

What should you do when Python gives you an error?

### 9.

What is the output?

```python
print(10 + 5)
```

### 10.

What is the output?

```python
print("10 + 5")
```

### 11.

Why are those two examples different?

### 12.

What does this produce?

```python
print("Wallet")
print(10000)
print(5000)
print(10000 + 5000)
```

---

# 🥋 SKILL CHECK PREPARATION

Your eventual skill check for this batch should test whether you can independently:

### Part A — Explain

Explain:

* Python programs
* sequence
* `print()`
* strings
* numbers
* comments
* syntax
* indentation
* errors

### Part B — Write

Write a simple Python program using:

```python
print()
```

with:

* text
* numbers
* calculations
* comments

### Part C — Predict

Given a small Python program:

> Predict its output before running it.

### Part D — Debug

Given broken Python:

> Identify and fix the problem.

### Part E — Translate

Given a simple real-world scenario:

> Think through the Input → Process → Output and implement it in Python.

---

# 🧠 REVISION PACK

Before leaving this batch, you should be comfortable with this mental model:

```text
PYTHON PROGRAM
      ↓
Python reads instructions
      ↓
Instructions execute
      ↓
Usually from top to bottom
      ↓
Python evaluates values/expressions
      ↓
Python produces output
```

---

## Core Syntax

### Display text

```python
print("Hello")
```

### Display a number

```python
print(5000)
```

### Calculate

```python
print(2000 * 4)
```

### Comment

```python
# This is a comment
```

### Basic block indentation

```python
if True:
    print("Hello")
```

---

# 🚨 COMMON BEGINNER MISTAKES

Watch for these.

### Mistake 1 — Missing quotes

```python
print(Hello)
```

when you intended:

```python
print("Hello")
```

---

### Mistake 2 — Missing closing parenthesis

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

---

### Mistake 3 — Broken string

```python
print("Hello)
```

Correct:

```python
print("Hello")
```

---

### Mistake 4 — Incorrect indentation

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

---

### Mistake 5 — Not reading the error

Don't immediately rewrite the entire program.

First ask:

```text
What error did Python give me?
Which line?
What was Python expecting?
What did I actually write?
```

That's debugging.

---

# 🧠 THE DEBUGGING MINDSET

A beginner says:

> "The code doesn't work."

A growing programmer says:

> "Python gave me a SyntaxError on line 4. Let me inspect line 4 and the line before it."

That difference matters.

Your goal isn't to never make mistakes.

Your goal is to become good at **finding and fixing them**.

---

# 🥋 BATCH 2 FINAL CHALLENGE

Without looking at the previous examples, build this yourself:

## 💰 Wallet Display

Your program should produce something like:

```text
========================
       MY WALLET
========================

Starting Balance
₦30000

Deposit
₦12000

New Balance
₦42000
```

Requirements:

* Use `print()`.
* Use numbers for calculations.
* Use strings for text.
* Include at least one useful comment.
* Calculate the new balance with Python.
* Don't use variables yet.
* Don't use `input()` yet.

---

## 🛒 Store Display

Then build:

```text
========================
       MY STORE
========================

Product
Backpack

Price
₦15000

Quantity
3

Total
₦45000
```

Requirements:

* Use `print()`.
* Use strings.
* Use numbers.
* Calculate the total.
* Include a useful comment.
* Don't use variables yet.
* Don't use `input()` yet.

---

# 🧠 FINAL REFLECTION

Before moving to Batch 3, answer these questions for yourself:

### 1.

Can I create and run a `.py` file without being guided?

### 2.

Can I explain what `print()` does?

### 3.

Can I distinguish text from numbers?

### 4.

Can I predict simple program output?

### 5.

Can I identify a missing quote or parenthesis?

### 6.

Can I read a basic error message without panicking?

### 7.

Can I explain why indentation matters?

### 8.

Can I turn a simple Input → Process → Output problem into Python code?

If several answers are "no," don't rush.

Practice.

---

# 🌱 GROWTH LOG

Record this in your learning journal after completing the batch.

```text
## Python — Batch 2 Growth Log

### What I learned

-

### What became easier

-

### What confused me

-

### Bugs I fixed

-

### Biggest mistake I made

-

### What I now understand better

-

### One thing I can do independently now

-

### One thing I still need to practice

-

### Confidence level
__/10

### Next target

Batch 3 — Variables & Data
```

---

# 📈 PROGRESS MAP

After completing Batch 2:

```text
✅ Batch 1 — Thinking Like a Programmer

✅/🚧 Batch 2 — Your First Python Programs
              ↑
              YOU ARE HERE

⬜ Batch 3 — Variables & Data

⬜ Batch 4 — Operators & Expressions

⬜ Batch 5 — Input & Output

⬜ Batch 6 — Strings

⬜ Batch 7 — Conditionals

⬜ Batch 8 — Loops

⬜ Part 1 Boss Fight
```

---

# 🚪 EXIT CRITERIA

You are ready for Batch 3 when you can independently:

* create a Python file
* run it from the terminal
* use `print()`
* print strings
* print numbers
* perform simple calculations
* write comments
* recognize basic syntax errors
* fix missing quotes/parentheses
* understand basic indentation
* predict simple outputs
* build the Wallet v0.1 display
* build the Store v0.1 display

Most importantly:

> **You should understand what your code is doing—not merely copy code that works.**

---

# 🥷 FINAL SENSEI MESSAGE

Apprentice...

Batch 1 taught you to **think before coding**.

Batch 2 taught you to **speak your first Python instructions**.

Don't underestimate these tiny programs.

Every:

```python
print()
```

is another repetition.

Every syntax error you fix is debugging practice.

Every output you predict correctly strengthens your mental model.

And every time you stop and ask:

> "What exactly is Python doing here?"

you are becoming a better programmer.

Soon, you'll stop writing isolated instructions.

You'll start **storing information**.

Then you'll start **transforming information**.

Then you'll make programs **respond to users**.

Then they'll make decisions.

Then they'll repeat work.

Then they'll become systems.

And eventually...

Your 💰 Wallet App and 🛒 Store App will stop being exercises.

They'll become actual software projects that grow alongside you.

But not yet.

For now:

> **Master the small things.**

> **Understand before memorizing.**

> **Predict before running.**

> **Debug before giving up.**

> **Build before calling yourself stuck.**

🐍 **Next target: Batch 3 — Variables & Data.**
