# db.py
import psycopg2
import os
from dotenv import load_dotenv

# You can use environment variables or hardcode for local dev
load_dotenv()
DB_PARAMS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PW"),
    "host": "localhost",
    "port": 5432,
}

def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def fetch_majors():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM Major ORDER BY name;")
            return cur.fetchall()

def fetch_programs_by_major(major_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, university || ' — ' || program_name 
                FROM Institution 
                WHERE major_id = %s
                ORDER BY university;
            """, (major_id,))
            return cur.fetchall()

def get_program_by_id(program_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT university || ' — ' || program_name, url 
                FROM Institution 
                WHERE id = %s
            """, (program_id,))
            return cur.fetchone()

