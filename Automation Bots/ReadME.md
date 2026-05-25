To make it completely *seamless** here is how the bot works.

**my_bot_project**/          **<-- Your main project folder**
│
├── .git\              **<-- Hidden folder that tracks changes (Git initializes this)**\
├── auto_uploader.py\     **<-- The Python automation script we just looked at**\
└── bot.py\               **<-- Your actual Discord bot code**

or simply\

[ Your Local Project Folder ]\ 
                │
                ▼  (Step 1: git add .)\
       [ The Staging Area ]\
                │
                ▼  (Step 2: git commit)\
     [ Your Local Git History ]\
                │
                ▼  (Step 3: git push)\
       [ GitHub Repository ]\
