from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db.db_1 import *

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

@app.route('/review')
def review():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('subpage/review.html', name='사용자명')

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

# food #################################
@app.route('/search')
def search():
        keyword = request.args.get('k')
        rows    = db_selectNameFood(keyword) 
        return jsonify(rows)

@app.route('/food_detail')
def food_detail():
        return render_template( 'subpage/food_detail.html', 
                                r=request.args.get('r'), 
                                food=db_selectFoodByName( name=request.args.get('name') )
        )

########################################

if __name__ == '__main__':
    app.run(debug=True)