class schema:

    # countries table schema
    Country_Table = '''CREATE TABLE if not Exists countries(
      country_id int PRIMARY KEY NOT NULL,
      country_name TEXT NOT NULL
    )
    '''

    # states table schema
    State_Table = '''CREATE TABLE if not Exists states(
        state_id int PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        country_id int NOT NULL,
        country_name TEXT NOT NULL,
        FOREIGN KEY (country_id) REFERENCES countries (country_id)
      )'''

    # cities table schema
    City_Table = '''CREATE TABLE if not Exists cities(
    city_id int PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    state_id int NOT NULL,
    country_id int NOT NULL,
    country_name TEXT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (state_id),
    FOREIGN KEY (country_id) REFERENCES countries (country_id)
  )'''
