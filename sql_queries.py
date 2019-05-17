# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
                                        (songplay_id SERIAL PRIMARY KEY,           
                                         start_time TIME NOT NULL,                             
                                         user_id int NOT NULL,                                 
                                         level varchar,                                        
                                         song_id varchar,                                      
                                         artist_id varchar,                                    
                                         session_id varchar NOT NULL,                          
                                         location varchar,                                     
                                         user_agent varchar,
                                         CONSTRAINT pk_tmusrses_id 
                                         UNIQUE (start_time, user_id, session_id)
                                        )
                         """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
                                    (user_id int PRIMARY KEY, 
                                     first_name	varchar, 
                                     last_name varchar, 
                                     gender char(1), 
                                     level varchar
                                    )
                     """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
                                    (song_id varchar PRIMARY KEY, 
                                     title varchar, 
                                     artist_id varchar, 
                                     year int, 
                                     duration numeric 
                                    )
                     """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
                                      (artist_id varchar PRIMARY KEY, 
                                       artist_name varchar, 
                                       location varchar, 
                                       latitude numeric, 
                                       longitude numeric
                                      )
                       """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
                                    (start_time time PRIMARY KEY, 
                                     hour int, 
                                     day int,
                                     week int, 
                                     month int, 
                                     year int, 
                                     weekday int
                                    )
                     """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays 
                                 (start_time,
                                  user_id,
                                  level,
                                  song_id,
                                  artist_id,
                                  session_id,
                                  location,
                                  user_agent)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s) 
                            ON CONFLICT (start_time, user_id, session_id) 
                            DO NOTHING
                         """)

user_table_insert = ("""INSERT INTO users 
                              (user_id,
                               first_name,
                               last_name,
                               gender,
                               level)
                        VALUES (%s,%s,%s,%s,%s) 
                        ON CONFLICT (user_id) 
                        DO UPDATE SET level = EXCLUDED.level """)

song_table_insert = ("""INSERT INTO songs 
                             (song_id,
                              title,
                              artist_id,
                              year,
                              duration) 
                         VALUES (%s,%s,%s,%s,%s) 
                         ON CONFLICT (song_id) 
                         DO NOTHING 
                     """)

artist_table_insert = ("""INSERT INTO artists 
                             (artist_id,
                              artist_name,
                              location,
                              latitude,
                              longitude)
                          select distinct artist_id, 
                              artist_name, 
                              artist_location, 
                              artist_latitude, 
                              artist_longitude 
                            from stg_songs
                       """)

time_table_insert = ("""INSERT INTO time 
                             (start_time,
                              hour,
                              day,
                              week,
                              month,
                              year,
                              weekday)
                        VALUES (%s,%s,%s,%s,%s,%s,%s) 
                        ON CONFLICT (start_time) 
                        DO NOTHING
                     """)

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id 
                    FROM songs as s
                    LEFT JOIN artists as a ON a.artist_id = s.artist_id
                   WHERE title = %s AND artist_name = %s AND duration=%s
               """)

# QUERY LISTS

create_table_queries = [songplay_table_create, 
                        user_table_create, 
                        song_table_create, 
                        artist_table_create, 
                        time_table_create
                       ]
drop_table_queries = [songplay_table_drop, 
                      user_table_drop, 
                      song_table_drop, 
                      artist_table_drop, 
                      time_table_drop
                     ]
