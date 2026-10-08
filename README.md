batch8

🐍 PART 1 — FOUNDATIONS
Batch 8 — Loops & Repetition 🔁

    😎 Alright, apprentice.
    Your programs can now store data, calculate, receive input, work with text, and make decisions.

    But there is one major weakness left:

    Your program gets tired doing the same thing repeatedly. 😂

    Imagine telling Python:

    Print "Hello" 100 times.

    You could write print() 100 times...

    Or you could teach Python how to repeat work for you.

    Welcome to LOOPS. 🔁🐍

🎯 BATCH MISSION

By the end of this batch, you should understand:

    Why loops exist

    while loops

    Loop conditions

    Counters

    Updating loop variables

    Infinite loops

    for loops

    range()

    break

    continue

    Loops + conditionals

    Running totals

    Repeated user input

    Common loop bugs

    How loops upgrade your Wallet App

    How loops upgrade your Store App

And most importantly:

    You should be able to look at a repetitive task and think: "This needs a loop."

🧠 1. THE PROBLEM LOOPS SOLVE

Suppose you want Python to print numbers 1 to 5.

Without a loop:

print(1)
print(2)
print(3)
print(4)
print(5)

That works.

But what if you need:

1 to 100

Or:

1 to 10,000

You don't want to manually write thousands of print() statements.

A loop lets you say:

Python, repeat this instruction.

🔁 2. WHAT IS A LOOP?

A loop is a programming structure that allows code to repeat.

Think of it like this:

START
  ↓
CHECK CONDITION
  ↓
Should I continue?
  ↓
YES ──→ DO SOMETHING
  ↑           ↓
  └── UPDATE ┘
  ↓
CHECK AGAIN
  ↓
NO
  ↓
END

A loop basically tells Python:

    "Keep doing this while the rules say you should."

🧩 3. THE TWO MAIN LOOP TYPES

Python gives us two major loops:

while

and

for

Think of them like this:
Loop	Main Idea
while	Repeat while a condition is true
for	Repeat for a known sequence/range of values

We'll start with while.
🔥 4. THE while LOOP

Basic structure:

while condition:
    # code to repeat

Example:

count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5

🧠 5. BREAKING IT DOWN

Look carefully:

count = 1

We create our starting point.

Then:

while count <= 5:

Python asks:

    Is count <= 5 true?

Since:

1 <= 5

Yes.

So Python executes:

print(count)

Then:

count += 1

Now:

count = 2

Python checks again.

2 <= 5

Still true.

It repeats.

Eventually:

count = 6

Python checks:

6 <= 5

False.

The loop stops.
🔄 6. THE LOOP CYCLE

Our example follows this pattern:

count = 1

       ↓
┌───────────────┐
│ count <= 5 ?  │
└───────┬───────┘
        │
       YES
        ↓
   print(count)
        ↓
   count += 1
        │
        └──────→ CHECK AGAIN

Eventually:

count = 6

6 <= 5 ?

NO

↓
END

This pattern is extremely important.
⚠️ 7. THE DANGER OF INFINITE LOOPS

Look at this:

count = 1

while count <= 5:
    print(count)

What's wrong?

We never change count.

It stays:

1

So Python keeps asking:

Is 1 <= 5?

Yes.

Again.

Yes.

Again.

Yes.

Forever. 😭

This creates an:
♾️ INFINITE LOOP

An infinite loop never reaches its stopping condition.
🛠️ 8. HOW TO AVOID INFINITE LOOPS

Make sure something inside the loop changes the condition.

Correct:

count = 1

while count <= 5:
    print(count)
    count += 1

Incorrect:

count = 1

while count <= 5:
    print(count)

The important idea:

    A while loop needs a path toward its stopping condition.

🧪 EXERCISE 1 — COUNTING

Write a program that prints:

1
2
3
4
5
6
7
8
9
10

Rules

Use:

while

Do not write ten print() statements.
🧪 EXERCISE 2 — COUNTDOWN

Write a program that prints:

10
9
8
7
6
5
4
3
2
1

Then print:

Blast off! 🚀

Hint:

Your counter needs to decrease.

You can use:

count -= 1

🧠 9. LOOP COUNTERS

A counter is simply a variable used to keep track of repetitions.

Example:

count = 1

while count <= 5:
    print("Hello")
    count += 1

Output:

Hello
Hello
Hello
Hello
Hello

The counter controls how many times the loop runs.
🎯 10. LOOP + CONDITIONAL

Loops become much more powerful when combined with if.

Example:

number = 1

while number <= 10:

    if number % 2 == 0:
        print(number)

    number += 1

Output:

2
4
6
8
10

We have combined:

LOOP
  +
CONDITION

This is a major programming pattern.
🧪 EXERCISE 3 — EVEN NUMBERS

Write a program that prints all even numbers from:

1 to 20

Expected:

2
4
6
8
10
12
14
16
18
20

Use:

    while

    %

    if

🧮 11. RUNNING TOTALS

Loops can also repeatedly calculate something.

Suppose we want:

1 + 2 + 3 + 4 + 5

We can use a running total.

number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Total:", total)

Output:

Total: 15

🧠 WHAT HAPPENS?

Initially:

total = 0

Then:

+1 → 1
+2 → 3
+3 → 6
+4 → 10
+5 → 15

So:

Final total = 15

This pattern is extremely important:

START TOTAL
     ↓
GET VALUE
     ↓
ADD VALUE
     ↓
REPEAT
     ↓
FINAL TOTAL

🧪 EXERCISE 4 — SUM NUMBERS

Write a program that calculates:

1 + 2 + 3 + ... + 10

Expected output:

Total: 55

Don't use a built-in sum() function.

Build the total yourself.
🗣️ 12. while + USER INPUT

Now things get interesting.

We can repeatedly ask the user for input.

Example:

count = 1

while count <= 3:

    name = input("Enter your name: ")

    print("Hello", name)

    count += 1

The user gets asked three times.
🧪 EXERCISE 5 — THREE DEPOSITS

Create a program that:

    Starts with:

balance = 10000

    Asks the user for a deposit.

    Adds the deposit to the balance.

    Does this 3 times.

    Prints the final balance.

Example:

Enter deposit: 5000
Enter deposit: 2000
Enter deposit: 3000

Final balance: 20000

🐍 13. THE for LOOP

Now meet Python's other major loop.

Basic structure:

for variable in something:
    # repeated code

For now, we'll use it with range().

Example:

for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5

🧠 14. UNDERSTANDING range()

range() generates a sequence of numbers.
One argument

range(5)

Produces:

0
1
2
3
4

Notice:

It stops before 5.
🔥 IMPORTANT RULE

The ending number is not included.

range(5)

means:

0 → 4

Not:

0 → 5

15. range(start, stop)

Example:

range(1, 6)

Produces:

1
2
3
4
5

Again:

6 is NOT included.

Think:

START → included
STOP  → excluded

16. range(start, stop, step)

You can also specify how much to move each time.

Example:

for number in range(2, 11, 2):
    print(number)

Output:

2
4
6
8
10

Because:

start = 2
stop = 11
step = 2

🧪 EXERCISE 6 — for LOOP

Use a for loop to print:

1
2
3
4
5
6
7
8
9
10

Use:

range()

🧪 EXERCISE 7 — MULTIPLES

Use a for loop to print multiples of 5 from 5 to 50.

Expected:

5
10
15
20
25
30
35
40
45
50

🧠 17. while VS for

Both repeat code, but they are useful in different situations.
while

Use when repetition depends mainly on a condition.

Example:

balance = 10000

while balance > 0:
    print("Balance:", balance)
    balance -= 1000

for

Use when you know the number/range of repetitions.

Example:

for number in range(1, 6):
    print(number)

Simple mental model:

WHILE
"Keep going while this is true."

FOR
"Repeat this for these values."

🛑 18. break

Sometimes you want to stop a loop immediately.

That's what break does.

Example:

count = 1

while count <= 10:

    if count == 5:
        break

    print(count)

    count += 1

Output:

1
2
3
4

When:

count == 5

becomes true:

break

ends the loop.
🧠 VISUAL

1
↓
2
↓
3
↓
4
↓
5
↓
BREAK 🛑
↓
END

🧪 EXERCISE 8 — STOP AT 7

Create a loop that counts from:

1 → 10

But stops when it reaches:

7

Expected:

1
2
3
4
5
6

⏭️ 19. continue

continue does something different.

It means:

    "Skip the rest of this iteration and move to the next one."

Example:

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

Output:

1
2
4
5

When Python reaches:

number == 3

it skips:

print(number)

and moves to the next loop cycle.
🧠 break VS continue

Remember this:

break
   ↓
STOP THE ENTIRE LOOP 🛑

while:

continue
   ↓
SKIP THIS ITERATION ⏭️

🧪 EXERCISE 9 — SKIP 5

Write a for loop that prints numbers:

1 → 10

but skips:

5

Expected:

1
2
3
4
6
7
8
9
10

🧩 20. LOOPS + VALIDATION

Remember validation from Batch 7?

We can combine it with loops.

Suppose a user must enter a positive amount.

amount = 0

while amount <= 0:
    amount = float(input("Enter a positive amount: "))

print("Accepted:", amount)

The program keeps asking until the user enters something valid.

This is a powerful pattern:

ASK
 ↓
CHECK
 ↓
INVALID?
 ↓
ASK AGAIN
 ↓
CHECK AGAIN
 ↓
VALID?
 ↓
CONTINUE

🧪 EXERCISE 10 — VALID PAYMENT

Create a program that repeatedly asks:

Enter payment:

The program should continue asking while the payment is:

0 or negative

Once the user enters a positive number:

Payment accepted

should be printed.
🐛 21. LOOP DEBUGGING LAB

Now we hunt bugs. 😈
BUG #1 — Infinite Loop

count = 1

while count <= 5:
    print(count)

Your task:

Explain:

    Why does it never stop?

    What line is missing?

BUG #2 — Wrong Direction

count = 10

while count >= 1:
    print(count)
    count += 1

This loop never reaches the stopping condition.
Your task:

Fix it.
BUG #3 — Off-by-One

for number in range(1, 5):
    print(number)

The programmer expected:

1
2
3
4
5

But Python prints:

1
2
3
4

Your task:

Fix the range.
BUG #4 — Wrong Indentation

count = 1

while count <= 5:
print(count)
count += 1

Your task:

Fix the indentation.
🧠 22. LOOP PATTERNS YOU SHOULD RECOGNIZE

By now, these patterns should start becoming familiar.
Counting upward

count = 1

while count <= 10:
    print(count)
    count += 1

Counting downward

count = 10

while count >= 1:
    print(count)
    count -= 1

Fixed repetitions

for number in range(5):
    print("Hello")

Running total

total = 0

for number in range(1, 6):
    total += number

print(total)

Repeated input

for number in range(3):
    amount = float(input("Enter amount: "))

Stop early

for number in range(1, 11):

    if number == 6:
        break

    print(number)

💰 23. WALLET APP v0.7

Your Wallet App can now handle repeated transactions.
🎯 Mission

Create a program that starts with:

balance = 10000

Then allow the user to make 5 transactions.

For each transaction:

    Ask for the transaction type:

    deposit

    or:

    withdraw

    Ask for the amount.

    If it's a deposit:

        add to balance.

    If it's a withdrawal:

        check whether the balance is enough.

        subtract if approved.

    After all 5 transactions, display:

Final Balance: ₦...

🧠 WALLET FLOW

START
  ↓
BALANCE
  ↓
TRANSACTION 1
  ↓
UPDATE BALANCE
  ↓
TRANSACTION 2
  ↓
UPDATE BALANCE
  ↓
TRANSACTION 3
  ↓
UPDATE BALANCE
  ↓
TRANSACTION 4
  ↓
UPDATE BALANCE
  ↓
TRANSACTION 5
  ↓
FINAL BALANCE
  ↓
END

You are combining:

VARIABLES
+
INPUT
+
STRINGS
+
OPERATORS
+
CONDITIONALS
+
LOOPS

🔥 That's your first real multi-concept program.
🏪 24. STORE APP v0.7

Now upgrade the Store App.

The store should process 5 products.

For each product:

Enter product price:
Enter quantity:

Calculate:

price × quantity

Then add that product's cost to a running total.

After all 5 products:

Subtotal: ₦...

Then apply the discount rules from Batch 7:

₦100,000+       → 20%
₦50,000–99,999  → 10%
Below ₦50,000   → 0%

Finally display:

Subtotal
Discount
Final Total

🧠 STORE FLOW

START
  ↓
TOTAL = 0
  ↓
PRODUCT 1
  ↓
CALCULATE
  ↓
ADD TO TOTAL
  ↓
PRODUCT 2
  ↓
CALCULATE
  ↓
ADD TO TOTAL
  ↓
...
  ↓
PRODUCT 5
  ↓
CALCULATE
  ↓
ADD TO TOTAL
  ↓
DISCOUNT
  ↓
FINAL TOTAL
  ↓
END

This is where loops start becoming useful in real applications.
🧪 25. CHALLENGE — MINI RECEIPT ENGINE 🧾

Build a program that processes 5 purchases.

For every purchase:

Enter price:
Enter quantity:

Calculate:

item_total = price * quantity

Then keep a running total.

At the end:

========== RECEIPT ==========

Subtotal: ₦XXXXX

Discount: ₦XXXXX

Final Total: ₦XXXXX

=============================

Rules

You must use:

    variables

    input

    float() or int()

    arithmetic operators

    for or while

    if / elif / else

    formatted output

Restrictions

Do not use:

    functions

    lists

    dictionaries

    classes

Those belong to later parts.
😈 26. HARDER CHALLENGE — WALLET GUARD

Create a wallet program that starts with:

Balance = ₦50,000

The user gets up to 5 withdrawal attempts.

For every attempt:

Enter withdrawal amount:

Rules:

    If amount is 0 or negative:

    Invalid amount

    If amount is greater than balance:

    Insufficient funds

    Otherwise:

    Withdrawal approved

    and subtract it.

At the end:

Remaining Balance: ₦...

Bonus

If the user enters:

0

you may use break to end the program.
🧠 27. COMPREHENSION CHECK

Before moving forward, answer these without looking back.
Question 1

What problem do loops solve?
Question 2

What is the difference between:

while

and:

for

?
Question 3

What does this produce?

range(1, 6)

Question 4

Why does this create an infinite loop?

count = 1

while count <= 5:
    print(count)

Question 5

What does this do?

count += 1

Question 6

What is the difference between:

break

and:

continue

?
Question 7

What does % help us determine?
Question 8

Why is this important?

total += amount

⚔️ 28. BATCH 8 SKILL CHECK

Complete these without copying previous solutions.
LEVEL 1 — EASY 🟢
Task 1

Print numbers:

1 → 20

using a for loop.
Task 2

Print:

20 → 1

using a while loop.
LEVEL 2 — MEDIUM 🟡
Task 3

Print all odd numbers between:

1 → 30

Task 4

Calculate:

1 + 2 + 3 + ... + 100

without using sum().
LEVEL 3 — HARD 🟠
Task 5

Ask the user for 5 numbers.

Calculate:

Total

and:

Average

Task 6

Ask the user for 5 product prices.

Calculate the total.

Then apply:

20% discount if total >= 100000
10% discount if total >= 50000
No discount otherwise

LEVEL 4 — BOSS PREP 🔴
Task 7

Build a mini wallet system.

Starting balance:

₦50,000

Allow the user to perform 5 transactions.

Each transaction can be:

deposit
withdraw

Handle:

    deposits

    withdrawals

    insufficient funds

    invalid amounts

    final balance

Use loops and conditionals.
🧪 29. FINAL DEBUGGING TEST

Find the problem:

balance = 10000
count = 1

while count <= 5:

    amount = float(input("Enter withdrawal: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal approved")

    count -= 1

print("Final balance:", balance)

Your mission:

Find why this program does not behave correctly.

Hint:

Look carefully at:

count -= 1

Ask yourself:

    Is count moving toward or away from the loop's stopping condition?

Fix it.
🧠 30. THE BIG IDEA OF BATCH 8

Loops are not about memorizing syntax.

They're about recognizing repetition.

When you see:

Do this.
Do it again.
Do it again.
Do it again.
...

your programmer brain should start asking:

    "Can I turn this into a loop?"

That is the skill we're building.
🏆 BATCH 8 COMPLETION CHECKLIST

You should now be able to:

    Explain why loops exist

    Write a while loop

    Write a for loop

    Create counters

    Increase counters

    Decrease counters

    Explain infinite loops

    Use range()

    Explain start/stop/step

    Remember that range() excludes the stop value

    Combine loops with if

    Create running totals

    Use repeated user input

    Use break

    Use continue

    Debug infinite loops

    Debug off-by-one errors

    Build Wallet App v0.7

    Build Store App v0.7

    Complete the skill check independently

📈 YOUR PROGRESS

PART 1 — PYTHON FOUNDATIONS

Batch 1  ████████████████████ 100% ✅
Batch 2  ████████████████████ 100% ✅
Batch 3  ████████████████████ 100% ✅
Batch 4  ████████████████████ 100% ✅
Batch 5  ████████████████████ 100% ✅
Batch 6  ████████████████████ 100% ✅
Batch 7  ████████████████████ 100% ✅
Batch 8  ████████████████████ 100% 👈

Learning Batches: COMPLETE 🎉

Part 1 Boss Fight: 🔒 LOCKED

🚪 BATCH 8 EXIT CRITERIA

You are ready for the Part 1 Boss Fight when you can:

    Explain while without memorizing a definition.

    Explain for without memorizing a definition.

    Know when to use each.

    Write a loop from scratch.

    Prevent infinite loops.

    Use range() correctly.

    Combine loops and conditionals.

    Track a running total.

    Use break and continue.

    Build the Wallet and Store upgrades without copying the solution.

    Debug a broken loop yourself.

    Complete the Skill Check independently.

🏁 WHAT COMES NEXT?

You've now covered the core foundations:

THINKING
   ↓
PYTHON SYNTAX
   ↓
VARIABLES
   ↓
DATA TYPES
   ↓
OPERATORS
   ↓
INPUT / OUTPUT
   ↓
STRINGS
   ↓
CONDITIONALS
   ↓
LOOPS
   ↓
🔥 PART 1 BOSS FIGHT

The next challenge is different.

There won't be a lesson walking you through every step.

You'll receive a problem.

You'll design the solution.

You'll write the code.

You'll debug it.

You'll explain your decisions.

And Python will have nowhere left to hide. 😈🐍
⚔️ PART 1 BOSS FIGHT — NEXT

Finish Batch 8 exercises and Skill Check first.

Then report your result.

    😎 You've learned how to make Python think. Now we're about to test whether you can make it build.


