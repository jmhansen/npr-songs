from peewee import PostgresqlDatabase

database = PostgresqlDatabase(
    database='npr_songs_local',
    user='postgres',
    host='127.0.0.1'
)