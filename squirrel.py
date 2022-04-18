import pandas

data = pandas.read_csv("squirrel_Data.csv")

gray =[]
cinammon = []
black = []

fur_color = data["Primary Fur Color"].to_list()
for color in fur_color:
    if color == "Gray":
        gray.append(color)
        # print(len(gray))
    elif color == "Cinnamon" :
        cinammon.append(color)
        
    elif color == "Black" :
        black.append(color)
        
data_dict = {
    "Fur Color" : ["Gray", "Cinammon", "Black"],
    "Count" : [len(gray), len(cinammon) ,len(black)]
}

squirrel = pandas.DataFrame(data_dict)
squirrel.to_csv("squirrel_count.csv")
