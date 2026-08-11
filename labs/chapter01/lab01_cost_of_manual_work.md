# Lab 1.1: Count the Cost of Manual Work

This is a thinking lab. It needs no computer and no code. The point is to feel, in
numbers, why automation is worth learning before you write a single line of Python.

## Objective

Estimate the time and error cost of a manual daily check, and compare it to an
automated one.

## Network scenario

Every morning your team checks that the WAN interface is up on each branch router.

## Prerequisites

None. Bring a pen.

## Steps

1. Suppose you have 60 branch routers, and it takes about 45 seconds to log in, run
   one command, read the result, and log out of each one. How long does the full
   manual check take each morning?
2. Over a five-day week, how much time is that?
3. People make small mistakes when doing the same thing over and over. If you misread
   just one router in fifty, roughly how many misreads might you make across a month
   of daily checks (about 20 working days)?
4. Now assume an automated check runs in about 30 seconds for all 60 routers and
   never misreads. How much time does it save per week?
5. Write two or three sentences on what you would do with the time saved.

## Expected result

Rough numbers are fine. The manual check is about 45 minutes a day, close to four
hours a week. The automated check is under a minute. The saving is large, and the
misread rate on the reading step drops to zero.

## Verification

You have a per-week time saving and a clear sense of how errors grow as a manual
task is repeated.

## Student exercise

List five tasks you do by hand today that you would like to automate. For each one,
write down the manual steps you follow. Keep this list. As the course goes on you
will build tools for several of them. A sample answer is in
`solutions/chapter01/exercise_manual_tasks.md`.

## Challenge

From your list, pick the task that would save the most time if automated, and write
down how you would know the automation worked correctly. Thinking about how to check
the result, before you build anything, is a habit that separates safe automation
from risky automation.
