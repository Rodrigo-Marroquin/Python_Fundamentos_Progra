def load_file ():
    
    filepath = input("Enter the path of the file to load: ")
    
    file = open (filepath, 'r', encoding = 'utf-8')
    lines = file.readlines()
    file.close()
    
    return lines
    
def set_enviroment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env
    
def print_env(env):
    for row in env:
        for cell in row:
            if cell == 1:
                print('■', end='')
            else:
                print(' ', end='')
        print()

def check_neighbor(env, x, y):
    count = 0
    l1 = [x-1, x, x+1]
    l2 = [y-1, y, y+1]
    for i in l1:
        for j in l2:
            if x == i and y == j:
                continue
            if env[i][j] == 1:
                count += 1
        return count

my_file = load_file()
#print(my_file)
env = set_enviroment(my_file)
print_env(env)