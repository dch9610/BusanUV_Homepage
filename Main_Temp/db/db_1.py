import pymysql as my

# 음식점 #####################################################################

def db_selectNameFood( keyword ):
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
            # 파라미터를 무조건 execute()를 통해서 넣을 필요는 없다
            sql ='''
                SELECT * FROM food WHERE 분류 like '%{}%' ORDER BY 가게명 asc;
            '''.format(keyword)
            cursor.execute(sql)
            rows =cursor.fetchall()
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows

# 가게명을 넣어서 해당 가게 1개의 상세 정보를 가져온다
def db_selectFoodByName( name ):
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
                    SELECT * FROM food WHERE 가게명 = %s; 
            '''
            cursor.execute(sql, name)
            row =cursor.fetchone()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

# 가게명을 넣어서 해당 해당 가게의 리뷰를 가져온다
def db_selectFoodReviewByName( name ):
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
                    SELECT * FROM reviews WHERE name = %s; 
            '''
            cursor.execute(sql, name)
            rows =cursor.fetchall()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows


# 카페 #####################################################################

def db_selectNameCafe( keyword ):
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
            # 파라미터를 무조건 execute()를 통해서 넣을 필요는 없다
            sql ='''
                SELECT * FROM cafe WHERE 분류 like '%{}%' ORDER BY 가게명 asc;
            '''.format(keyword)
            cursor.execute(sql)
            rows =cursor.fetchall()
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows

# 가게명을 넣어서 해당 가게 1개의 상세 정보를 가져온다
def db_selectCafeByName( name ):
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
                    SELECT * FROM cafe WHERE 가게명 = %s; 
            '''
            cursor.execute(sql, name)
            row =cursor.fetchone()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

# 가게명을 넣어서 해당 해당 가게의 리뷰를 가져온다
def db_selectCafeReviewByName( name ):
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
                    SELECT * FROM reviews WHERE name = %s; 
            '''
            cursor.execute(sql, name)
            row =cursor.fetchall()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

# 놀거리 #####################################################################

def db_selectNameEnjoy( keyword ):
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
            # 파라미터를 무조건 execute()를 통해서 넣을 필요는 없다
            sql ='''
                SELECT * FROM enjoy WHERE 분류 like '%{}%' ORDER BY 가게명 asc;
            '''.format(keyword)
            cursor.execute(sql)
            rows =cursor.fetchall()
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows

# 가게명을 넣어서 해당 가게 1개의 상세 정보를 가져온다
def db_selectEnjoyByName( name ):
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
                    SELECT * FROM enjoy WHERE 가게명 = %s; 
            '''
            cursor.execute(sql, name)
            row =cursor.fetchone()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

# 가게명을 넣어서 해당 해당 가게의 리뷰를 가져온다
def db_selectEnjoyReviewByName( name ):
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
                    SELECT * FROM reviews WHERE name = %s; 
            '''
            cursor.execute(sql, name)
            row =cursor.fetchall()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row