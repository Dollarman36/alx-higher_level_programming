#!/usr/bin/python3

""" 4-cities_by_state module """

if __name__ == '__main__':
    import MySQLdb
    import sys

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=inp[1],
                           passwd=inp[2],
                           db=inp[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute('''SELECT cities.id, cities.name, states.name
                FROM cities, states
                WHERE cities.state_id=states.id
                ORDER BY cities.id ASC''')
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
