import sys
def rows(sql, table):
    for line in sql.split('\n'):
        if not line.startswith(f"INSERT INTO `{table}` VALUES"): continue
        s=line[line.index("VALUES")+6:]; i=0; n=len(s)
        while i<n:
            if s[i]=='(':
                i+=1; row=[]; cur=''; q=False
                while True:
                    c=s[i]
                    if q:
                        if c=='\\':
                            e=s[i+1]; cur+={'n':'\n','r':'\r','t':'\t','0':'\0'}.get(e,e); i+=2; continue
                        if c=="'": q=False
                        else: cur+=c
                    else:
                        if c=="'": q=True
                        elif c==',': row.append(cur); cur=''
                        elif c==')': row.append(cur); break
                        else: cur+=c
                    i+=1
                yield row
            i+=1
