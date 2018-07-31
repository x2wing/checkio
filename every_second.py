


def main(array):
    return array[-1] * sum(filter(lambda x: not x%2,array))

if __name__ == '__main__':
    print (main([1,2,3,4,5]))