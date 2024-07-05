def generate_shape(n):
    return '\n'.join(['+' * n for _ in range(n)])

print(generate_shape(int(input())))