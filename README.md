# delta_challenge
Delta Challenge (Selenium + Python)

Part I -  See the 'delta_booking_test_case_masterlist' document for detailed  approach broken down into smaller tests.

Part II - See 'manual_test_case_a004' and 'manual_test_case_F010' document.

Part III - See automated test work in the GitHub repo scripts sub-folder or included Selenium python scripts.

Part IV - Attempting to automate a sanity test (SEE atl_to_pbi.py) for searching for initial booking ATL<->PBI but faced issues with SFA001 errors from Delta.
https://www.reddit.com/r/delta/comments/1fvb2cy/persistent_error_sfaf001_trying_to_book_flights/

Challenges Faced:
1. Focusing on smaller step tests vs full interaction, documenting as I go to not loose thought.
2. Delta's website has a lot of dynamic loading, which caused a lot of browser crashing on my setup during Inspections. Also, usage of time.sleep() isn't the best approach. May come back to it if I find a more graceful implementation.
4. Manual testing process took a lot longer in some areas due to it only being accessible after verified login. I had to make a dummy login.
5. For challenges not overcome, I commented out sections and came back to it if I found a better way to tackle it. Also noted in comments as reminder.



