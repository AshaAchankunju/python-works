f1_path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\student.txt"
f2_path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\failed.txt"

f1_read=open(f1_path,"r")
f2_read=open(f2_path,"r")

# all_stud=set()
# fail_stud=set()
# for line in f1_read:
#     student=line.rstrip("\n")
#     all_stud.add(student)

# for line in f2_read:
#     failed=line.rstrip("\n")
#     fail_stud.add(failed)  

# passed_stud=all_stud-fail_stud
# print(passed_stud) 

# or 

all_stud_set={str.rstrip("\n") for str in f1_read}
failed_stud={str.rstrip("\n") for str in f2_read}

passes_stud=all_stud_set-failed_stud
print(passes_stud)