# in dictornary we can add different data types as value but key should be unique and immutable data type like str, int, float, bool, tuple etc. 
info = {
    "name" : "Shubham Bhaiya", #str
    "city" : "Pune", #str
    "qualification": "Mtech",
    "age" : 29, # int
    "salary": 22.5, # float
    "married": True, # Bool
    "favourites" : ["teaching", "movies", 18]
}

print("I live in",info["city"])
print("I love ", info.get("favourite","Not Found"))# error ke kaise bach sakte hai get function ka use karke agar key nahi milega to Not Found print karega

info.update({"channel": "TrainWithShubham"})#info ko update karne ke liye update function ka use karte hai

print(dir(info))


for key,value in info.items():# items function is used to get the key and value of the dictornary
    print(key,value)