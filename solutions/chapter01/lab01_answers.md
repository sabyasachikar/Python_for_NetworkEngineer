# Lab 1.1 answers

## Part A

1. There are five interfaces in total.
2. Administratively up but line down: `br-rtr-01 Gig0/1` and `br-rtr-03 Gig0/0`.
3. The one that is down on purpose is `br-rtr-02 Gig0/1`, which is admin down.
   It should not be flagged.
4. Times will vary. The point is that reading three routers is quick, but the
   effort grows in a straight line with the number of devices and interfaces.
   Fifty routers with twelve interfaces each is six hundred lines to scan by
   eye, every morning. Common mistakes are skipping a line, misreading up as
   down, and flagging an interface that was shut on purpose.

## Part B

1. `interface_status` is a list of dictionaries. Each dictionary is one
   interface, with its device, name, admin state, and line state.
2. `find_down_links` keeps only the interfaces where admin is `up` and line is
   `down`. That is the exact rule you applied by hand.
3. For each problem interface it prints the device, the interface name, and both
   states, one per line.

## Part C

Running the script prints two problem interfaces, `br-rtr-01 Gig0/1` and
`br-rtr-03 Gig0/0`, which matches your hand answers.
