"""
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sqlite3
from datetime import datetime

def start_project(project_name):
    conn = sqlite3.connect('surveyoffice.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS time_log
                    (id INTEGER PRIMARY KEY, job_no TEXT, start_time TEXT, end_time TEXT),
                    work_description TEXT''')
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO time_log (job_no, start_time) VALUES (?, ?)',
                   (project_name, start_time))
    conn.commit()
    conn.close()

def stop_project(project_id):
    conn = sqlite3.connect('surveyoffice.db')
    cursor = conn.cursor()
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('UPDATE time_log SET end_time = ? WHERE id = ?', (end_time, project_id))
    conn.commit()
    conn.close()