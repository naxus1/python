
numCompetitors = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
numCompetitors.sort()
count_reviews = []
result_reviews = []
numReviews = ["newshop is providing good services in the city; everyone should use newshop", "best services by newshop", "fashionbeats has great services in the city", "I am proud to have fashionbeats", "mymarket has awesome services", "Thanks newshop for the quick delivery.", "mymarket has awesome services", ]
cont = 0


for competitors in numCompetitors:
    for reviews in numReviews:
        lis = reviews.lower().count(competitors)
        if lis > 0:
            cont += 1
    count_reviews.append(cont)
    cont = 0
print(count_reviews)
c = list(zip(count_reviews, numCompetitors))
c.sort()
c.reverse()
print(c)

for i in range(len(c)):
    if i < len(c)-1:
        if c[i][0] == c[i+1][0] and c[i][0]>0:
            a = c[i][1] if c[i][1] > c[i+1][1] else c[i+1][1]
            print(a)
            result_reviews.append(c[i])
            c.pop(i)
        elif c[i][0] > c[i+1][0] and c[i][0]>0:
            print(c[i][1])
            result_reviews.append(c[i])
print(result_reviews)