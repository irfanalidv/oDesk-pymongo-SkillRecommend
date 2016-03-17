# oDesk-pymongo-SkillRecommend

1. Acquired data by accessing the oDesk REST API using python-oDesk API wrappers.
2. Inserted the raw json responses into MongoDB document collection using pymongo framework.
3. Identified key skills a person should learn to get more work, or to work at a higher rate.

`odesk_api.py` does 1.<br>
`oDesk_pymongo_queries.py` does 2. and 3.<br>
`DATA.zip` has the raw json responses.<br>

Getting Started: Refer to [odesk/python-odesk](https://github.com/odesk/python-odesk)<br>
Python Package Requirements: nose, mock, oauth2, urllib3

**Future Work**
*Employ Natural Language Processing to see what profile elements are most effective.
