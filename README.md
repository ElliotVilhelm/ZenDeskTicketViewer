## Execution
```
python3 ticketviewer.py
```
## Description
Simple Ticket Viewer with connects to the Zendesk API. Viewer is able to request all tickets for
an account, display them in a list, and view individual ticket details.

## Dependencies
* Python3
* Zenpy


### EXAMPLE NORMAL OUTPUT

```
python3 ticketviewer.py < test1.py
```
<pre>
(V)IEW_ALL (T)ICKET_NUMBER (E)ND
Enter Choice: v
Displaying All Tickets!

----------------------------------------
Ticket:  1
Subject:  I lost my shoes!
Description Has anyone seen my shoes I lost them!
Priority:  None
----------------------------------------


----------------------------------------
Ticket:  2
Subject:  Im so mad!
Description ahh!
Priority:  None
----------------------------------------


----------------------------------------
Ticket:  3
Subject:  Sample ticket: Meet the ticket
Description Hi Elliot,

Emails, chats, voicemails, and tweets are captured in Zendesk Support as tickets. Start typing above to respond and click Submit to send. To test how an email becomes a ticket, send a message to support@elliotvilhelm.zendesk.com.

Curious about what your customers will see when you reply? Check out this video:
https://demos.zendesk.com/hc/en-us/articles/202341799

Priority:  normal
----------------------------------------



(V)IEW_ALL (T)ICKET_NUMBER (E)ND
Enter Choice: t
Enter Ticket Number: 1

----------------------------------------
Ticket:  1
Subject:  I lost my shoes!
Description Has anyone seen my shoes I lost them!
ID:  4
Created at:  2018-03-05T21:06:17Z
Type:  None
Priority:  None
----------------------------------------



(V)IEW_ALL (T)ICKET_NUMBER (E)ND
Enter Choice: e
Ending Program
</pre>

### EXAMPLE ERROR OUTPUT
#### Invalid Credentials/API Unavailable
<pre>
Error connecting to API
</pre>

#### Invalid Choice
```
python3 ticketviewer.py < test2.txt
```
<pre>
(V)IEW_ALL (T)ICKET_NUMBER (E)ND (F)ETCH
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



(V)IEW_ALL (T)ICKET_NUMBER (E)ND (F)ETCH
Enter Choice: z
Invalid choice

(V)IEW_ALL (T)ICKET_NUMBER (E)ND (F)ETCH
Enter Choice: x
Invalid choice

(V)IEW_ALL (T)ICKET_NUMBER (E)ND (F)ETCH
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


(V)IEW_ALL (T)ICKET_NUMBER (E)ND (F)ETCH
Enter Choice: e
Ending Program
</pre>