a = [100,200,300, True, 4.6]    # LIST banane ka 1la tareeka
print(type(a))
a.append(500)
print(a)

clouds = list() # LIST banane ka 2sra tareeka
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("ibm")
clouds.append("alibaba")
clouds.append("utho")
print(clouds)
print("Length of list is:", len(clouds))
print("World Leader for Cloud Service Provider is:",clouds[0])
print("Indian Cloud Service Provider is:",clouds[-1])

print(dir(clouds))# dir is used to know about the functions which are available for the list and how to use it like what the append function does and how to use it
print(clouds.extend.__doc__) #doc is used to know about the function and how to use it like what the extand function does and how to use it


# ['aws', 'azure', 'gcp', 'ibm', 'alibaba', 'utho']
# range(5) -> 0,1,2,3,4

# iterate a list using for loop
for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} Market Leader + coverd in course")# f string is used to print the value of variable in the string
    elif cloud == "utho":
        print(f"{cloud} Indian Cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} DevOps - Zero To Hero Me vo bhi cover karoonga")
    else:
        print(f"{cloud} baaki nahi honge")