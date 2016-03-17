# oDesk-pymongo-SkillRecommend

The code essentially does the following:

**1.** Acquires data by accessing the oDesk REST API using python-oDesk API wrappers.<br>
**2.** Inserts the raw json responses into MongoDB document collection using pymongo framework.<br>
**3.** Identifies key skills a person should learn to get more work, or to work at a higher rate.

`odesk_api.py` does **1.**<br>
`oDesk_pymongo_queries.py` does **2.** and **3.**<br>
`DATA.zip` has the raw json responses.

Getting Started: Refer to [odesk/python-odesk](https://github.com/odesk/python-odesk) (Now deprecated..)<br>
Python Package Requirements: nose, mock, oauth2, urllib3

### **Future Work:**
* Employ Natural Language Processing to see what profile elements are most effective.
