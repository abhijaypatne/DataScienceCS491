import sqlite3

####################################################
# TODO assign [your netid].result to netid variable
####################################################
netid = "apatne2.result"  # suppose your netid is "liu4", the output file should be
                       # liu4.result with extension .result

###########################################
# TODO put database file in the right path
###########################################
social_db = "./data/social.db"
matrix_db = "./data/matrix.db"
university_db = "./data/university.db"

#################################
# TODO write all your query here
#################################
query_1 = "select name from student where grade=9 order by name asc;"
query_2 = "select grade, count(id) as count from student group by grade order by grade asc;"
query_3 = "select a.name, a.grade from student a, friend b where a.id=b.id1 group by a.name, a.grade having count(*)>2 order by a.name, a.grade asc;"
query_4 = "select a.name, a.grade from student a, student a1, likes b where a.id=b.id2 and a1.id=b.id1 and a1.grade>a.grade order by a.name, a.grade asc;"
query_5 = "select name, grade from student where id in (select id1 from likes where id1 not in (select a.id1 from likes a where a.id2 not in (select b.id2 from friend b where b.id1=a.id1))) union select name, grade from student where id not in (select id1 from likes) order by name asc, grade asc;"
query_6 = "select a.id as id1, a.name as name1, b.id as id2, b.name as name2 from student a, student b, likes c where a.id=c.id1 and b.id=c.id2 and a.id not in (select d.id1 from friend d where d.id2=c.id2 and d.id1=a.id) order by a.id asc, b.id asc;"
query_7 = "select temp.id1, s1.name, temp.id2, s2.name, f1.id2, s3.name from (select l.id1,l.id2 from likes l where l.id2 not in ( select f.id2 from friend f where f.id1=l.id1)) temp , friend f1, friend f2 , student s1, student s2, student s3  where temp.id1 = f1.id1 and f1.id2 = f2.id1 and temp.id2=f2.id2 and temp.id1=s1.id and temp.id2=s2.id and f1.id2=s3.id order by temp.id1 asc, temp.id2 asc, f1.id2 asc;"
query_8 = ""
query_9 = "select tenured, avg(class_Score) from dim_professor, fact_course_evaluation where professor_id=id group by tenured;"
query_10 = "select year, area, avg(class_score) as avg_score from dim_type type, dim_term term, fact_course_evaluation fact where term.id=fact.term_id and fact.type_id=type.id group by term.year, type.area order by term.year asc, type.area asc;"
query_11 = "select a.row_num, b.col_num, sum( a.value * b.value ) from a, b where a.col_num=b.row_num group by a.row_num, b.col_num order by a.row_num asc, b.col_num asc;"

################################################################################

def get_query_list():
    """
    Form a query list for all the queries above
    """
    query_list = []
    ## TODO change query number here
    for index in range(1,12):
        eval("query_list.append(query_" + str(index) + ")")
    # end for
    return query_list
    pass

def output_result(index, result):
    """
    Output the result of query to facilitate autograding.
    Caution!! Do not change this method
    """
    with open(netid, 'a') as fout:
        fout.write("<"+str(index)+">\n")
    with open(netid, 'a') as fout:
        for item in result:
            fout.write(str(item))
            fout.write('\n')
        #end for
    #end with
    with open(netid, 'a') as fout:
        fout.write("</"+str(index) + ">\n")
    pass

#def run():
    ## get all the query list
query_list = get_query_list()
    ## problem 1
conn = sqlite3.connect(social_db)
cur = conn.cursor()
for index in range(0, 7): # TODO query 1-8 for problem 1
	cur.execute(query_list[index])
	result = cur.fetchall()
	tag = "q" + str(index+1)
	output_result(tag, result)
    #end for
    ## TODO problem 2
    
	## problem 2
	
conn = sqlite3.connect(university_db)
cur = conn.cursor()
for index in range(8, 10): # TODO query 1-8 for problem 1
	cur.execute(query_list[index])
	result = cur.fetchall()
	tag = "q" + str(index+1)
	output_result(tag, result)
#end for
## TODO problem 3
## problem 1
conn = sqlite3.connect(matrix_db)
cur = conn.cursor()
#for index in range(10): # TODO query 1-8 for problem 1
cur.execute(query_list[10])
result = cur.fetchall()
tag = "q" + str(index+1)
output_result(tag, result)
    #end for
    #end run()

