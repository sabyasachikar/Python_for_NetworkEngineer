# Chapter 1 mock data: branch router interface states

This is the same data used inside `scripts/chapter01/interface_audit_demo.py`,
written out here so you can read it as a table and do the Chapter 1 lab by hand
before you run any code.

| Device     | Interface | Admin state | Line state |
|------------|-----------|-------------|------------|
| br-rtr-01  | Gig0/0    | up          | up         |
| br-rtr-01  | Gig0/1    | up          | down       |
| br-rtr-02  | Gig0/0    | up          | up         |
| br-rtr-02  | Gig0/1    | down        | down       |
| br-rtr-03  | Gig0/0    | up          | down       |

Reminder on how to read the two states:

- Admin state is whether someone configured the interface as on (`up`) or shut it off (`down`) on purpose.
- Line state is whether the interface is actually working right now.

An interface that is admin `up` but line `down` is the interesting case. It was
supposed to be working, and it is not. That usually means a cable, a neighbor,
or a fault, and it is worth a look. An interface that is admin `down` was turned
off deliberately, so it is not a surprise and not a problem.
