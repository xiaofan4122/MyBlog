import os
 
def copy_dir(src_path, target_path):
	if os.path.isdir(src_path) and os.path.isdir(target_path):		
		filelist_src = os.listdir(src_path)							
		for file in filelist_src:
			path = os.path.join(os.path.abspath(src_path), file)	
			if os.path.isdir(path):
				path1 = os.path.join(os.path.abspath(target_path), file)	
				if not os.path.exists(path1):						
					os.mkdir(path1)
				copy_dir(path,path1)			
			else:								
				with open(path, 'rb') as read_stream:
					contents = read_stream.read()
					path1 = os.path.join(target_path, file)
					with open(path1, 'wb') as write_stream:
						write_stream.write(contents)
		return 	True	
						
	else:
		return False


import os

def findAllFilesWithSpecifiedSuffix(target_dir, target_suffix="md"):
    find_res = []
    target_suffix_dot = "." + target_suffix
    walk_generator = os.walk(target_dir)
    for root_path, dirs, files in walk_generator:
        if len(files) < 1:
            continue
        for file in files:
            file_name, suffix_name = os.path.splitext(file)
            if suffix_name == target_suffix_dot:
                find_res.append(os.path.join(root_path, file))
    return find_res

def my_replace(file_dir):
	f = open(file_dir, "r", encoding="utf-8")
	txt=f.read();
	f.close()

	print(txt)
	t1="<img src="
	t2="\" alt=\""
	t3="style=\"zoom:"
	t4="%;\" />"

	t11="<center><img src={require('"
	t12="').default} alt=\""
	t13="width=\""
	t14="%\" align=\"middle\"/></center>"


	txt=txt.replace(t1,t11)
	txt=txt.replace(t2,t12)
	txt=txt.replace(t3,t13)
	txt=txt.replace(t4,t14)

	file_dir_replace=file_dir.replace("markdown_docs","docs")

	with open(file_dir_replace, 'w') as f:
		f.write(txt)

	txt=txt.replace(t11,t1)
	txt=txt.replace(t12,t2)
	txt=txt.replace(t13,t3)
	txt=txt.replace(t14,t4)


	with open('abc.md', 'w') as f:
		f.write(txt)
		
copy_dir("F:\AERO\Blog\my-website\markdown_docs","F:\AERO\Blog\my-website\docs")

md_list=findAllFilesWithSpecifiedSuffix("F:\AERO\Blog\my-website\markdown_docs")
for i in md_list:
	my_replace(i)


print("down,{}个md文件已替换".format(len(md_list)))