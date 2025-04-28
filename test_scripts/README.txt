The scripts are designed to work leveraging Selenium with Python.
Execute directly in command prompt or console.
Ensure you have Python, Selenium WedDriver, and ChromeDriver installed. See docs folder for details on setup.

atl_to_pbi.py - Attempting to automate happy flow for searching for flight from ATL to PBI, the calendar datpicker was giving me a hard time focusing on the current day. First methods I tried didnt work, I comment it out and tried a more brut force way with key presses that seemed to work a few times then didnt. Not sure why.
Even when the solution worked a few times, I got a SFA001 error from Delta's site.

delta_login_a004.py - Log in to Delta with valid credentials. This seems to work but the end validation isnt 100% correct. Validation by URL didnt seem to work so I tried to find a focusable element that only would show if you had sucessfully logged in.
