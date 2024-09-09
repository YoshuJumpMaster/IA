

def perceptron_input(inputs, weights, bias):

    weighted_sum = bias + sum([i * w for i, w in zip(inputs, weights)])
    print(f"Soma ponderada com viés incluído : {weighted_sum}")
    return weighted_sum

def perceptron_output(weighted_sum):

    threshold = 2

    if weighted_sum > threshold:
        print("1")
        return 1
    else:
        print("0")
        return 0
    
    

def main():


    # ex1
    inputs = [1, 1, 2]
    weights = [1, 1, 0]
    bias = 0.5
    weighted_sum = perceptron_input(inputs, weights, bias)
    perceptron_output(weighted_sum)

    # ex2
    inputs = [0, 1, 3]
    weights = [1, -1, 0.5]
    bias = 1.0
    weighted_sum = perceptron_input(inputs, weights, bias)
    perceptron_output(weighted_sum)

    # ex3
    inputs = [2, -1, 1]
    weights = [0.5, 0.5, -1]
    bias = 0.2
    weighted_sum = perceptron_input(inputs, weights, bias)
    perceptron_output(weighted_sum)

if __name__ == "__main__":
    main()
