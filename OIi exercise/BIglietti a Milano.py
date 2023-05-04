with open('input.txt','r') as input:
    for word in input:
        data=word.split()

trip=int(data[0])
CarnetTikets=int(data[1])
TiketPrice=int(data[2])
CarnetPrice=int(data[3])


if CarnetPrice<(trip%CarnetTikets)*TiketPrice:
    answer=((trip//CarnetTikets)+1)*CarnetPrice
    with open('output.txt','w') as output:
        output.write(str(answer))
else:
    answer=((trip//CarnetTikets)*CarnetPrice)+((trip%CarnetTikets)*TiketPrice)
    with open('output.txt','w') as output:
        output.write(str(answer))