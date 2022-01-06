
def letterCounter(names):

    results = {}
    for name in names:
        letters = 0;
        for letter in name:
            letters += 1;
        results.update({name : letters})
            

    return results

names = ['hayder','aly','jutt','python','javascript','java']
print(letterCounter(names))
        

