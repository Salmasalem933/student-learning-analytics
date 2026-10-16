import psycopg2
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials 

def get_connection():
        return psycopg2.connect(
                dbname='analystmind',
                user='postgres',
                password='salma',
                host='localhost',
                port=5432
        )

def load_students_details():
        conn = get_connection()
        cursor = conn.cursor()
        with open(r"C:\Users\hp\Downloads\Student Learning Analytics System Project-20260719T140957Z-1-001\ Student Learning Analytics System Project\StudentDetails.json") as f:
                data = json.load(f)
                for row in data:
                        cursor.execute("""INSERT INTO student_details (id,name,contact_number,email_id,school_id,grade)
                                    values(%s,%s,%s,%s,%s,%s) on conflict (id) do nothing""",
                                    (
                                        row.get('id'),
                                        row.get('name'),
                                        row.get('contact_number'),
                                        row.get('email_id'),
                                        row.get('school_id'),
                                        row.get('grade')
                                    )
                        )

        conn.commit()
        cursor.close()
        conn.close()
        print("Data loaded successfully into students table")

load_students_details()

def load_performance_input():
        conn = get_connection()
        curr = conn.cursor()

        with open("PerformanceInput.json") as f:
            data = json.load(f)

            for row in data:
                curr.execute("""INSERT INTO performance_input (attempt_id,child_id,school_id,submitted_at,status)
                            values(%s,%s,%s,%s,%s) on conflict (attempt_id) do nothing""",
                            (
                                row.get('id'),
                                row.get('child_id'),
                                row.get('school_id'),
                                row.get('submitted_at'),
                                row.get('status')
                            )
                )
        conn.commit()
        curr.close()
        conn.close()
        print("Data loaded successfully into students table")
  
load_performance_input()

def load_performance_metrics():
    conn = get_connection()
    curr = conn.cursor()
    with open("PerformanceMetrics.json") as f:
        data = json.load(f)
        for row in data:
              curr.execute("""INSERT INTO performance_metrics (metric_id,input_id,processed_date,wpm,wcpm,pronunciation,fluency,noise)
                           values(%s,%s,%s,%s,%s,%s,%s,%s) on conflict (metric_id) do nothing""",
                           (
                                row.get('id'),
                                row.get('input_id'),
                                row.get('processed_date'),
                                row.get('wpm'),
                                row.get('wcpm'),
                                row.get('pronunciation'),
                                row.get('fluency'),
                                row.get('noise')
                                )
                                )
    conn.commit()
    curr.close()
    conn.close()
    print("Data loaded successfully into performance_metrics table")

load_performance_metrics()

def load_from_response():
    conn = get_connection()
    curr = conn.cursor()
    gc = gspread.service_account("bubbly-journey-506202-q3-e42a2e6ded7d.json")
    sh = gc.open_by_key('1ThgP6FhCv_aweXxEHQTeNFkrRAQcmkdp09-nUGgRAqg')
    
    worksheet = sh.worksheet('FormResponse')

    data = worksheet.get_all_records()
    for row in data:
        curr.execute("""INSERT INTO form_responces (form_submission_date,school_id,school_name,city,state,contact_number,email_id,no_of_students)
                    values(%s,%s,%s,%s,%s,%s,%s,%s) on conflict (school_id) do nothing""",
                    (
                        row.get('form_submission_date'),
                        row.get('school_id'),
                        row.get('school_name'),
                        row.get('city'),
                        row.get('state'),
                        row.get('contact_number'),
                        row.get('email_id'),
                        row.get('no_of_students')
                    )
        )
    conn.commit()
    curr.close()
    conn.close()
    print("Data loaded successfully from google sheet into form_responces table")

load_from_response()