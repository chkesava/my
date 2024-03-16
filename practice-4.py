"""wrire a program to check the type of triangle where yountake the input from the user and clasify accordingly into euailateral isoloclis and scaling"""
s1=int(input())
s2=int(input())
s3=int(input())
if(s1==s2 and s2==s3):
    print("euilateral Triangel")
elif(s1==s2 or s2==s3 or s1==s3):
    print("isoloclis Triangel")
else:
    print("scalling Trinagle")
