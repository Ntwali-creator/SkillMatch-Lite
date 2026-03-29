from database import get_connection

def match_user():
    print(" MATCH THE JOBS WITH THE USER ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, skills FROM users")
    users = cursor.fetchall()

    if not users:
       print("\n no user found!")
       conn.close()
       return
    
    cursor.execute("SELECT id, title, skills FROM jobs")
    jobs = cursor.fetchall()

    if not jobs:
       print("\n no job found!")
       conn.close()
       return

    print("\n  MATCH USER TO THE JOB ")
    print("\navailable users:")
    for user in users:
        print(f"ID: {user[0]} | NAME: {user[1]} | SKILLS: {user[2]}")
          
    try:
        user_id = int(input("\nenter user ID"))
    except:
        print(" invalid input ")
        conn.close()
        return

    cursor.execute("SELECT id, name, skills FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
         print(" user not found!")
         conn.close() 
         return

    print(f"\nMatching {user[1]} with jobs....")
    print("=" * 50)

    user_skills = [s.strip().lower().replace(" ", "") for s in user[2].split(',')]

    found = False

    for job in jobs:
        job_title = job[1]
        job_skills = [s.strip().lower().replace(" ", "") for s in job[2].split(',')]

        matching = []

        for skill in user_skills:
            for js in job_skills:
              if skill in js or js in skill:
                  matching.append(skill)

        if matching:
            found = True
            print(f"\n Job: {job_title}")
            print(f" Matching skills: {','.join(matching)}")
            print(f" Match: {len(matching)} out of {len(job_skills)} skills")

    if not found:
        print("\nno matching job found!")

    conn.close()

if __name__ == "__main__":
         match_user()
         input("\n press enter key to exit..")