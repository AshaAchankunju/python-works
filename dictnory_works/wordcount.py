
dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]
wc={}

for dist in dengue_list:
    if dist in wc:
        wc[dist]+=1
    else:
        wc[dist]=1
print(wc)

srt_wc=sorted(wc,key=lambda k: wc.get(k), reverse=True)
print(srt_wc)