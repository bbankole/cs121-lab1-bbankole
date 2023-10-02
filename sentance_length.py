def main():
    # write your code here
    sentence = input("Enter a sentence:")
    
    count = len(sentence)

    round_count = count - (count % 10)

    approx_length = round_count * 10

    print("The length of this sentence is", approx_length)
    
    return

if __name__ == '__main__':
    main()