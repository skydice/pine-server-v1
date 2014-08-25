Version management
==================


v 1.0.2 latest version update.
------------------------------
**Update**
  * add `type` key in APIs.
        
- Get latest timeline                                      [/timeline/friends?count={count}]
- Get next threads in timeline starting from offset thread [/timeline/friends/since_offset?offset_id={offset_id}&count={count}]
- Get friend's timeline previous offset                    [/timeline/friends/previous_offset?offset_id={offset_id}&count={count}]      
- Get thread                                               [/threads/<thread_id>]



### v 1.0.1 update.
**Update**
  * add event_date in ios push message. (need to test)
  * add `image_url` key in ios push json.
  
        "aps": {
            "alert": (message, String),
            "badge": 1,
        },
        'thread_id': (int),
        'event_date': 'YYYY-mm-dd HH:MM:SS',
        'image_url': (String)

**Bug fixed**
  * thread, comment notification error.
