from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db.db_1 import db_selectNameFood
from db.db import insert_data, db_selectreviewList

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('index.html', name='사용자명')

### 소개 ##############
@app.route('/about')
def about():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('about.html', name='사용자명')

 

# SubPage######################
@app.route('/food')
def food():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('subpage/food.html', name='사용자명')

@app.route('/cafe')
def cafe():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('subpage/cafe.html', name='사용자명')

@app.route('/enjoy')
def enjoy():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('subpage/enjoy.html', name='사용자명')

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method =='GET': 
        return render_template('subpage/review.html')
    else:
        reviewer = request.form.get('reviewer')
        name     = request.form.get('name')
        star     = request.form.get('star')
        menu     = request.form.get('menu')
        price    = request.form.get('price')
        review   = request.form.get('review')
        reviews = insert_data(reviewer, name, star, menu, price, review )

        if reviews:  
            return redirect(url_for('review')) 
        else:
            return render_template('subpage/alert.html')

@app.route('/review_r')
def review_r():
    curPage = 1 if not request.args.get('pageNo')  else int(request.args.get('pageNo'))
    amt     = 5 if not request.args.get('amt')  else int(request.args.get('amt'))
    rows = db_selectreviewList()
    return render_template('modpage/review/review_r.html', reviews= rows)

@app.route('/ad')
def ad():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('subpage/ad.html', name='사용자명')

@app.route('/game')
def game():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('subpage/game.html', name='사용자명')
########################################

#####map#####
@app.route('/map_cafe')
def map_cafe():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('modpage/cafe/map_cafe.html')





# food #################################
@app.route('/search')
def search():
        keyword = request.args.get('k')
        rows    = db_selectNameFood(keyword) 
        return jsonify(rows)


########################################


if __name__ == '__main__':
    app.run(debug=True)