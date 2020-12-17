import pymysql as my

def db_review( reviewer, name, star, menu, price, review ):
    conn = None
    row  = None 

    try:
        conn= my.connect(   host    ='localhost',                    
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                INSERT INTO reviews VALUES ({},{},{},{},{},{} ) 
                '''.format(reviewer, name, star, menu, price, review )

            cursor.execute(sql, ( reviewer, name, star, menu, price, review ))
            row =cursor.fetchone()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

def create_table():
     try: 
        conn= my.connect(   
                host    ='localhost',                    
                user    ='root',
                password='12341234',
                port    = 3306,
                db      ='python_db',
                charset ='utf8mb4',
                cursorclass=my.cursors.DictCursor
            )
        with conn.cursor( ) as cursor:
            sql ="""
            CREATE TABLE reviews (reviewer varchar(50), name varchar(50), star int(10),
            menu varchar(50), price int(11), review varchar(50))
            """
            cursor.execute(sql)
            conn.commit()
     except Exception as e: 
        print('db error:', e) 
     finally: 
        conn.close()

def insert_data( reviewer, name, star, menu, price, review ): 
    result = 0
    try: 
        conn= my.connect(   
            host    ='localhost',                    
            user    ='root',
            password='12341234',
            port    = 3306,
            db      ='python_db',
            charset ='utf8mb4',
            cursorclass=my.cursors.DictCursor
        ) 
        c = conn.cursor( ) 
        # sql ='''
        #     INSERT INTO reviews VALUES ({},{},{},{},{},{} ) 
        #     '''.format(reviewer, name, star, menu, price, review )
        setdata = (reviewer, name,  menu, review )
        print( setdata )
        sql = "INSERT INTO reviews VALUES ('%s','%s',%s,'%s',%s,'%s' )" % (reviewer, name, star, menu, price, review)
        print( sql )
        c.execute(sql) 
        conn.commit() 
        result = conn.affected_rows()
    except Exception as e: 
        print('db error:', e) 
    finally: 
        conn.close()
    return result



def insertDataBusan(  reviewer, name, star, menu, price, review ):
    try:
        sql = "insert into famous values(:reviewer, :name, :star, :menu, :price, :review)" # 입력될 테이블명선언
        conn= my.connect(   
                    host    ='localhost',                    
                    user    ='root',
                    password='12341234',
                    port    = 3306,
                    db      ='python_db',
                    charset ='utf8mb4',
                    cursorclass=my.cursors.DictCursor
                ) 
        cur = conn.cursor()
        cur.execute( sql, ( reviewer, name, int(star), menu, int(price), review) )
        conn.commit()
        conn.close()
    except Exception as err:
        print('err:',err)
        return '입력에 실패했습니다'


def db_selectreviewList( curPageId=1 , onePage_dataNum=10 ):
    conn = None
    rows  = None 

    try:
        conn= my.connect(   host    ='localhost',  
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                SELECT * FROM reviews LIMIT %s, %s;
                '''
            amt       = onePage_dataNum
            srartPage = (curPageId - 1 )*amt
            cursor.execute(sql, ( srartPage, amt ))
            rows =cursor.fetchall()
            # 결과를 다 가져와라
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows

#########################################3


def insert_Prom_data( promoter, name, promote ): 
    result = 0
    try: 
        conn= my.connect(   
            host    ='localhost',                    
            user    ='root',
            password='12341234',
            port    = 3306,
            db      ='python_db',
            charset ='utf8mb4',
            cursorclass=my.cursors.DictCursor
        ) 
        c = conn.cursor( ) 
        # sql ='''
        #     INSERT INTO reviews VALUES ({},{},{},{},{},{} ) 
        #     '''.format(reviewer, name, star, menu, price, review )
        setdata = (promoter, name, promote )
        sql = "INSERT INTO promotes VALUES ('%s','%s','%s' )" % (promoter, name, promote )
        c.execute(sql) 
        conn.commit() 
        result = conn.affected_rows()
    except Exception as e: 
        print('db error:', e) 
    finally: 
        conn.close()
    return result


def db_selectpromList( curPageId=1 , onePage_dataNum=10):
    conn = None
    rows  = None 

    try:
        conn= my.connect(   host    ='localhost',  
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                SELECT * FROM promotes LIMIT %s, %s;
                '''
            amt       = onePage_dataNum
            srartPage = (curPageId - 1 )*amt
            cursor.execute(sql, ( srartPage, amt ))
            rows =cursor.fetchall()
            # 결과를 다 가져와라
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows


####################################