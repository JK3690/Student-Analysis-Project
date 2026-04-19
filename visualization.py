import matplotlib.pyplot as plt
from database import (convert, run_query)

filename = "Student Mental health.csv"
config = {'user': 'root', 'password': 'Jess@2009', 'host': 'localhost','database': 'project'}
convert(filename, **config)

def mhi_by_fields():
    mhi_fields = ['Depression', 'Anxiety', 'Panic_attack']
    counts = []

    for issue in mhi_fields:
        count = run_query(f"SELECT COUNT(*) FROM student_mental_health WHERE {issue} = 'Yes';",fetch=True)[0][0]
        counts.append(count)

    plt.pie(counts, labels=mhi_fields, autopct='%1.1f%%')
    plt.title("Mental Health Issues Among Students")
    plt.show()
    
    mhi = input("Enter MHI: ")
    field = input("Enter field: ")

    result = run_query(f"SELECT {field}, COUNT(*) FROM student_mental_health WHERE {mhi}='Yes' GROUP BY {field};",
        fetch=True)

    labels = [row[0] for row in result]
    counts = [row[1] for row in result]
    plt.bar(labels, counts)
    plt.title(f"{mhi} by {field}")
    plt.show()
    
def dist_by_fields():
    field = input("Enter field (Age/Year): ").capitalize().strip()

    allowed_fields = ["Age", "Year"]
    if field not in allowed_fields:
        print("Only numeric fields allowed ❌")
        return

    results = run_query(f"SELECT {field} FROM student_mental_health;", fetch=True)
  
    values = []
    for row in results:
        if row[0] is not None:
            values.append(float(row[0]))

    bins_map = {"Age": 7, "Year": 4}

    plt.hist(values, bins=bins_map[field])
    plt.title(f"Distribution of {field}")
    plt.xlabel(field)
    plt.ylabel("No. of Students")
    plt.show()