from flask import Blueprint,request
from dotenv import dotenv_values
from server.postgresql_curd import PostgreSQLDB,parse_the_type,return_utc_add_8_times



gameService = Blueprint('gameService', __name__)

@gameService.route('/gameshow')
def show():
    return "Hello fucking app2"

@gameService.route('/game' , methods=['GET',"POST","PUT","DELETE"])
def CURD():
    if(request.method == 'GET'):
        '''
        getOneByID
        '''
        if(request.args.get('id')):
            id = request.args.get('id')
            # print(game.query.filter_by(serial=1).first()) # 不知道為啥一直失敗
            dataObject = PostgreSQLDB.getDF(f'''select * 
                                                from "game" u  
                                                where "serial" ={str(id)}''')
            return dataObject.to_json(orient='records')
        else:
            '''
            get all 
            '''
            dataObject = PostgreSQLDB.getDF(f'''select * from "game" ''')
            return dataObject.to_json(orient='records')
    elif(request.method == 'POST'):
        '''
        insertOneData()
        '''
        dataObject = request.json
        gameName = dataObject['gameName']
        country = dataObject['country']
        PostgreSQLDB.executeQuery(f'''
        INSERT INTO public.game
        ("gameName", "Country", "LastUpdateDate")
        VALUES('{gameName}', '{country}', '{return_utc_add_8_times()}');
        ''')
        return "add scuess"
    elif(request.method == 'PUT'):
        '''
        updateByID()
        '''
        dataObject = request.json
        serial = parse_the_type(dataObject['serial'])
        gameName = parse_the_type(dataObject['gameName'])
        country = parse_the_type(dataObject['country'])

        PostgreSQLDB.executeQuery(f'''
        UPDATE public.game
        SET "gameName"={gameName}, 
            "Country"={country},
            "LastUpdateDate"='{return_utc_add_8_times()}'
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
        DELETE FROM public."game"
        WHERE serial={serial};
        ''')
        return "delete scuess"

