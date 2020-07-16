from flask.app import Flask
import pyrebase
from flask.globals import request
from flask.templating import render_template
import jinja2
from logging import addLevelName
app = Flask(__name__)
app.jinja_env.add_extension(jinja2.ext.do)

firebaseConfig = {
  'apiKey': "AIzaSyDKaQFT-Q3Ra9HhkOCtNfR2G6t5CaXIVa4",
  'authDomain': "dream-prediction-b1f7b.firebaseapp.com",
  'databaseURL': "https://dream-prediction-b1f7b.firebaseio.com",
  'projectId': "dream-prediction-b1f7b",
  'storageBucket': "dream-prediction-b1f7b.appspot.com",
  'messagingSenderId': "305120582997",
  'appId': "1:305120582997:web:21e09d5c32971d8da063dc",
  'measurementId': "G-HHLF9446QC"
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

Id,Name,Age,Gender,Choose=0,"","-1","",""
Attitude_8,Education_8,Games_8,Eca_8,Time_8="","","","",""
Attitude_9,Education_9,Games_9,Eca_9,Time_9="","","","",""
Attitude_10,Education_10,Games_10,Eca_10,Time_10="","","","",""
Attitude_11,Education_11,Games_11,Eca_11,Time_11="","","","",""
Attitude_12,Education_12,Games_12,Eca_12,Time_12="","","","",""


    
@app.route("/home")
def fun1():
    return render_template("home.html")

@app.route("/contact")
def fun2():
    return render_template("contact.html")

@app.route("/predict")
def fun3():
    return render_template("ip_form08.html")

@app.route("/output")
def fun4():
    return render_template("sam_output.html")

@app.route("/college")
def fun5():
    return render_template("college_list.html")

@app.route("/about")
def fun6():
    return render_template("about_us.html")

@app.route("/pre_ip_08")
def fun12():
    return render_template("ip_form08.html")

@app.route("/pre_ip_09")
def fun13():
    return render_template("ip_form09.html")

@app.route("/pre_ip_10")
def fun14():
    return render_template("ip_form10.html")

@app.route("/pre_ip_11")
def fun15():
    return render_template("ip_form11.html")

@app.route("/re_contact")
def fun17():
    return render_template("contact.html")

@app.route("/contact_auth",methods=['POST','GET'])
def fun16():
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        country=request.form['country']
        conte=request.form['subject']
        if(fname=="" or conte==""):
            return render_template("iv_contact.html")
        else:
            db.child('Feedback').child(fname+lname).push({'fname':fname,'lname':lname,'country':country,'subject':conte})
            return render_template("sub_contact.html")

@app.route("/find_col",methods=['POST'])
def fun7():
    addr=str(request.form['district'])
    dept=str(request.form['course'])
    
    a=db.child('college').get()
    detail=[]
    v=list(a.val().items())
    #print(list(a.val().items()))
    for i in v:
        c=list(i[1].values())[0]
        detail.append(c)
        
    #detail=db.session.query(college.name,college.address,college.dept_1,college.dept_2,college.dept_3,college.dept_4,college.dept_5,college.dept_6,college.dept_7,college.dept_8,college.dept_9,college.dept_10,college.dept_11,college.dept_12,college.dept_13,college.dept_14,college.dept_15).all()
    return render_template('college_res.html',detai=detail,Addr=addr,Dept=dept)

    
@app.route('/proj',methods=['GET','POST'])
def proj():
    if request.method=='GET':
        return render_template('main_page.html')
    
    elif request.method=='POST':
        option=request.form['option']
        if option=='Submit_1':
            global Attitude_8,Education_8,Games_8,Eca_8,Time_8,Id,Name,Age,Gender,Choose
            #Id=int(request.form['id'])
            Name=request.form['name']
            Age=int(request.form['age'])
            if (Name=="" or Age==-1):
                return render_template('invalid_ip.html')
            Gender=request.form['gender']
            Choose=int(request.form['class'])
            Attitude_6=request.form['Attitude_8']
            Education_6=request.form['Education_8']
            Games_6=request.form['Games_8']
            Eca_6=request.form['Eca_8']
            Time_6=request.form['Time_8']
            return render_template('ip_form09.html')
        
        
        if option=='Submit_2':
            global Attitude_9,Education_9,Games_9,Eca_9,Time_9
            Attitude_9=request.form['Attitude_9']
            Education_9=request.form['Education_9']
            Games_9=request.form['Games_9']
            Eca_9=request.form['Eca_9']
            Time_9=request.form['Time_9']
            return render_template('ip_form10.html')
        
        if option=='Submit_3':
            global Attitude_10,Education_10,Games_10,Eca_10,Time_10
            results=[]
            Attitude_10=request.form['Attitude_10']
            Education_10=request.form['Education_10']
            Games_10=request.form['Games_10']
            Eca_10=request.form['Eca_10']
            Time_10=request.form['Time_10']
            if Choose is 10:
                db.child('User_details').child(str(Id)).push({'id':Id,'name':Name,'age':Age,'gender':Gender,'choose':Choose})
                Id=Id+1
                
                def attr():
                    Atd_8,Atd_9,Atd_10=Attitude_8,Attitude_9,Attitude_10
                    Atds_l=[Atd_8,Atd_9,Atd_10]
                    Atds=list(set(Atds_l))
                    d6,n_l={},[]
    
                    for i in Atds:
                        d6[i]=0

                    for i in Atds_l:
                        if  i is Atd_8:
                            d6[i]+=32
                            Atd_8=""
                        if  i is Atd_9:
                            d6[i]+=33
                            Atd_9=""
                        if  i is Atd_10:
                            d6[i]+=35
                            Atd_10=""
 
                    l=d6.values()
                    mx=max(l)
                    for i,j in d6.items():
                        if mx is j:
                            n_l.append(i)
                    Attitude=""
                    if "Bold" in n_l:
                        Attitude="Bold"
                    elif "Normal" in n_l:
                        Attitude="Normal"
                    else:
                        Attitude="Shie"
                    results.append(Attitude)
    
                attr()

                def edu():
                    Edu_8,Edu_9,Edu_10=Education_8,Education_9,Education_10
                    Edus_l=[Edu_8,Edu_9,Edu_10]
                    Edus=list(set(Edus_l))
                    d7,n_l={},[]
                    for i in Edus:
                        d7[i]=0
                    for i in Edus_l:
                        if  i is Edu_8:
                            d7[i]+=32
                            Edu_8=""
                        if  i is Edu_9:
                            d7[i]+=33
                            Edu_9=""
                        if  i is Edu_10:
                            d7[i]+=35
                            Edu_10=""
        
                    for i,j in d7.items():
                        if j>=33 :
                            n_l.append((i,j))
                    Education=dict(n_l)
                    results.append(Education)

                edu()


                def  game():
                    Gam_8,Gam_9,Gam_10=Games_8,Games_9,Games_10
                    Games_l=[Gam_8,Gam_9,Gam_10]
                    d8,n_l={},[]
                    Games=list(set(Games_l))
    
                    for i in Games:
                        d8[i]=0

                    for i in Games_l:
                        if  i is Gam_8:
                            d8[i]+=32
                            Gam_8=""
                        if  i is Gam_9:
                            d8[i]+=33
                            Gam_9=""
                        if  i is Gam_10:
                            d8[i]+=35
                            Gam_10=""
      
                    for i,j in d8.items():
                        if j>=33:
                            n_l.append((i,j))
                    games=dict(n_l)
                    results.append(games)
                
                game()



                def eca():
                    Ea_8,Ea_9,Ea_10=Eca_8,Eca_9,Eca_10
                    Ecas_l=[Ea_8,Ea_9,Ea_10]
                    d9,n_l={},[]
                    Ecas=list(set(Ecas_l))

                    for i in Ecas:
                        d9[i]=0

                    for i in Ecas_l:
                        if  i is Ea_8:
                            d9[i]+=32
                            Ea_8=""
                        if  i is Ea_9:
                            d9[i]+=33
                            Ea_9=""
                        if  i is Ea_10:
                            d9[i]+=35
                            Ea_10=""
      
                    for i,j in d9.items():
                        if j>=33:
                            n_l.append((i,j))
                    ecas=dict(n_l)
                    results.append(ecas)
                 
                eca()


                def mtf():
                    Mtf_8,Mtf_9,Mtf_10=Time_8,Time_9,Time_10
                    Mtfs_l=[Mtf_8,Mtf_9,Mtf_10]
                    d10,n_l={},[]
                    Mtfs=list(set(Mtfs_l))

                    for i in Mtfs:
                        d10[i]=0

                    for i in Mtfs_l:
                        if  i is Mtf_8:
                            d10[i]+=32
                            Mtf_8=""
                        if  i is Mtf_9:
                            d10[i]+=33
                            Mtf_9=""
                        if  i is Mtf_10:
                            d10[i]+=35
                            Mtf_10=""
        
                    for i,j in d10.items():
                            if j>=33:
                                n_l.append((i,j))
                    mtfs=dict(n_l)
                    results.append(d10)
                    #results.append(mtfs)

                mtf()

                res=results[1]
                #res={'Tamil':63,'Maths':37}
                key=res.keys()
                n_key=list(key)
                course=[[],[]]
                ind2=0
                a=db.child('predict_ten').get()
                v=list(a.val().items())
                #print(list(a.val().items()))
                for i in n_key:
                    for j in v:
                        dt=list(j[1].values())[0]
                        if(dt[str(i)])=='NA':
                            pass
                        else:
                            s=dt[str(i)].split('-')
                            a,b,c=int(s[0]),int(s[1]),int(res[str(i)])
                            if (c>=a and c<=b):
                                course[ind2].append(dt['Courses'])
                    ind2+=1
                kk=list(results[4].keys())
                vv=list(results[4].values())
                ii=vv.index(max(vv))
                ss=kk[ii]
                spor=list(results[2].keys())
                ext=list(results[3].keys())
                return render_template("pred_res.html",det1=course[0],det2=course[1],subj=n_key,info=results,k_k=kk,v_v=vv,s_s=ss,sp_or=spor,ex_t=ext)
            else:
                return render_template('ip_form11.html')
        
        if option=='Submit_4':
            global Attitude_11,Education_11,Games_11,Eca_11,Time_11
            Attitude_11=request.form['Attitude_11']
            Education_11=request.form['Education_11']
            Games_11=request.form['Games_11']
            Eca_11=request.form['Eca_11']
            Time_11=request.form['Time_11']
            return render_template('ip_form12.html')

        if option=='Submit_5':
            global Attitude_12,Education_12,Games_12,Eca_12,Time_12
            results=[]
            Attitude_12=request.form['Attitude_12']
            Education_12=request.form['Education_12']
            Games_12=request.form['Games_12']
            Eca_12=request.form['Eca_12']
            Time_12=request.form['Time_12']
            db.child('User_details').child(str(Id)).push({'id':Id,'name':Name,'age':Age,'gender':Gender,'choose':Choose})
            Id=Id+1
            
            def attr():
                Atd_8,Atd_9,Atd_10,Atd_11,Atd_12=Attitude_8,Attitude_9,Attitude_10,Attitude_11,Attitude_12
                Atds_l=[Atd_8,Atd_9,Atd_10,Atd_11,Atd_12]
                Atds=list(set(Atds_l))
                d6,n_l={},[]
    
                for i in Atds:
                    d6[i]=0

                for i in Atds_l:
                    if  i is Atd_8:
                        d6[i]+=16
                        Atd_8="" 
                    if  i is Atd_9:
                        d6[i]+=17
                        Atd_9=""   
                    if  i is Atd_10:
                        d6[i]+=18
                        Atd_10="" 
                    if  i is Atd_11:
                        d6[i]+=24
                        Atd_11=""
                    if  i is Atd_12:
                        d6[i]+=25
                        Atd_12=""
 
                l=d6.values()
                mx=max(l)
                for i,j in d6.items():
                    if mx is j:
                        n_l.append(i)
                Attitude=""
                if "Bold" in n_l:
                    Attitude="Bold"
                elif "Normal" in n_l:
                    Attitude="Normal"
                else:
                    Attitude="Shie"
                results.append(Attitude)

            attr()
            
            def edu():
                Edu_8,Edu_9,Edu_10,Edu_11,Edu_12=Education_8,Education_9,Education_10,Education_11,Education_12
                Edus_l=[Edu_8,Edu_9,Edu_10,Edu_11,Edu_12]
                Edus=list(set(Edus_l))
                d7,n_l={},[]
                for i in Edus:
                    d7[i]=0
                for i in Edus_l:
                    if  i is Edu_8:
                        d7[i]+=16
                        Edu_8=""  
                    if  i is Edu_9:
                        d7[i]+=17
                        Edu_9="" 
                    if  i is Edu_10:
                        d7[i]+=18
                        Edu_10=""  
                    if  i is Edu_11:
                        d7[i]+=24
                        Edu_11=""
                    if  i is Edu_12:
                        d7[i]+=25
                        Edu_12=""
        
                for i,j in d7.items():
                    if j>=33 :
                        n_l.append((i,j))
                Education=dict(n_l) 
                results.append(Education)

            edu()
            
            def  game():
                Gam_8,Gam_9,Gam_10,Gam_11,Gam_12=Games_8,Games_9,Games_10,Games_11,Games_12
                Games_l=[Gam_8,Gam_9,Gam_10,Gam_11,Gam_12]
                d8,n_l={},[]
                Games=list(set(Games_l))
    
                for i in Games:
                    d8[i]=0

                for i in Games_l:
                    if  i is Gam_8:
                        d8[i]+=16
                        Gam_8=""   
                    if  i is Gam_9:
                        d8[i]+=17
                        Gam_9=""  
                    if  i is Gam_10:
                        d8[i]+=18
                        Gam_10="" 
                    if  i is Gam_11:
                        d8[i]+=24
                        Gam_11=""  
                    if  i is Gam_12:
                        d8[i]+=25
                        Gam_12=""
      
                for i,j in d8.items():
                    if j>=33:
                        n_l.append((i,j))
                games=dict(n_l)
                results.append(games)
                
            game()
            
            def eca():
                Ea_8,Ea_9,Ea_10,Ea_11,Ea_12=Eca_8,Eca_9,Eca_10,Eca_11,Eca_12
                Ecas_l=[Ea_8,Ea_9,Ea_10,Ea_11,Ea_12]
                d9,n_l={},[]
                Ecas=list(set(Ecas_l))

                for i in Ecas:
                    d9[i]=0

                for i in Ecas_l:
                    if  i is Ea_8:
                        d9[i]+=16
                        Ea_8="" 
                    if  i is Ea_9:
                        d9[i]+=17
                        Ea_9=""
                    if  i is Ea_10:
                        d9[i]+=18
                        Ea_10=""   
                    if  i is Ea_11:
                        d9[i]+=24
                        Ea_11="" 
                    if  i is Ea_12:
                        d9[i]+=25
                        Ea_12=""
      
                for i,j in d9.items():
                    if j>=33:
                        n_l.append((i,j))
                ecas=dict(n_l)
                results.append(ecas)
                 
            eca()
            
            def mtf():
                Mtf_8,Mtf_9,Mtf_10,Mtf_11,Mtf_12=Time_8,Time_9,Time_10,Time_11,Time_12
                Mtfs_l=[Mtf_8,Mtf_9,Mtf_10,Mtf_11,Mtf_12]
                d10,n_l={},[]
                Mtfs=list(set(Mtfs_l))

                for i in Mtfs:
                    d10[i]=0

                for i in Mtfs_l: 
                    if  i is Mtf_8:
                        d10[i]+=16
                        Mtf_8=""   
                    if  i is Mtf_9:
                        d10[i]+=17
                        Mtf_9=""   
                    if  i is Mtf_10:
                        d10[i]+=18
                        Mtf_10=""  
                    if  i is Mtf_11:
                        d10[i]+=24
                        Mtf_11=""  
                    if  i is Mtf_12:
                        d10[i]+=25
                        Mtf_12=""
                        
                for i,j in d10.items():
                    if j>=33:
                        n_l.append((i,j))
                mtfs=dict(n_l)
                results.append(d10)

            mtf()
            
            
            res=results[1]
            key=res.keys()
            n_key=list(key)
            course=[[],[]]
            ind1=0
            a=db.child('predict').get()
            v=list(a.val().items())
            #print(list(a.val().items()))
            for i in n_key:
                for j in v:
                    dt=list(j[1].values())[0]
                    if(dt[str(i)])=='NA':
                        pass
                    else:
                        s=dt[str(i)].split('-')
                        a,b,c=int(s[0]),int(s[1]),int(res[str(i)])
                        if (c>=a and c<=b):
                            course[ind1].append(dt['Courses'])
                ind1+=1
            kk=list(results[4].keys())
            vv=list(results[4].values())
            ii=vv.index(max(vv))
            ss=kk[ii]
            spor=list(results[2].keys())
            ext=list(results[3].keys())
            return render_template("pred_res.html",det1=course[0],det2=course[1],subj=n_key,info=results,k_k=kk,v_v=vv,s_s=ss,sp_or=spor,ex_t=ext)
            
        
if __name__=="__main__":
    app.run(debug=True)