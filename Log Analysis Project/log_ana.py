#!/usr/bin/python
import psycopg2

datab = 'news'

# What are the most popular three articles of all time?

ques_one = \
    """select articles.title, count(*) as num
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

# Who are the most popular article authors of all time?

ques_two = \
    """select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;"""

# On which days did more than 1% of requests lead to errors?

ques_three = \
    """WITH num_req AS (
              SELECT time::date AS day, count(*)
              from log
              group by time::date
              order by time::date
              ), num_er AS (
                SELECT time::date AS day, count(*)
                from log
                where status != '200 OK'
                group by time::date
                order by time::date
              ), error AS (
                SELECT num_req.day,
                  num_er.count::float / num_req.count::float * 100
                  AS error_pc
                FROM num_req, num_er
                WHERE num_req.day = num_er.day
              )
            SELECT * FROM error WHERE error_pc > 1; """


# using sqlcmmds function to run querys in database.

def sqlcmmds(query):
    try:
        conn = psycopg2.connect(database=datab)
        sql_query = conn.cursor()
        sql_query.execute(query)
        results = sql_query.fetchall()
        conn.close()
        return results
    except:
        print ("Error Message")


# results stored in variable cmd1,cmd2,cmd3.
if __name__ == "__main__":
    cmd1 = sqlcmmds(ques_one)
    cmd2 = sqlcmmds(ques_two)
    cmd3 = sqlcmmds(ques_three)

# results displayed with Ques's.
    print("Most popular articles:\n")
    for count in cmd1:
        print("{} -- {} {}".format(str(count[0]), str(count[1]), 'views'))
    print("-" * 70)
    print("Most popular article authors:\n")
    for count in cmd2:
        print("{} -- {} {}".format(str(count[0]), str(count[1]), 'views'))
    print("-" * 70)
    print("On which days did more than 1% of requests lead to errors:\n")
    for count in cmd3:
        print("{} -- {} {}".format(str(count[0]), str(count[1]), '% errors'))
    print("-" * 70)
