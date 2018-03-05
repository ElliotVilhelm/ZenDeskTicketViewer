## Installation
```
cd ~/
git clone https://github.com/ElliotVilhelm/ZenDeskTicketViewer.git
cd ~/ZenDeskTicketViewer
```
## Execution
```
python3 ticketviewer.py
```
## Description
Simple Ticket Viewer with connects to the Zendesk API. Viewer is able to request all tickets for
an account, display them in a list, and view individual ticket details.

The programs prompt provides four options
1. (V)IEW_ALL - 'v' or 'V' will display all tickets.
2. (T)ICKET_NUMBER - 't' or 'T' will then prompt the user for the ticket number and display the details of the ticket.
3. (F)ETCH - 'f' or 'F' will re-request all tickets updating the current tickets.
4. (E)ND - 'e' or 'E' will end the program.

## Dependencies
* Python3
* Zenpy

### EXAMPLE NORMAL OUTPUT

```
python3 ticketviewer.py < test1.txt
```
<pre>
(V)IEW_ALL (T)ICKET_NUMBER  (F)ETCH (E)ND
Enter Choice: v

Displaying All Tickets!

----------------------------------------
Ticket:  1
Subject:  Im so hungry!
Description Someone please bring me some lunch!
Priority:  None
----------------------------------------


----------------------------------------
Ticket:  2
Subject:  I lost my shoes!
Description Has anyone seen my shoes I lost them!
Priority:  None
----------------------------------------


----------------------------------------
Ticket:  3
Subject:  Im so mad!
Description ahh!
Priority:  None
----------------------------------------



(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: t
Enter Ticket Number: 1

----------------------------------------
Ticket:  1
Subject:  Im so hungry!
Description Someone please bring me some lunch!
ID:  5
Created at:  2018-03-05T22:16:53Z
Type:  None
Priority:  None
----------------------------------------



(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: f
Requesting all tickets

(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: t
Enter Ticket Number: 2

----------------------------------------
Ticket:  2
Subject:  I lost my shoes!
Description Has anyone seen my shoes I lost them!
ID:  4
Created at:  2018-03-05T21:06:17Z
Type:  None
Priority:  None
----------------------------------------


(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: e
Ending Program
</pre>

### EXAMPLE ERROR OUTPUT
#### Invalid Credentials/API Unavailable
<pre>
Error connecting to API
</pre>

### Invalid Choice
```
python3 ticketviewer.py < test2.txt
```
<pre>
(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: Enter Ticket Number:

----------------------------------------
Ticket:  1
Subject:  I lost my shoes!
Description Has anyone seen my shoes I lost them!
ID:  4
Created at:  2018-03-05T21:06:17Z
Type:  None
Priority:  None
----------------------------------------



(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: z
Invalid choice

(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: x
Invalid choice

(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: t
Enter Ticket Number: 2

----------------------------------------
Ticket:  2
Subject:  Im so mad!
Description ahh!
ID:  3
Created at:  2018-03-05T11:29:36Z
Type:  None
Priority:  None
----------------------------------------


(V)IEW_ALL (T)ICKET_NUMBER (F)ETCH (E)ND
Enter Choice: e
Ending Program
</pre>