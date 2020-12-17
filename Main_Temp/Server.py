from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db.db_1 import *
from db.db import insert_data, db_selectreviewList, insert_Prom_data, db_selectpromList

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('index.html', name='사용자명')

### 소개 ##############
@app.route('/about')
def about():    
    return render_template('about.html', name='사용자명')


# SubPage######################
@app.route('/food')
def food():    
    return render_template('subpage/food.html', name='사용자명')

@app.route('/cafe')
def cafe():    
    return render_template('subpage/cafe.html', name='사용자명')

@app.route('/enjoy')
def enjoy():    
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
    amt     = 30 if not request.args.get('amt')  else int(request.args.get('amt'))
    rows = db_selectreviewList()
    return render_template('modpage/review/review_r.html', reviews= rows)

@app.route('/ad')
def ad():    
    return render_template('subpage/ad.html', name='사용자명')

@app.route('/game')
def game():    
    return render_template('subpage/game.html', name='사용자명')
########################################

##### map #####
@app.route('/map')
def map():    
    return render_template('modpage/map.html')

@app.route('/map_han')
def map_han():    
    return render_template('modpage/food/map_han.html')

@app.route('/map_yang')
def map_yang():    
    return render_template('modpage/food/map_yang.html')    

@app.route('/map_jung')
def map_jung():    
    return render_template('modpage/food/map_jung.html')  

@app.route('/map_bun')
def map_bun():    
    return render_template('modpage/food/map_bun.html')       

@app.route('/map_enjoy')
def map_enjoy():    
    return render_template('modpage/food/map_enj.html')       

@app.route('/map_chicken')
def map_chicken():    
    return render_template('modpage/food/map_chicken.html')   

@app.route('/map_bread')
def map_bread():    
    return render_template('modpage/food/map_bread.html')

##########################################################
@app.route('/map_cafe_front')
def map_cafe_front():    
    return render_template('modpage/cafe/map_cafe_front.html')

@app.route('/map_cafe_north')
def map_cafe_north():    
    return render_template('modpage/cafe/map_cafe_north.html')

@app.route('/map_cafe_sub')
def map_cafe_sub():    
    return render_template('modpage/cafe/map_cafe_sub.html')

#############_------------------------------------------
@app.route('/map_dang')
def map_dang():    
    return render_template('modpage/enjoy/map_dang.html')

@app.route('/map_pc')
def map_pc():    
    return render_template('modpage/enjoy/map_pc.html')

@app.route('/map_tak')
def map_tak():    
    return render_template('modpage/enjoy/map_tak.html')

@app.route('/map_video')
def map_video():    
    return render_template('modpage/enjoy/map_video.html')    
#############_------------------------------------------


# food #################################
@app.route('/search_food')
def search_food():
        keyword = request.args.get('k')
        rows    = db_selectNameFood(keyword) 
        return jsonify(rows)

@app.route('/food_detail')
def food_detail():
        return render_template( 'subpage/food_detail.html', 
                                r=request.args.get('r'), 
                                food=db_selectFoodByName( name=request.args.get('name') )
        )

# cafe #################################

@app.route('/search_cafe')
def search_cafe():
        keyword = request.args.get('k')
        rows    = db_selectNameCafe(keyword) 
        return jsonify(rows)

@app.route('/cafe_detail')
def cafe_detail():
        return render_template( 'subpage/cafe_detail.html', 
                                r=request.args.get('r'), 
                                cafe=db_selectCafeByName( name=request.args.get('name') )
        )

# enjoy #################################

@app.route('/search_enjoy')
def search_enjoy():
        keyword = request.args.get('k')
        rows    = db_selectNameEnjoy(keyword) 
        return jsonify(rows)

@app.route('/enjoy_detail')
def enjoy_detail():
        return render_template( 'subpage/enjoy_detail.html', 
                                r=request.args.get('r'), 
                                enjoy=db_selectEnjoyByName( name=request.args.get('name') )
        )

########################################
########################################
@app.route('/promote', methods=['GET', 'POST'])
def promote():
    if request.method =='GET': 
        return render_template('subpage/promote.html')
    else:
        promoter = request.form.get('promoter')
        name     = request.form.get('prom_name')
        promote  = request.form.get('promote')
        promoters = insert_Prom_data(promoter, name, promote )

        if promoters:  
            return redirect(url_for('promote')) 
        else:
            return render_template('subpage/alert.html')


@app.route('/promote_r')
def promote_r():
    curPage = 1 if not request.args.get('pageNo')  else int(request.args.get('pageNo'))
    amt     = 30 if not request.args.get('amt')  else int(request.args.get('amt'))
    rows = db_selectpromList()
    return render_template('modpage/promote/promote_r.html', promotes = rows)

#########################################

if __name__ == '__main__':
    app.run(debug=True)