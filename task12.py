try:
    student_dictionary={"alice":40,"pravin":30,"ravi":60,"ram":50}
    a=str(input("enter student name:"))
    b=a.lower()
    c=b.capitalize()
    print(c,"marks: ",student_dictionary[b])
except KeyError:
    print("student not found")
finally:
    print("all done")