import time as t
from datetime import date
import mysql.connector as mycon
mydb=mycon.connectcon.connect(host='localhost',user='root',password='12345')
mycursor=mydb.cursor(dictionary=True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS FOOD_GENDA")
mycursor.execute('USE FOOD_GENDA')
mycursor.execute('CREATE TABLE IF NOT EXISTS USERS (NAME    VARCHAR(50) , E_MAIL   VARCHAR(50)  PRIMARY KEY,PH_NO     VARCHAR(10)     UNIQUE,PASSWD     VARCHAR(30)      DEFAULT NULL,T_PRICE   INT(8)   DEFAULT 0,N_ITEMS    INT(8)   DEFAULT 0)')
mycursor.execute("CREATE TABLE IF NOT EXISTS D_BOY (NAME   VARCHAR(50), ADHAAR    VARCHAR(12)   Primary Key,City  VARCHAR(45) DEFAULT NULL,AGE      SMALLINT   DEFAULT NULL,STATUS     VARCHAR(10)     DEFAULT 'NO',GENDER      VARCHAR(1)   DEFAULT NULL,D_APPLY    DATE,D_APPROVAL   DATE)")
def feedback():
    feedback=input("""
+——————————————————————————————————————————————————————————————————————————————————————+
|          _____             _ _                _      ____                            |
|         |  ___|__  ___  __| | |__   __ _  ___| | __ |  _ \ __ _  __ _  ___           |
|         | |_ / _ \/ _ \/ _` | '_ \ / _` |/ __| |/ / | |_) / _` |/ _` |/ _ \          |
|         |  _|  __/  __/ (_| | |_) | (_| | (__|   <  |  __/ (_| | (_| |  __/          |
|         |_|  \___|\___|\__,_|_.__/ \__,_|\___|_|\_\ |_|   \__,_|\__, |\___|          |
|                                                                 |___/                |
+——————————————————————————————————————————————————————————————————————————————————————+
+————————————————————————————————————————————————————————————————————+
|  Please Provide us your valuable feedback or any suggestions       |
+————————————————————————————————————————————————————————————————————+
===> """)
    with open('.feedback','a') as d:
        name=input('''
+————————————————————————————————————————————————————————+
|  Enter your Name                                       |
+————————————————————————————————————————————————————————+
===> ''')
        email=input("""
+————————————————————————————————————————————————————————+
|  Enter your E-Mail                                     |
+————————————————————————————————————————————————————————+
===> """)
        d.write(feedback+f" \n —by {name} E_mail- {email}")
        print("""
+————————————————————————————————————————————————————————————————————+
|    Thanks for spending your precious time in providing Valuable    |
|                           Feedback to us                           |
+————————————————————————————————————————————————————————————————————+
""")
def d_boy():
    print("""
+——————————————————————————————————————————————————————————————————————————————————————+
|            _                       __             _______                            |
|           / \                     [  |           |_   __ \                           |
|          / _ \    _ .--.   _ .--.  | |   _   __    | |__) |,--.   .--./) .---.       |
|         / ___ \  [ '/'`\ \[ '/'`\ \| |  [ \ [  ]   |  ___/`'_\ : / /'`\;/ /__\\       |
|       _/ /   \ \_ | \__/ | | \__/ || |   \ '/ /   _| |_   // | |,\ \._//| \__.,      |
|      |____| |____|| ;.__/  | ;.__/[___][\_:  /   |_____|  \'-;__/.',__`  '.__.'       |
|                  [__|     [__|          \__.'                   ( ( __))             |
+——————————————————————————————————————————————————————————————————————————————————————+
""")
    status=input("""
+————————————————————————————————————————————————————————————————————+
|    ____                      _____       _              _          |
|   |  _ \ _ __ ___  ___ ___  | ____|_ __ | |_ ___ _ __  | |_ ___    |
|   | |_) | '__/ _ \/ __/ __| |  _| | '_ \| __/ _ \ '__| | __/ _ \   |
|   |  __/| | |  __/\__ \__ \ | |___| | | | ||  __/ |    | || (_) |  |
|   |_|   |_|  \___||___/___/ |_____|_| |_|\__\___|_|     \__\___/   |
|                                                                    |
|               ____            _   _                                |
|              / ___|___  _ __ | |_(_)_ __  _   _  ___               |
|             | |   / _ \| '_ \| __| | '_ \| | | |/ _ \              |
|             | |__| (_) | | | | |_| | | | | |_| |  __/              |
|              \____\___/|_| |_|\__|_|_| |_|\__,_|\___|              |
+————————————————————————————————————————————————————————————————————+
""")
    if status !='what is my status':
        while True:
            name=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter your full name                                              |
+————————————————————————————————————————————————————————————————————+
===> """)
            try:
                adhaar=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter your Adhaar Card Number                                     |
+————————————————————————————————————————————————————————————————————+
===> """)
                if len(adhaar)!=12:
                    a=int(adhaar)
                    print("""
+————————————————————————————————————————————————————————————————————+
|         Adhaar Card Number is entered in incorrect format          |
+————————————————————————————————————————————————————————————————————+
""")
                    continue
                else:
                    adhaar=str(adhaar)
            except:
                print("""
+————————————————————————————————————————————————————————————————————+
|         Adhaar Card Number is entered in incorrect format          |
+————————————————————————————————————————————————————————————————————+""")
                continue
            mycursor.execute("SELECT * FROM D_BOY")
            data=mycursor.fetchall()
            for i in data:
                if i['ADHAAR']==adhaar:
                    mycursor.execute(f"DELETE FROM D_BOY WHERE ADHAAR='{adhaar}'")
                    break
            city=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter the City in which you live                                  |
+————————————————————————————————————————————————————————————————————+
===> """).lstrip().rstrip()
            try:
                age=int(input("""
+————————————————————————————————————————————————————————————————————+
|  Enter Your Age                                                    |
+————————————————————————————————————————————————————————————————————+
===> """))
            except:
                print("""
+————————————————————————————————————————————————————————————————————+
|              !! Age should be entered numerically !!               |
+————————————————————————————————————————————————————————————————————+
""")
                continue
            gender=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter your gender{Male:M/m,Female:F/f,Other:O/o}                  |
+————————————————————————————————————————————————————————————————————+
===> """).lower()
            if (gender!="m" and gender!='f' and gender!='o') or gender=='':
                print("""
+————————————————————————————————————————————————————————————————————+
|        Please enter your Gender in the above stated format         |
+————————————————————————————————————————————————————————————————————+
""")
                continue
            else:
                a=date.today()
                print("""
+————————————————————————————————————————————————————————————————————+
|  Your data has been sent to the owner.You can know your status by  |
|       going back to apply page and typing 'what is my status'      |
+————————————————————————————————————————————————————————————————————+
""")
                mycursor.execute(f"INSERT INTO D_BOY (NAME,ADHAAR,CITY,AGE,GENDER,D_APPLY) VALUES('{name}','{adhaar}','{city}',{age},'{gender}','{a}')")
                mydb.commit()
                break
    else:
        while True:
            adh=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter your Adhaar Number                                          |
+————————————————————————————————————————————————————————————————————+
===> """)
            mycursor.execute("SELECT * FROM D_BOY")
            data=mycursor.fetchall()
            adh_found=False
            for i in data:
                if i['ADHAAR']==adh:
                    adh_found=True
                    break
            if adh_found==True:
                is_resolved=False
                for i in data:
                    if i['STATUS']!='YES':
                        is_resolved=True
                        break
                if is_resolved==True:
                    print("""
+————————————————————————————————————————————————————————————————————+
|  Congratulations ...You have been choosen as a delivery boy at     |
|  Food Genda.Please follow the following guidelines, else you will  |
|  loose your job:-                                                  |
|  1. No misbehaving with customer.                                  |
|  2. Food should not be delivered late at any cost                  |
|  3. Stealing of food will not be tolerated at all                  |
|                                                                    |
|  Please contact us via e-mail to know more about your job ...      |
|  E-mail ---> fastdelivery@foodgenda.com                            |
+————————————————————————————————————————————————————————————————————+
""")
                    break
                elif is_resolved==False:
                    print("""
+————————————————————————————————————————————————————————————————————+
|  Sorry, No response has been given by the team... You may re-apply |
|  or wait                                                           |
+————————————————————————————————————————————————————————————————————+
""")
                    break
            else:
                t.sleep(0.5)
                print("""
+————————————————————————————————————————————————————————————————————+
|   This Adhaar Card number is not registered..., Please try again   |
+————————————————————————————————————————————————————————————————————+
""")
                t.sleep(0.35)
                cont=input("""
+————————————————————————————————————————————————————————————————————+
|    Do you want to continue(Y/y)  or  go back to main menu(N/n)?    |
+————————————————————————————————————————————————————————————————————+
""").lower()
                if cont=='y' or cont=='yes' and cont not in '':
                    continue
                else:
                   break 
def iprice(foodcat,choicelist):
    price=0
    for i in foodcat:
        for j in choicelist:
            if i==int(j):
                price+=foodcat[i][1]
                break
    print("""
+————————————————————————————————————————————————————————————————————+
|  Generating bill Please wait                                       |""")
    for i in range(3):
        print("""|  .                                                                 |""")
        t.sleep(0.5)
    print("""+————————————————————————————————————————————————————————————————————+
""")
    print("""
+————————————————————————————————————————————————————————————————————+
|                       ******Food Bill******                        |
+————————————————————————————————————————————————————————————————————+
|                    Food Items                    |       Price     |
+————————————————————————————————————————————————————————————————————+""")
            
    for i in foodcat:
        for k in choicelist:
            if int(k)==i:
                print(f"| {foodcat[i][0]:49s}| {chr(8377)}{str(foodcat[i][1]):15s}|")
                break
    print(f"""+————————————————————————————————————————————————————————————————————+
| Total Price                                   ===>{chr(8377)}{str(price):16s}|
+————————————————————————————————————————————————————————————————————+
""")
    return price
def welcome():
    t.sleep(1)
    print("""
+——————————————————————————————————————————————————————————————————————————————————————+""");t.sleep(0.025)
    print("""|    _______________________________     ______________________   ________________     |""");t.sleep(0.025)
    print("""|    ___  ____/_  __ \_  __ \__  __ \    __  ____/__  ____/__  | / /__  __ \__    |    |""");t.sleep(0.025)
    print("""|    __  /_   _  / / /  / / /_  / / /    _  / __ __  __/  __   |/ /__  / / /_  /| |    |""");t.sleep(0.025)
    print("""|    _  __/   / /_/ // /_/ /_  /_/ /     / /_/ / _  /___  _  /|  / _  /_/ /_  ___ |    |""");t.sleep(0.025)
    print("""|    /_/      \____/ \____/ /_____/      \____/  /_____/  /_/ |_/  /_____/ /_/  |_|    |""");t.sleep(0.025)
    print("""+——————————————————————————————————————————————————————————————————————————————————————+""");t.sleep(0.025)
    print("""
+——————————————————————————————————————————————————————————————————————————————————————+
|                                                                                      |
|    :syys+`                                                                           |
|   oyoooooy+                                                                          |
|  osooooooosh-                                                                        |
| /yooooooooooms.                                                                      |
|.hoooooooooosyhy+`                                                        :/:`        |
|osooooooosyhhhdy+y/                                                      .y/+s-       |
|hoooooooyhhhhhhmo/oy`           `-:/++ooooossoooo+++/:-`                `y////s/      |
|d+oooooyhhhhhhhhm//+h.    `-/+ossoo++/////////////////+oso+/-`         `s+/////y:     |
|hsooooshhhhhhhhhmo//+h`-+oysooo++///////////////////////////oso/-     .s+//////+h`    |
|-mooooyhhhhhhhhhdy///odsoooo+///////////////////////////////////os+:`/s/////////s+    |
| :dyooyhhhhhhhhhhd////yso++////////////////////////////////////////+syo/////////oy    |
|  .ymyyhhhhhhhhhhN/////y+////////////////////////////////////////////+oyo//////++h    |
|    :hmdddhhhhhhyN//////////////////////////////////////////////////////oyo///+ooy    |
|     `-oyhhhdddhhmo///////////////////////////////////////////////////////oyo+ooh-    |
|        `-hyyssooos/////////////////////////////////////////////////////////syoy:     |
|        :yooooooo+///////////////////////////////////////////////////////////+h:      |
|       +yooooooo+/////////////////////////////////////////////////////////////+y:     |
|      oyooooooo+////////////////////////+oyyyso/////////////////////////////////y:    |
|     osooooooo+///////////////////////odmddhhhhho+///////////////////////////////y-   |
|    +yooooooo+//////////////////////ohhsoo+ooo+ooo+///////////////////////////////h.  |
|   -hoooooooo//////////////////////sso++++++++++++++//////////////////////////////os  |
|  `hoooooooo+/////////////////////+o+++++++++++++++++///////////////////////////+ydN- |
|  /yoooooooo/////////////////////++++++++osyyyys++++++/////////////////////////+ooody |
|  hoooooooo+/////////////////////++++++yhs+:::/oyy++++/////////////////////////++++od |
| .doooooooo/////////////////////+++++sh/.````````/y++++///////////////////////++++++d |
| +yoooooooo/////////////////////++++yo......`     .y+++/////////////////////osyy+++oy |
| ssooooooo+/////////////////////+++ys  `:syyss/-   -y++////////////////////s/--+d++h: |
| yoooooooo+/////////////////////++om-    :mddhyyo.  o++///////////////////y:  ``osos  |
| soooooooo+/////////////////////++hho-``-hMMMNdyyy. -s+//////////////////hh:`   /yy`  |
| osoooooooo/////////////////////+/hsNNmmNMMMMMMmyyo `y+/////////////////hm+-`   od.   |
| :hoooooooo///////////////////////hsMMMMMMMMMMMNooy .y/////////////////yMm` `: `y.    |
| `doooooooo+//////////////////////syNMMMMMMMMMMdooo /o////////////////sMMMhoso /-     |
|  ssooooooo+//////////////////////+hymMMMMMMMyosos..s////////////////+NMMMNyy/./      |
|  .doooooooo///////////////////////odhhdmmmdh++so--s+////////////////yMMMMhos./       |
|   +yooooooo+////////////////////////osyyssssys+/oo//////////////////NMNdysy//        |
|   `yoooooooo+//////////////////////////+ooooooo+////////////+++ooooomms//+ym`        |
|    .hoooooooo////////////////////////////////////////////////////+oys///+ooN+        |
|     .hooooooo+///////////////////////////////////////////////////++////+oo+hh.       |
|      .ysoooooo+///////////////////////////////////////+++//////////////ooo+mh+       |
|       `ssoooooo+///////////////////////////+++///////sso+++//////////+oooosyys       |
|         /yoooooo+//////////////+osssyhysyyyso////////o/osddy+/////+sooooooh//h`      |
|          .ssoooooo+///////////+o+++++dhoo++////////////hsMMMNs/////+ssyyyy+//hh.     |
|            :ssooooo++/////////////////mdo+////////////+hoMMMMN+/////+ossoo+//yys     |
|              :ssooooo+////////////////+NNy+////////////hodMMMMy//////++o++///yh/     |
|                -oyooooo++//////////////oMMmy++//////////yohNMMs//////////////m+      |
|                  `/oyoooo++/////////////yMMMNdyo++///////osyds//////////////s/       |
|                     `/ossooo+++//////////mMMMMMMmdso+//////////////////////os        |
|                         ./+sysooooo+/////oMMMMMMMMMmhs++//////////////////os`        |
|                             `-/+ooshds+///mmmmNMMMMmmmdyo++//////////////so          |
|                                     `:yo//odyyyhdNmdddmmmhoo+++++///+++ss-           |
|                                       `yo//dyssssydyyyyyddhsosssyyysso+.             |
|                                        `ss+/yhssssyssssyhso                          |
|                                          +yo++syhhhhhyyys:                           |
|                                           `:+ossyyyyso+-                             |
|                                                                                      |
+——————————————————————————————————————————————————————————————————————————————————————+""")
    t.sleep(0.7)
    print("+——————————————————————————————————————————————————————————————————————————————————————+");t.sleep(0.025)
    print("|               __   _      __   __       _             ____         __                |");t.sleep(0.025)
    print("|              / /  (_)__ _/ /  / /____  (_)__  ___ _  / __/__ ____ / /_               |");t.sleep(0.025)
    print("|             / /__/ / _ `/ _ \/ __/ _ \/ / _ \/ _ `/ / _// _ `(_-</ __/               |");t.sleep(0.025)
    print("|            /____/_/\_, /_//_/\__/_//_/_/_//_/\_, / /_/  \_,_/___/\__/                |");t.sleep(0.025)
    print("|                   /___/                     /___/                                    |");t.sleep(0.025)
    print("|                           ___      ___                                               |");t.sleep(0.025)
    print("|                          / _ \___ / (_)  _____ ______ __                             |");t.sleep(0.025)
    print("|                         / // / -_) / / |/ / -_) __/ // /                             |");t.sleep(0.025)
    print("|                        /____/\__/_/_/|___/\__/_/  \_, /                              |");t.sleep(0.025)
    print("|                                                  /___/                               |");t.sleep(0.025)
    print("+——————————————————————————————————————————————————————————————————————————————————————+");t.sleep(0.025)
welcome()
def o_choice(foodcat,email):
    while True:
        choice=input("""
+————————————————————————————————————————————————————————————————————+
| Enter the S.No. of the Food Item You want to order                 |
| Note: If you want to order more than one food item please enter    |
| their S.No. as 1,2,3 ...                                           |
+————————————————————————————————————————————————————————————————————+
===> """).lstrip().rstrip()
        choice=choice.rstrip()
        if choice!='' :
            choicelist=choice.split(",")
            address=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter the address where the food is to be delivered               |
+————————————————————————————————————————————————————————————————————+
===> """)
            payment=input("""
+————————————————————————————————————————————————————————————————————+
|             Please choose a payment option from below              |
+————————————————————————————————————————————————————————————————————+
|   +————————————————————————————+  +————————————————————————————+   |
|   | Cash on Delivery{Enter 1 } |  |  Online Payment {Enter 2}  |   |
|   +————————————————————————————+  +————————————————————————————+   |
+————————————————————————————————————————————————————————————————————+
===> """)
            tprice=0
            if payment=='1':
                tprice=iprice(foodcat,choicelist)
                print(f"""
+————————————————————————————————————————————————————————————————————+
|  Thanks For Ordering Food From us ...Your items will be delivered  |
|  at {address:63s}|
+————————————————————————————————————————————————————————————————————+
""")
                print("""
+————————————————————————————————————————————————————————————————————+
|  !!!        Please don't bargain with the delivery boy        !!!  |
+————————————————————————————————————————————————————————————————————+
""")
                mycursor.execute(f"SELECT * FROM USERS WHERE E_MAIL='{email}'")
                data=mycursor.fetchall()
                for i in data:
                    if i['E_MAIL']==email:
                        tprice+=i['T_PRICE']
                        mycursor.execute(f"UPDATE USERS SET T_PRICE={tprice} WHERE E_MAIL='{email}'")
                        i_count=0
                        for j in choicelist:
                            i_count+=1
                        i_count+=i['N_ITEMS']
                        mycursor.execute(f"UPDATE USERS SET N_ITEMS={i_count}  WHERE E_MAIL='{email}'")
                        mydb.commit()
                        break
                break
            if payment=='2':
                tprice=iprice(foodcat,choicelist)
                up_id=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter your UPI-ID                                                 |
+————————————————————————————————————————————————————————————————————+
===> """)
                up_pin=input("""
+————————————————————————————————————————————————————————————————————+
|  Enter your UPI-PIN                                                |
+————————————————————————————————————————————————————————————————————+
===> """)
                print(f"""
+————————————————————————————————————————————————————————————————————+
|  Thanks For Ordering Food From us ...Your items will be delivered  |
|  at {address:63s}|
+————————————————————————————————————————————————————————————————————+
""")
                mycursor.execute(f"SELECT * FROM USERS WHERE E_MAIL='{email}'")
                data=mycursor.fetchall()
                for i in data:
                    if i['E_MAIL']==email:
                        tprice+=i['T_PRICE']
                        mycursor.execute(f"UPDATE USERS SET T_PRICE={tprice} WHERE E_MAIL='{email}'")
                        i_count=0
                        for j in choicelist:
                            i_count+=1
                        i_count+=i['N_ITEMS']
                        mycursor.execute(f"UPDATE USERS SET N_ITEMS={i_count}  WHERE E_MAIL='{email}'")
                        mydb.commit()
                        break
                break
        else:
            print("""
+————————————————————————————————————————————————————————————————————+
|               !! Please Enter something to order !!                |
+————————————————————————————————————————————————————————————————————+
""")
            continue
def veg(email):
    mycursor.execute(f"SELECT * FROM USERS WHERE E_MAIL='{email}'")
    data=mycursor.fetchall()
    print(f"""
+——————————————————————————————————————————————————————————————————————————————————————+
| User --> {data[0]['NAME']:76s}|
| No. of food Items Baught --> {str(data[0]['N_ITEMS']):56s}|
| Total Price of Items Baught --> {chr(8377)}{str(data[0]['T_PRICE']):51s}|
+——————————————————————————————————————————————————————————————————————————————————————+""")
    print("""+——————————————————————————————————————————————————————————————————————————————————————+
|       .........................................................................      |
|       ::::'###::::'##:::::::'##::::::::::::::::'##::::'##:'########::'######:::      |
|       :::'## ##::: ##::::::: ##:::::::::::::::: ##:::: ##: ##.....::'##... ##::      |
|       ::'##:. ##:: ##::::::: ##:::::::::::::::: ##:::: ##: ##::::::: ##:::..:::      |
|       :'##:::. ##: ##::::::: ##:::::::'#######: ##:::: ##: ######::: ##::'####:      |
|       : #########: ##::::::: ##:::::::........:. ##:: ##:: ##...:::: ##::: ##::      |
|       : ##.... ##: ##::::::: ##:::::::::::::::::. ## ##::: ##::::::: ##::: ##::      |
|       : ##:::: ##: ########: ########::::::::::::. ###:::: ########:. ######:::      |
|       :..:::::..::........::........::::::::::::::...:::::........:::......::::      |
+——————————————————————————————————————————————————————————————————————————————————————+
""");t.sleep(0.6)
    foodcat=input("""
+————————————————————————————————————————————————————————————————————+
| S.No. |                       Food Categories                      |
+————————————————————————————————————————————————————————————————————+
| 1.    | Appetizers                                                 |
| 2.    | Continental                                                |
| 3.    | Wok Station                                                |
| 4.    | Indian/Thalis                                              |
| 5.    | Fit N Fab                                                  |
| 6.    | Snacks                                                     |
| 7.    | Dessert                                                    |
+————————————————————————————————————————————————————————————————————+
| Enter the Serial Number of category of food                        |
+————————————————————————————————————————————————————————————————————+
===> """)
    appetizers_v={
1:["Veg Spring Rolls",150],
2:["Hara Bhara Kabaab",149],
3:["Cheesy Tandoori Potato",158],
4:["Peri-Peri Potato Wedges",149],
5:["Sesame Golden Coins",179],
6:["Asian BBQ Veggies",189],
7:["Potato Crunchers Box",179],
8:["Mongolian Cottage Cheese Crackers",199],
9:["Asian Bullet Veggies",179],
10:["Cheesy Corn Cocktail Samosa",179],
11:["Black Pepper Paneer",199],
12:["Chilli Paneer",189],
13:["Chilli Corn",179],
14:["Corn Spinach Cutlets",179],
15:["Garlic Bread Supreme",159]
}
    continental_v={
1:["Classic Mac 'n' Cheese",209],
2:["Creamy Mushroom Pasta",219],
3:["Mexical Burrito Bowl",209],
4:["Ultimate Burrito Bowl",209],
5:["Baked Mac 'n' Cheese",219]
}
    wok_v={
1:["American Lo Mein",185],
2:["Smoke That Bowl",229],
3:["Mix Veg Hakka Noodels",169],
4:["Spinach and Mushroom Noodles",189],
5:["Burnt Garlic Noodles",179],
6:["Bangkok Street Noodles",209],
7:["Dragon Noodles with Dimplings",229],
8:["Mongolian Hot Pot",209],
9:["Cheesy Baked Shezwan Noodles",209]
}
    indian_v={
1:["Aloo Paratha Combo",125],
2:["Methi Paratha Combo",125],
3:["Kadhai Paneer Thaali",199],
4:["Mutter Paneer with Jeera Rice",199],
5:["Rajma Masala Thaali",165],
6:["Chole 'n' Rice",165],
7:["Chana Masala 'n' Pulao",179],
8:["Banarasi Aloo Mutter with Paratha",125],
9:["Palak Paneer Kofta Thali",209],
10:["Mutter Paneer Thali",229],
11:["Chole Masala Thali",209],
12:["Paneer Butter-Masala 'n' Peas Pulao",199],
13:["Paneer Daal Makhni Bowl",199],
14:["Aloo Gobhi Thali",159],
15:["Home style Thali",165]
}
    fit_v={
1:["Stir-Fried-Chilli-Paneer Superbowl",249],
2:["Corn Cucumber Salad",189],
3:["Italian Garden Pizza Bowl",225],
4:["Veg Extra Veganza Pizza",225],
5:["Asian Greens Superbowl",239],
6:["Punjabi Rajma Brown Rice",185]
}
    snacks_v={
1:["Achari Paneer Tikka Wrap with Wedges and Lemonade",349],
2:["Perfect Veggie Burger",149],
3:["Peri Peri Paneer Burger",149],
4:["Loaded Crunchy Burger",149],
5:["Mix Veg Hakka Noodles",129],
6:["Cheesy Veg Sandwich",119],
7:["Mini Fruit Parfait",69],
8:["Fresh Fruit Bowl",119],
9:["Muesli Yogurt Parfait",129],
10:["Cheesy veg sandwich with Swiss roll",169],
11:["Kolkata Paneer Wrap",129],
12:["Cucumber Chutney Sandwich",89],
13:["Achari Paneer Tikka Wrap",139],
14:["Palak-Paneer Bhurji Wrap",129]
}
    dessert_v={
1:["Black Forest Cake Slice",89],
2:["Salted Caramel Chocolate Tart",120],
3:["Red Velvet",69],
4:["Rainbow Pastry",99],
5:["Dutch Truffle Cake",99],
6:["Shahi-Tukda",89],
7:["Melting Moments Cookies (Pack of 10)",99],
8:["Lava Cake in the Jar",129],
9:["Crumble-Blueberry-Cake",79],
10:["Chocolate Rabri Jar",149],
11:["Red Velvet Pop",35],
12:["Classic Rabri Gulab Jamun",89],
13:["Choci Walnut Brownie",79],
14:["Pineapple Cake Slice",89],
15:["Soan Papdi Cheese Cake",139],
16:["Lemon Tart",99]
}
            
    if foodcat=='1':
        foodcat=appetizers_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                             Appetizers                             |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in appetizers_v:
            print(f"| {i:2d}.   | {appetizers_v[i][0]:49s}| {chr(8377)}{str(appetizers_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='2':
        foodcat=continental_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                             Continental                            |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in continental_v:
            print(f"| {i:2d}.   | {continental_v[i][0]:49s}| {chr(8377)}{str(continental_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='3':
        foodcat=wok_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                             Wok Station                            |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in wok_v:
            print(f"| {i:2d}.   | {wok_v[i][0]:49s}| {chr(8377)}{str(wok_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='4':
        foodcat=indian_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                            Indian/Thalis                           |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in indian_v:
            print(f"| {i:2d}.   | {indian_v[i][0]:49s}| {chr(8377)}{str(indian_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='5':
        foodcat=fit_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                              Fit N Fab                             |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in fit_v:
            print(f"| {i:2d}.   | {fit_v[i][0]:49s}| {chr(8377)}{str(fit_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='6':
        foodcat=snacks_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                                Snacks                              |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in snacks_v:
            print(f"| {i:2d}.   | {snacks_v[i][0]:49s}| {chr(8377)}{str(snacks_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='7':
        foodcat=dessert_v
        print("""
+————————————————————————————————————————————————————————————————————+
|                              Desserts                              |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in dessert_v:
            print(f"| {i:2d}.   | {dessert_v[i][0]:49s}| {chr(8377)}{str(dessert_v[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    o_choice(foodcat,email)
def FoodType(email):
    mycursor.execute(f"SELECT * FROM USERS WHERE E_MAIL='{email}'")
    data=mycursor.fetchall()
    print(f"""
+——————————————————————————————————————————————————————————————————————————————————————+
| User --> {data[0]['NAME']:76s}|
| No. of food Items Baught --> {str(data[0]['N_ITEMS']):56s}|
| Total Amount of Items Baught --> {chr(8377)}{str(data[0]['T_PRICE']):51s}|
+——————————————————————————————————————————————————————————————————————————————————————+""")
    foodtype=input("""
+——————————————————————————————————————————————————————————————————————————————————————+
|       _____               _    ____      _                        _                  |
|      |  ___|__   ___   __| |  / ___|__ _| |_ ___  __ _  ___  _ __(_) ___  ___        |
|      | |_ / _ \ / _ \ / _` | | |   / _` | __/ _ \/ _` |/ _ \| '__| |/ _ \/ __|       |
|      |  _| (_) | (_) | (_| | | |__| (_| | ||  __/ (_| | (_) | |  | |  __/\__ \       |
|      |_|  \___/ \___/ \__,_|  \____\__,_|\__\___|\__, |\___/|_|  |_|\___||___/       |
|                                                  |___/                               |
+——————————————————————————————————————————————————————————————————————————————————————+
|   +—————————————————————————+ +——————————————————————+ +—————————————————————————+   |
|   |   Vegetarian{Enter 1}   | | Beverages {Enter 2}  | | Non-vegetarian{Enter 3} |   |
|   +—————————————————————————+ +——————————————————————+ +—————————————————————————+   |
+——————————————————————————————————————————————————————————————————————————————————————+
===> """)
    if foodtype=='1':
        veg(email)
    elif foodtype=='3':
        nonveg(email)
    elif foodtype=='2':
        beverages(email)
def nonveg(email):
    mycursor.execute(f"SELECT * FROM USERS WHERE E_MAIL='{email}'")
    data=mycursor.fetchall()
    print(f"""
+——————————————————————————————————————————————————————————————————————————————————————+
| User --> {data[0]['NAME']:76s}|
| No. of food Items Baught --> {str(data[0]['N_ITEMS']):56s}|
| Total Price of Items Baught --> {chr(8377)}{str(data[0]['T_PRICE']):51s}|
+——————————————————————————————————————————————————————————————————————————————————————+""")
    print("""+——————————————————————————————————————————————————————————————————————————————————————+
|       .........................................................................      |
|       :'##::: ##::'#######::'##::: ##::::::::::'##::::'##:'########::'######:::      |
|       : ###:: ##:'##.... ##: ###:: ##:::::::::: ##:::: ##: ##.....::'##... ##::      |
|       : ####: ##: ##:::: ##: ####: ##:::::::::: ##:::: ##: ##::::::: ##:::..:::      |
|       : ## ## ##: ##:::: ##: ## ## ##:'#######: ##:::: ##: ######::: ##::'####:      |
|       : ##. ####: ##:::: ##: ##. ####:........:. ##:: ##:: ##...:::: ##::: ##::      |
|       : ##:. ###: ##:::: ##: ##:. ###:::::::::::. ## ##::: ##::::::: ##::: ##::      |
|       : ##::. ##:. #######:: ##::. ##::::::::::::. ###:::: ########:. ######:::      |
|       :..::::..:::.......:::..::::..::::::::::::::...:::::........:::......::::      |
+——————————————————————————————————————————————————————————————————————————————————————+
""");t.sleep(0.6)
    foodcat=input("""
+——————————————————————————————————————————————————————————+
| S.No. |                  Food Categories                 |
+——————————————————————————————————————————————————————————+
| 1.    | Appetizers                                       |
| 2.    | Continental                                      |
| 3.    | Wok Station                                      |
| 4.    | Indian/Thalis                                    |
| 5.    | Fit N Fab                                        |
| 6.    | Snacks                                           |
+——————————————————————————————————————————————————————————+
| Enter the food no. to order the food                     |
+——————————————————————————————————————————————————————————+
===> """)
    appetizers_n={
1:["Chicken Seekh-Kebab",219],
2:["Jumbo Chilli Chicken Lollipops",439],
3:["Chicken Sausage Pepper Fry",239],
4:["Jumbo Teriyaki Chicken Wings",449],
5:["Chicken Nuggets",219],
6:["Southwest Chicken Strips with Wedges",299],
7:["Pan-Fried Chilli Fish",279],
8:["Masala Pepper Chicken",199],
9:["Peri-Peri Chicken Kebab (6 Nos.)",219],
10:["Chilli Chicken Lollipops (6 Nos.)",229],
11:["Honey Chicken Peppers",199],
12:["Chicken-Tikka",219],
13:["Maori Fish Fingers",249],
}
    continental_n={
1:["Penne Alfredo with Chicken Steak",239],
2:["Loaded Chicken Steak Bowl",249],
3:["The Mafia's Chicken Meal",249],
4:["Chef's Signature Grilled Chicken",249],
5:["Fish 'n' Chips",279],
6:["Peri-Peri Chicken Steak Bowl",235],
5:["Creamy Spaghetti Chicken Charcuterie",235]
}
    wok_n={
1:["Honey-Garlic Chicken Noodles",229],
2:["Teriyaki-Chicken Hot Pot",249],
3:["Smokey BBQ Chicken Rice Bowl",239],
4:["Orientel Grilled Fish",289],
5:["Dan Dan-Chicken Noodles",199],
6:["Schezwan Chicken Rice Bowl",219],
7:["Black Pepper Honey Chicken 'n' Noodles",219],
8:["Black Pepper Honey Chicken 'n' Rice",229],
9:["Chilli Garlic Chicken Noodles",209],
10:["Pan-Asian Egg 'n' Chicken Chowmein",219],
11:["Chilli Garlic Chicken Noodles",209]
}
    indian_n={
1:["Butter Chicken with Jeera Rice",199],
2:["Butter Chicken Thali",209],
3:["Ghee-Roast Chicken Thali",209],
4:["Chicken-Tikka Dum Biriyani Thali",259],
5:["Masala Pepper Chicken Thali",209],
6:["Hyderabadi Dum Chicken Biriyani Thali",259],
7:["Ghee Roast Thali Combo",289],
8:["Ghee-Roast Chicken Biriyani Thali",259]
}
    snacks_n={
1:["Chicken Tikka Sandwich + Mini Fruit Parfait",189],
2:["Homestyle Chicken Sandwich + Mini Parfait",179],
3:["Mexican-Pulled Chicken Sandwich",139],
4:["Homestyle-Chicken Sandwich",129],
5:["BBQ Chicken Club Sandwich",179],
6:["BBQ-Chicken 'n' Cheese Sandwich",139],
7:["Steak Egg 'n' Cheese Sandwich",139],
8:["Chicken Tikka Club Sandwich",179],
9:["Butter Chicken Wrap",149],
10:["Omelette cheese sandwich with Nutty Pop",139]
}
    fit_n={
1:["Loaded Chicken Pizza Bowl",225],
2:["Roasted Garlic Chicken Soup",149],
3:["Keto Club Chicken Salad",199],
4:["Peri-Peri Chicken Pizza Bowl",225],
5:["Peri-Peri Chicken Pizza Bowl",249],
6:["Keto Peri Peri Grilled Chicken Twin Steak",329],
7:["Chicken Caesar Salad",189],
8:["Arabic Chicken Salad",199],
9:["Keto Peri Peri Grilled Chicken Steak",219],
10:["Signature Grilled Chicken 'n' Brown Rice",249],
11:["Stir-fried Chicken-Superbowl",249],
12:["Chicken Lemon Coriander Soup",149],
13:["Black-Pepper Chicken Stir-Fry",219]
}
    if foodcat=='1':
        foodcat=appetizers_n
        print("""
+————————————————————————————————————————————————————————————————————+
|                             Appetizers                             |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in appetizers_n:
            print(f"| {i:2d}.   | {appetizers_n[i][0]:49s}| {chr(8377)}{str(appetizers_n[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='2':
        foodcat=continental_n
        print("""
+————————————————————————————————————————————————————————————————————+
|                             Continental                            |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in continental_n:
            print(f"| {i:2d}.   | {continental_n[i][0]:49s}| {chr(8377)}{str(continental_n[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='3':
        foodcat=wok_n
        print("""
+————————————————————————————————————————————————————————————————————+
|                             Wok Station                            |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in wok_n:
            print(f"| {i:2d}.   | {wok_n[i][0]:49s}| {chr(8377)}{str(wok_n[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='4':
        foodcat=indian_n
        print("""
+————————————————————————————————————————————————————————————————————+
|                            Indian/Thalis                           |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in indian_n:
            print(f"| {i:2d}.   | {indian_n[i][0]:49s}| {chr(8377)}{str(indian_n[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='5':
        foodcat=fit_n
        print("""
+————————————————————————————————————————————————————————————————————+
|                              Fit N Fab                             |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in fit_n:
            print(f"| {i:2d}.   | {fit_n[i][0]:49s}| {chr(8377)}{str(fit_n[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    elif foodcat=='6':
        foodcat=snacks_n
        print("""
+————————————————————————————————————————————————————————————————————+
|                                Snacks                              |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
        for i in snacks_n:
            print(f"| {i:2d}.   | {snacks_n[i][0]:49s}| {chr(8377)}{str(snacks_n[i][1]):7s}|")
            t.sleep(0.025)
        print("+————————————————————————————————————————————————————————————————————+")
    o_choice(foodcat,email)
def beverages(email):
    mycursor.execute(f"SELECT * FROM USERS WHERE E_MAIL='{email}'")
    data=mycursor.fetchall()
    print(f"""
+——————————————————————————————————————————————————————————————————————————————————————+
| User --> {data[0]['NAME']:76s}|
| No. of food Items Baught --> {str(data[0]['N_ITEMS']):56s}|
| Total Price of Items Baught --> {chr(8377)}{str(data[0]['T_PRICE']):51s}|
+——————————————————————————————————————————————————————————————————————————————————————+""")
    print("""+——————————————————————————————————————————————————————————————————————————————————————+
|        ######  ####### #     # ####### ######     #     #####  #######  #####        | 
|        #     # #       #     # #       #     #   # #   #     # #       #     #       |
|        #     # #       #     # #       #     #  #   #  #       #       #             |
|        ######  #####   #     # #####   ######  #     # #  #### #####    #####        |
|        #     # #        #   #  #       #   #   ####### #     # #             #       |
|        #     # #         # #   #       #    #  #     # #     # #       #     #       |
|        ######  #######    #    ####### #     # #     #  #####  #######  #####        |
+——————————————————————————————————————————————————————————————————————————————————————+
""");t.sleep(0.6)
    beverages={
1:["Mango Lassi",85],
2:["Masala Lemonade",89],
3:["Mint Chaas",69],
5:["Chilli Guava Cooler",89],
6:["Whiskey Sour Cocktail",95]}
    print("""
+————————————————————————————————————————————————————————————————————+
|                             Beverages                              |
+————————————————————————————————————————————————————————————————————+
| S.No. |                    Food Items                    |  Price  |
+————————————————————————————————————————————————————————————————————+""")
    for i in beverages:
        print(f"| {i:2d}.   | {beverages[i][0]:49s}| {chr(8377)}{str(beverages[i][1]):7s}|")
        t.sleep(.025)
    print("+————————————————————————————————————————————————————————————————————+")
    o_choice(beverages,email)
def login():
    mycursor.execute("SELECT * FROM USERS")
    data=mycursor.fetchall()
    t.sleep(0.5)
    choice=input("""
+——————————————————————————————————————————————————————————————————————————————————————+
|                   _                 _        ______                                  |
|                  | |               (_)       | ___ \                                 |
|                  | |     ___   __ _ _ _ __   | |_/ /_ _  __ _  ___                   |
|                  | |    / _ \ / _` | | '_ \  |  __/ _` |/ _` |/ _ \                  |
|                  | |___| (_) | (_| | | | | | | | | (_| | (_| |  __/                  |
|                  \_____/\___/ \__, |_|_| |_| \_|  \__,_|\__, |\___|                  |
|                                __/ |                     __/ |                       |
|                               |___/                     |___/                        |
+——————————————————————————————————————————————————————————————————————————————————————+
|                            Create a new account {Enter 1}                            |
|                           Existing User ? Log-in {Enter 2}                           |
+——————————————————————————————————————————————————————————————————————————————————————+
===> """)
    if choice=='1':
        f_name=input("""
+————————————————————————————————————————————————————————+
|  Enter Your First Name                                 |
+————————————————————————————————————————————————————————+
===> """).lstrip().rstrip()
        l_name=input("""
+————————————————————————————————————————————————————————+
|  Enter Your Last Name                                  |
+————————————————————————————————————————————————————————+
===> """).rstrip().lstrip()
        name=f_name+" "+l_name
        while True:
            email=input("""
+————————————————————————————————————————————————————————+
|  Enter Your E-Mail                                     |
+————————————————————————————————————————————————————————+
===> """)
            flag1=1
            for i in data:
                if i['E_MAIL']==email:
                    flag1=0
                    break
            if flag1==0:
                print("""
+————————————————————————————————————————————————————————+
|       This E-Mail account is already registered        |
+————————————————————————————————————————————————————————+
""")
                continue
            else:
                break
        while True:
            passwd=input("""
+————————————————————————————————————————————————————————+
|  Enter your password                                   |
+————————————————————————————————————————————————————————+
===> """)
            num_c=0
            chr_c=0
            alp_c=0
            for i in passwd:
                if ord(i) in range(48,58):
                    num_c+=1
                elif ord(i) in range(97,123) or ord(i) in range(65,91):
                    alp_c+=1
                else:
                    chr_c+=1
            if num_c==0 or chr_c==0 or alp_c==0:
                print("""
+————————————————————————————————————————————————————————+
|      Your password must contain atleast 1 number       |
|         , 1 special character and 1 alphabet           |
+————————————————————————————————————————————————————————+
""")
                continue
            elif len(passwd)<5 or len(passwd)>16:
                print("""
+————————————————————————————————————————————————————————+
|  Password must contain atleast 5 characters and atmost |
|                     12 characters                      |
+————————————————————————————————————————————————————————+
""")
                continue
            else:
                v_passwd=input("""
+————————————————————————————————————————————————————————+
|  Confirm your password                                 |
+————————————————————————————————————————————————————————+
===> """)
                if v_passwd==passwd:
                    break
                else:
                    print("""
+————————————————————————————————————————————————————————+
|         Password's doesnt't match ...Try Again         |
+————————————————————————————————————————————————————————+
""")
                    continue
        while True:
            phno=input("""
+————————————————————————————————————————————————————————+
|  Enter your Phone Number                               |
+————————————————————————————————————————————————————————+
===> """)
            flag=1
            for i in data:
                if i['PH_NO']==phno:
                    print("""
+————————————————————————————————————————————————————————+
|      A user with this Phone Number already exists      |
+————————————————————————————————————————————————————————+
""")
                    flag=0
                    break
            if flag==0:
                 continue
            elif len(phno)==10:
                break
            else:
                print("""
+————————————————————————————————————————————————————————+
|  You have entered incorrect length of Phone Number     |
+————————————————————————————————————————————————————————+
""")
                continue
        mycursor.execute(f"INSERT INTO USERS(NAME,E_MAIL,PH_NO,PASSWD) VALUES('{name}','{email}','{phno}','{passwd}')")
        mydb.commit()
        print("""
+————————————————————————————————————————————————————————————————————+""");t.sleep(0.025)
        print("""|    ____                         ___     ____                       |""");t.sleep(0.025)
        print("""|   / __/_ _____________ ___ ___ / _/_ __/ / /_ __                   |""");t.sleep(0.025)
        print("""|  _\ \/ // / __/ __/ -_|_-<(_-</ _/ // / / / // /                   |""");t.sleep(0.025)
        print("""| /___/\_,_/\__/\__/\__/___/___/_/ \_,_/_/_/\_, /                    |""");t.sleep(0.025)
        print("""|                                          /___/                     |""");t.sleep(0.025)
        print("""|   _____             __         __  __  __                ____   __ |""");t.sleep(0.025)
        print("""|  / ___/______ ___ _/ /____ ___/ /  \ \/ /__  __ ______  /  _/__/ / |""");t.sleep(0.025)
        print("""| / /__/ __/ -_) _ `/ __/ -_) _  /    \  / _ \/ // / __/ _/ // _  /  |""");t.sleep(0.025)
        print("""| \___/_/  \__/\_,_/\__/\__/\_,_/     /_/\___/\_,_/_/   /___/\_,_/   |""");t.sleep(0.025)
        print("""|                                                                    |""");t.sleep(0.025)
        print("""+————————————————————————————————————————————————————————————————————+""");t.sleep(0.025)
        menu()
    elif choice=='2':
        while True:
            email=input("""
+————————————————————————————————————————————————————————+
|  Enter your E-Mail                                     |
+————————————————————————————————————————————————————————+
===>""")
            flag1=1
            for i in data:
                if i['E_MAIL']==email:
                    flag1=0
                    break
            if flag1==1:
                print("""
+————————————————————————————————————————————————————————+
|         This E-Mail account is not registered          |
+————————————————————————————————————————————————————————+
""")
                continue
            else:
                break
        while True:
            passwd=input('''
+————————————————————————————————————————————————————————+
|  Enter your Password                                   |
+————————————————————————————————————————————————————————+
===>''')
            for i in data:
                if i['E_MAIL']==email and i['PASSWD']==passwd:
                    f=1
                    break
                else:
                    f=0
            if f==0:
                print("""
+————————————————————————————————————————————————————————+
|       Incorrect Password Entered Please Try Again      |
+————————————————————————————————————————————————————————+
""")
                continue
            else:
                return email
    else:
        print("""
+————————————————————————————————————————————————————————+
|        Incorrect option entered Please Try Again       |
+————————————————————————————————————————————————————————+
""")
        login()
def PressEnterToContinue():
    status=input("""
+————————————————————————————————————————————————————————————————————+
|    ____                      _____       _              _          |
|   |  _ \ _ __ ___  ___ ___  | ____|_ __ | |_ ___ _ __  | |_ ___    |
|   | |_) | '__/ _ \/ __/ __| |  _| | '_ \| __/ _ \ '__| | __/ _ \   |
|   |  __/| | |  __/\__ \__ \ | |___| | | | ||  __/ |    | || (_) |  |
|   |_|   |_|  \___||___/___/ |_____|_| |_|\__\___|_|     \__\___/   |
|                                                                    |
|               ____            _   _                                |
|              / ___|___  _ __ | |_(_)_ __  _   _  ___               |
|             | |   / _ \| '_ \| __| | '_ \| | | |/ _ \              |
|             | |__| (_) | | | | |_| | | | | |_| |  __/              |
|              \____\___/|_| |_|\__|_|_| |_|\__,_|\___|              |
+————————————————————————————————————————————————————————————————————+
""")
def menu():
    t.sleep(0.7)
    print("""
+——————————————————————————————————————————————————————————————————————————————————————+
|                                 ___  __                                              |
|                                / _ \/ /__ ___ ____ ___                               |
|                               / ___/ / -_) _ `(_-</ -_)                              |
|                              /_/  /_/\__/\_,_/___/\__/                               |""")
    t.sleep(1/3)
    print("""|                             _      __     _ __      ___                              |
|                            | | /| / /__ _(_) /_    / _ |                             |
|                            | |/ |/ / _ `/ / __/   / __ |                             |
|                            |__/|__/\_,_/_/\__/   /_/ |_|                             |""")
    t.sleep(1/3)
    print("""|                               ____                     __                            |
|                              / __/__ _______  ___  ___/ /                            |
|                             _\ \/ -_) __/ _ \/ _ \/ _  /                             |
|                            /___/\__/\__/\___/_//_/\_,_/                              |
+——————————————————————————————————————————————————————————————————————————————————————+

""")
    t.sleep(1/3)
    choice=input("""
+——————————————————————————————————————————————————————————————————————————————————————+
| __      ___         _        _                                       _     _         |
| \ \    / / |_  __ _| |_   __| |___   _  _ ___ _  _  __ __ ____ _ _ _| |_  | |_ ___   |
|  \ \/\/ /| ' \/ _` |  _| / _` / _ \ | || / _ \ || | \ V  V / _` | ' \  _| |  _/ _ \  |
|   \_/\_/ |_||_\__,_|\__| \__,_\___/  \_, \___/\_,_|  \_/\_/\__,_|_||_\__|  \__\___/  |
|                                      |__/                                            |
|                                       _       ___                                    |
|                                    __| |___  |__ \                                   |
|                                   / _` / _ \   /_/                                   |
|                                   \__,_\___/  (_)                                    |
|                                                                                      |
+——————————————————————————————————————————————————————————————————————————————————————+
|                              Order Food Online  {Enter 1}                            |
|                            Apply For delivery boy  {Enter 2}                         |
|                             Provide your feedback {Enter 3}                          |
+——————————————————————————————————————————————————————————————————————————————————————+
===> """).lstrip().rstrip()
    if choice=='1':
        email=login()
        PressEnterToContinue()
        FoodType(email)
        PressEnterToContinue()
        menu()
    elif choice=='2':
        d_boy()
        PressEnterToContinue()
        menu()
    elif choice=='3':
        feedback()
        PressEnterToContinue()
        menu()
    else:
        menu()
menu()
        
  
                    
                
            
        
