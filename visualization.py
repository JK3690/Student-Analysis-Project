import matplotlib.pyplot as plt
from database import *
def mhi_by_fields():
    con = m.connect(**config)
    cursor = con.cursor()
    mhi_fields = ['Depression', 'Anxiety', 'Panic_attack']
    counts = []

    for issue in mhi_fields:
        cursor.execute(f"SELECT COUNT(*) FROM student_mental_health WHERE {issue} = 'Yes';")
        count = cursor.fetchone()[0]
        counts.append(count)

    cursor.close()
    con.close()

    plt.pie(counts, labels=mhi_fields, autopct='%1.1f%%')
    plt.title("Mental Health Issues Among Students")
    plt.show()
    
    mhi = input("Enter MHI: ")
    field = input("Enter field: ")

    result = run_query(
        f"SELECT {field}, COUNT(*) FROM student_mental_health WHERE {mhi}='Yes' GROUP BY {field};",
        fetch=True
    )

    labels = [row[0] for row in result]
    counts = [row[1] for row in result]

    plt.bar(labels, counts)
    plt.title(f"{mhi} by {field}")
    plt.show()
def dist_by_fields(filename):
    field = clean_input("Enter field: ")
    results = run_query(f"SELECT {field}, COUNT(*) FROM student_mental_health GROUP BY {field};", fetch=True)
    values = []
    bin = {"Age": 7, "Year": 4}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                values.append(float(row[field]))
            except ValueError:
                continue
    if field in bin:
        plt.hist(values, bins=bin[field], edgecolor='pink')
        plt.title(f"Distribution of {field}")
        plt.xlabel(field)
        plt.ylabel("No. of Students")
        plt.show()
    else:
        print("Selected field is not numeric, histogram skipped. 📊")
    return results
