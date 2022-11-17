from flask import Blueprint,request,session
from dotenv import dotenv_values
from server.postgresql_curd import PostgreSQLDB,parse_the_type,return_utc_add_8_times
# from ..main import user
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


userService = Blueprint('userService', __name__)

@userService.route('/usershow')
def show():
    return "Hello fucking app2"

@userService.route('/user' , methods=['GET',"POST","PUT","DELETE"])
def CURD():
    if(request.method == 'GET'):
        '''
        getOneByID
        '''
        if(request.args.get('id')):
            id = request.args.get('id')
            # user = 
            # print(session["user"].query.filter_by(serial=1).first()) # 不知道為啥一直失敗
            print(session["name"])
            print(session["game"].query.filter_by(serial=5).first())

            '''
            第20句 在幫我調研 我覺得update insert 用 orm應該比較合理 但目前不知道為啥import 一職失敗 local是可以的
            '''
            dataObject = PostgreSQLDB.getDF(f'''select * 
                                                from "user" u  
                                                where "serial" ={str(id)}''')
            return dataObject.to_json(orient='records')
        else:
            '''
            get all 
            '''
            dataObject = PostgreSQLDB.getDF(f'''select * from "user" ''')
            return dataObject.to_json(orient='records')

    elif(request.method == 'POST'):
        '''
        insertOneData()
        '''
        dataObject = request.json
        name = parse_the_type(dataObject['name'])
        sex = parse_the_type(dataObject['sex'])
        PostgreSQLDB.executeQuery(f'''
        INSERT INTO public.user
        ("name", "sex")
        VALUES({name}, {sex});
        ''')
        return "add scuess"

    elif(request.method == 'PUT'):
        '''
        updateByID()
        '''
        dataObject = request.json
        serial = parse_the_type(dataObject['serial'])
        name = parse_the_type(dataObject['name'])
        sex = parse_the_type(dataObject['sex'])

        PostgreSQLDB.executeQuery(f'''
        UPDATE public.user
        SET "name"={name}, 
            "sex"={sex}
        WHERE serial={serial};
        ''')
        return "update scuess"

    elif(request.method == 'DELETE'):
        '''
        DeleteByID()
        '''
        dataObject = request.json
        serial = parse_the_type(dataObject['serial'])
        PostgreSQLDB.executeQuery(f'''
        DELETE FROM public."user"
        WHERE serial={serial};
        ''')
        return "delete scuess"
