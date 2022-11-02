from lib import moyenne

def test_moyenne():
    data =[1,1,1]
    expected_result = 1

    result = moyenne(data)

    if result != expected_result:
        print('error in moyenne')
        exit(1)

test_moyenne()
exit(0)