from llm_interface import get_answer

def main():
    print("Welcome to the Market Intelligence Assistant!")
    print("Ask questions about Apple's market position.")
    print("Type 'exit' to quit.")
    
    while True:
        question = input("\nYour question: ")
        if question.lower() == 'exit':
            break
        answer = get_answer(question)
        print(f"\nAnswer: {answer}")

if __name__ == "__main__":
    main()
