# Busca binaria tem tempo de execução O(log n)
def binarySearch(arr, item):
    low = 0
    high = len(arr) - 1 # tamanho do array

    while(low <= high):

        midle = int((low + high)/2)

        kick = arr[midle]

        if(kick == item):
            return midle
        
        if(kick > item):        # se o valor que estou chutando é maior do que estou procurando então
            high = midle - 1    # quer dizer que o eu devo procurar do meio para baixo 
                                #logo o meio deve virar o novo alto
        else:
            low =  midle + 1    # se a condição acima não for atendida é porque o valor esta acima do meio
    return None

arrayTest = [1,3,5,7,8,12,35,22,45,78,90,112,144456,12233451]
result = binarySearch(arrayTest,1)
print(result)