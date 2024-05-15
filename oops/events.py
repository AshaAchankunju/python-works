events=[
    
    {"id":1,"name":"mrg","client":"roshan","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":2,"name":"engagement","client":"bilal","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":3,"name":"mrg","client":"manoj","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":4,"name":"birthday","client":"mobin","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":5,"name":"anniversary","client":"soumya","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":6,"name":"meeting","client":"athira","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":7,"name":"xmascelebration","client":"anjali","date":"12-12-2024","place":"ekm","budget":800000},
   

]

# event_details=[e for e in events if e.get("id") ==id ]
# print(event_details)

# id=1
# for e in events :
#     if e.get("id")==id:
#         e.update({"budget":1000000})
#         print(e)

id=5
event_object=[e for e in events if e.get("id")==id][0]
   
