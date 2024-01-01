$ pylint example_requests.py
************* Module example_requests
example_requests.py:17:11: W0718: Catching too general exception Exception (broad-exception-caught)
example_requests.py:10:15: W3101: Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely (missing-timeout)
example_requests.py:17:4: W0612: Unused variable 'e' (unused-variable)
example_requests.py:21:23: W0621: Redefining name 'status_dict' from outer scope (line 74) (redefined-outer-name)
example_requests.py:32:11: W0718: Catching too general exception Exception (broad-exception-caught)
example_requests.py:24:21: W3101: Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely (missing-timeout)
example_requests.py:54:11: W0718: Catching too general exception Exception (broad-exception-caught)
example_requests.py:54:4: W0612: Unused variable 'e' (unused-variable)
example_requests.py:59:4: W0621: Redefining name 'urls' from outer scope (line 73) (redefined-outer-name)
example_requests.py:63:4: W0621: Redefining name 'status_dict' from outer scope (line 74) (redefined-outer-name)
example_requests.py:65:8: W0612: Unused variable 'i' (unused-variable)
example_requests.py:3:0: C0411: standard import "import random" should be placed before "import requests" (wrong-import-order)
example_requests.py:4:0: C0411: standard import "import re" should be placed before "import requests" (wrong-import-order)

-----------------------------------
Your code has been rated at 7.29/10
