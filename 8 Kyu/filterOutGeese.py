geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for x in geese:
        if x in birds:
            birds.remove(x)
            
    return birds


print(goose_filter(["Bird", "COuntry","African","Pilgrimase","Toulouse"]))