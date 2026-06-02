import json

school = {
    "school": "Lakeside Academy",
    "departments": [
        {
            "name": "Science",
            "classes": [
                {
                    "class_name": "10A",
                    "students": [
                        {"name": "Alice", "scores": {"Physics": 82, "Chemistry": 45}},
                        {"name": "Bob",   "scores": {"Physics": 67, "Chemistry": 71}},
                    ]
                }
            ]
        },
        {
            "name": "Arts",
            "classes": [
                {
                    "class_name": "11B",
                    "students": [
                        {"name": "Carol", "scores": {"History": 48, "English": 90}},
                        {"name": "Dave",  "scores": {"History": 35, "English": 42}},
                    ]
                }
            ]
        }
    ]
}

at_risk = []

for dept in school["departments"]:
    for cls in dept["classes"]:
        for student in cls["students"]:
            for subject, score in student["scores"].items():
                if score < 50:
                    at_risk.append({
                        "student":    student["name"],
                        "department": dept["name"],
                        "class":      cls["class_name"],
                        "subject":    subject,
                        "score":      score
                    })

with open("at_risk_students.json", "w") as f:
    json.dump(at_risk, f, indent=2)

print(f"{len(at_risk)} at-risk entries found:")
for entry in at_risk:
    print(f"  {entry['student']} — {entry['subject']}: {entry['score']}")