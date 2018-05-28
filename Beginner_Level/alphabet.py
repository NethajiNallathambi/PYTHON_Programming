A = input("Enter any character: ");
if A == '0':
    exit();
else:
    if((A>='a' and A<='z') or (A>='A' and A<='Z')):
    	print(A, "is an alphabet.");
    else:
    	print(A, "is not an alphabet.");
