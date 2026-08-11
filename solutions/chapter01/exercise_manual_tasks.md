# Sample answer: five manual tasks worth automating

Your list will be different, and that is the point. Here is an example to show the
level of detail that is useful. Notice that each task is broken into the small steps
you actually perform, because those steps are what a script will one day carry out.

1. Morning interface check.
   - SSH into each router.
   - Run the command that shows interface status.
   - Read the output and note any interface that should be up but is down.
   - Move to the next router.

2. Nightly configuration backup.
   - SSH into each device.
   - Show the running configuration.
   - Copy the output into a file named with the device and the date.
   - Store the file somewhere safe.

3. Checking BGP neighbors after a change.
   - SSH into each affected router.
   - Show the BGP summary.
   - Confirm every neighbor is established.
   - Flag any that are not.

4. Creating a VLAN across access switches.
   - SSH into each switch.
   - Enter configuration mode.
   - Add the VLAN and its name.
   - Save the configuration.

5. Validating an addressing plan before a rollout.
   - Open the planning spreadsheet.
   - Check each address is well formed and inside the right subnet.
   - Check for duplicates.
   - Mark any bad entries.

## Which one first, and how would you check it

A good pick is the morning interface check, because it happens every day and the
steps are identical each time. You would know the automation worked if, run against a
known-good lab first, it reports the interfaces you already know are down and none
that are actually up. That is your test before you ever point it at production.
