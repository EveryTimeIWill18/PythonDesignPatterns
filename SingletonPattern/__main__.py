from singleton import Singleton

def main():
    s1 = Singleton()
    s1._instance.first_name = 'William'
    s1._instance.last_name = 'Murphy'
    s1._instance.age = 31

    s2 = Singleton()
    print(s1.__dict__)
    print(s1, s2)

if __name__ == '__main__':
    main()
