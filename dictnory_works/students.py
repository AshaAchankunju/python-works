students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
]

# 1--- total number of students
#print("total number of students:", len(students))

# 2--- print all student name
# for s in students:
#     print(s.get("name"))
#           or
all_stud_name=[s.get("name") for s in students]
# print(all_stud_name)
          
# 3--- print student names whose exp>1
# for s in students:
#     if s.get("exp")>1:
#         print(s.get("name"))
        # or
stud_exp_gt=[s.get("name") for s in students if s.get("exp")>1]
#  print(stud_exp_gt)

# 4--- print student names whos skills contain both java and python
# for stud in students:
#     if "java" in stud.get("skills") and "python" in stud.get("skills"):
#         print(stud.get("name"))

# 5--- print mca student names
stud_name=[s.get("name") for s in students if s.get("qualification")=="mca"]
# print(stud_name)

# 6-- most experienced student
most_experienced=max(students, key=lambda d:d.get("exp"))
highest_exp=most_experienced.get("exp")
exp_studs=[s.get("name")for s in students if s.get("exp")==highest_exp]
# print(exp_studs)

# 7 print students name having skills>2
# for s in students:
    # if len(s.get("skills"))>2:
        # print(s.get("name"))

# 8 print students name starts with j
# for stud in students:
#     if stud.get("name").startswith("j"):
         # print(stud.get("name"))

# 9 most students having skills
skill_count={}
for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)


    

