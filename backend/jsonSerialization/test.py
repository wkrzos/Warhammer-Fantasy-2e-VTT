import json

if __name__ == "__main__":
    lst = []
    dic = {
        "test": {
            "test2": 'XD'
        }
    }
    lst.append(dic)
    with open("test",'w') as json_file:
        json.dump(lst, json_file)

    json_file.close()
    with open("test", "r") as json_file:
        test = json.load(json_file)
    print (test)