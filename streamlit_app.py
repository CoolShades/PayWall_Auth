import streamlit as st
import uuid
import time
import pymysql

def generate_key():
    # Generate a unique key
    key = str(uuid.uuid4())
    # Set expiry time for 1 minute from now
    expiry = int(time.time()) + 60  # 60 seconds for 1 minute
    return key, expiry

def save_key_to_database(key, expiry):
    # Database connection and insertion logic
    connection = pymysql.connect(host='paywall.doctorsvote.app',
                                 port=3306,
                                 user='prospectivepay',
                                 password='84hdk83jhs2',
                                 database='auth_keys',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "INSERT INTO auth_keys (`key`, `expiry`) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (key, expiry))
            connection.commit()
        except pymysql.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

def create_auth_uri(key):
    # Construct the URI with the key
    uri = f"http://paywall.doctorsvote.app/prospectivepay?key={key}"
    return uri

st.title('Authentication Key Generator and Access URI')

if st.button('Generate Authentication Key'):
    key, expiry = generate_key()
    save_key_to_database(key, expiry)
    uri = create_auth_uri(key)
    st.success(f'Generated Key: {key}')
    st.write('Expires in 1 minute.')
    st.markdown(f'Access URI: [Click here to authenticate]({uri})')
