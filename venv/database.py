import mysql.connector
import requests


db = mysql.connector.connect(
    user="sql5438247",
    passwd="qTQKC5tmJk",
    host="sql5.freemysqlhosting.net",
    database="sql5438247"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE User(name VARCHAR(50), passwd VARCHAR(50), personID int PRIMARY KEY AUTO_INCREMENT)")

name = "oinktink"
passwd = "tanimusmanimus"

# # #
# # mycursor.execute(f"INSERT INTO User(name, passwd) VALUES(%s, %s)", (name, passwd))
# # db.commit()
#
# mycursor.execute("ALTER TABLE User")

data = {
    "user": "lzy",
    "passwd": 123,
    "travel_distance": 12000,
    "transport_type": "CAR",
    "postalcode": "L5M5M4"
}

postalcode = data["postalcode"]
postal = [postalcode[0:3], postalcode[3:6]]
response = requests.get(f'https://geocoder.ca/?locate={postal[0]}%20{postal[1]}&geoit=XML&json=1')

latlong = []
latlong.append(response.json()['latt'])
latlong.append(response.json()['longt'])
mycursor.execute(
    "INSERT INTO User(name, passwd, groupcode, travel_distance, transport_type, postalcode, latt,longt) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
    (data["user"], data["passwd"], data["groupcode"], data["travel_distance"], data["transport_type"], data["postalcode"], latlong[0],
    latlong[1]))

db.commit()
# mycursor.execute("SELECT * FROM User")
# #
# for x in mycursor:
#     print(x)