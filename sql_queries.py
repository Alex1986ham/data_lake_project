songs_table_query = ("""
                    SELECT distinct
                    song_id,
                    title as song_title,
                    artist_id,
                    year,
                    duration
                    FROM songs
                    """)

artists_table_query = ("""
                        SELECT distinct
                        artist_id,
                        artist_name,
                        artist_location,
                        artist_latitude,
                        artist_logtitude
                        FROM songs
                        """)

log_filtered_query = ("""
                    SELECT *, cast(ts/1000 as Timestamp) as timestamp from staging_events where pate = 'NextSong'
                    """)

users_query = ("""
                SELECT
                a.userId,
                a.firstName,
                a.lastName,
                a.gender,
                a.level
                FROM staging_events a
                INNER JOIN
                (
                    SELECT
                    userId,
                    max(ts) as ts
                    FROM staging_events
                    GROUP BY
                    userId,
                    page
                ) b
                ON a.userId = b.userId AND a.ts = b.ts
                """)

time_query = ("""
            SELECT distinct
            timestamp as start_time,
            hour(timestamp) as hour,
            day(timestamp) as day,
            weekofyear(timestamp) as week,
            month(timestamp) as month,
            year(timestamp) as year,
            weekday(timestampe) as weekday
            FROM staging_events
            """)

songplays_query = ("""
                    select
                    a.timestamp as start_time,
                    a.userId,
                    a.level,
                    b.song_id,
                    b.artist_id,
                    a.sessionId,
                    a.location,
                    a.userAgent,
                    year(a.timestamp) as year,
                    month(a.timestamp) as month
                    FROM staging_events as a
                    INNER JOIN songs AS b ON a.song = b.song_title
                    """)
