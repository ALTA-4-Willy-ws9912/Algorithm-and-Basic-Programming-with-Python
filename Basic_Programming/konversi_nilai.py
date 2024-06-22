
student_score = int(80)

if student_score >= 80 and student_score <= 100:
    nilai_huruf = "A"
elif student_score >= 65 and student_score <= 79:
    nilai_huruf = "B+"
elif student_score >= 50 and student_score <= 64:
    nilai_huruf = "B"
elif student_score >= 35 and student_score <= 49:
    nilai_huruf = "C"
elif student_score >= 0 and student_score <= 34:
    nilai_huruf = "D"
else:
    nilai_huruf = "Nilai tidak ada"


print(f"Nilai {nilai_huruf}")
