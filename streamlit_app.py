# streamlit_app.py
import streamlit as st
import uuid
import time
import pymysql

def generate_key():
    # Generate a unique key
    key = str(uuid.uuid4())
    # Set expiry time for 24 hours from now
    expiry = int(time.time()) + (24 * 60 * 60)
    return key, expiry

def save_key_to_database(key, expiry):
    # Placeholder for database connection and insertion logic
    connection = pymysql.connect(host='paywall.doctorsvote.app',
                                 user='prospectivepay',
                                 password='84hdk83jhs2',
                                 database='auth_keys',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "INSERT INTO auth_keys (`key`, `expiry`) VALUES (%s, %s)"
        cursor.execute(sql, (key, expiry))
    connection.commit()
    connection.close()

st.title('Authentication Key Generator')

if st.button('Generate Authentication Key'):
    key, expiry = generate_key()
    save_key_to_database(key, expiry)
    st.success(f'Generated Key: {key}')
    st.write(f'Expires in 24 hours.')
