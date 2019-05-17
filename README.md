SPARKIFY DATAMART
=================
Purpose : 
This datamart is built for catering to the needs of the Analysis team in the startup company "SPARKIFY". 
Business needs to know the below key information generated from the new music streaming app for Sparkify.
    => Metadata for Songs being played
    => User-activity on the app.

SOURCE 
======
Source of data in these tables are JSON logs generated from app based on user activity.
Two feeds into the process are -
    => SONG_DATA formatted as JSON logs
    => LOG_DATA formatted as JSON logs

TARGET
======
The two JSON files ('song metadata' & 'log data of user activity') are read and loaded into below tables.
    DIMENSION TABLES - 
        'SONGS' 
        'USERS'
        'ARTISTS'
        'TIME' 
    FACT TABLE 
        'SONGPLAYS'

DATA MODEL
==========
    DIMENSION TABLES
    ================
        SONG_DATA feed contains information about the SONG and ARTISTS (i.e. song metadata). 
                Hence, these two information are loaded into separate DIMENSIONAL tables in SONGS & ARTISTS tables respectively.
            =>SONGS table holds below attributes :
                    song_id, song_title, artist, song_year, duration
            =>ARTISTS table holds below attributes :
                    artist_id, artist_name, location, latitude, longitude

        LOG_DATA feed contains information about user-activity in the app. 
                Hence, the information in this are loaded into two separate DIMESNTIONAL tables in TIME & USERS & SONGPLAYS tables respectively.
            => USERS table holds below attributes :
                    user_id, first_name, last_name, gender, level
            => TIME table holds below attributes :
                    start_time, hour, day, week, month, year, weekday

    FACT TABLE
    ==========
        SONGPLAYS table - This is a FACT table. Data is extracted from the LOG_DATA feed with lookup information 
                pulled from SONGS & ARTISTS dimensional tables.
            => This table holds below attributes available for analysis team for analysis.
                songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

ETL PIPELINE
=============
This ETL pipeline is to load SONG_DATA & LOG_DATA feeds into the tables detailed above.
This process is accomplished with below steps -
    => PROCESS_DATA function in the generic function that is used to process both the feeds... SONG_DATA & LOG_DATA
        This is achieved by passing FILEPATH & CORRESPONDING_FUNCTION as parameters to this function.  
        This calls wither PROCESS_SONG_FILE or PROCESS_LOG_FILE based on the parameters passed.
    => PROCESS_SONG_FILE function
        This browse through all the files in the path (song data), and does ETL of all JSON data into the 
        tables SONGS & ARTISTS mentioned above
            => For every JSON file read, required attributes are extracted, and the respective INSERT query is
               executed  (SONGS & ARTISTS)
    => PROCESS_LOG_FILE function
        This browse through all the files in the path (log data), and does ETL of all JSON data into the 
        tables USERS & TIME & SONGPLAYS tables.
            => For every JSON file read, required attributes are extracted, and respective INSERT uqery is
               executed (USERS & TIME)
            => USERS & TIME tables are first loaded in separate loop (using ITERROWS function)
            => Then in another LOOP through the log data files, SONGPLAY related attributes are extracted 
               with lookup information done to SONGS & ARTISTS table, so we are complaint with 3NF
               as part of NORMALIZATION.
              
FILES USED
==========
(1) sql_queries.py       => This holds drop/create/insert statements for POSTGRES tables
(2) create_tables.py     => This drop/create SPARKIFY database in which DDL/DML statements mentioned in 'sql_queries.py' are utilized.
(3) etl.py               => This contains python code that helps perform the ETL of JSON logs in DATASET to load into the target-tables.

HOW TO RUN
==========
(1) Run the 'create_tables.py' first to setup the DATABASE SPARKIFY and DROP/CREATE the dimension/fact tables defined in the project.
(2) After (1) is done, execute 'etl.py' to extract-transform-load the JSON dataset. After successful run of 'etl.py' data will be available in the target tables in POSTGRES.

THANKS
======
To the slack community and Mentor FARHAD for guiding during the project development, and help accomplish successful completion of the DATAMART. Special thanks to UDACITY for providing me an excellent platform to learn quick.
