import sys, os, tempfile
with open(sys.argv[1]) as f: bf = f.read()
c,i="""int putchar(int c);int getchar();int main() { static char a[30000], *ptr; ptr=a;""",{">":"++ptr;","<":"--ptr;","+":"++(*ptr);","-":"--(*ptr);",".":"""putchar(*ptr);""",",":"""*ptr=getchar();""","[":"""while(*ptr){""","]":"}"}
for x in bf: c = (c + i[x]) if x in i else c
f = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.c'); f.write(c + "return 0; }"); f.close(); os.system(f"/usr/bin/gcc -w {f.name} -o {sys.argv[2]}"); os.remove(f.name)