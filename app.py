from openai import OpenAI
client = OpenAI()
conversation_history = []
while True:
    question=input("You: ")
    if question.lower() == "exit":
        print("AI: Good Bye!")
        break
    
    conversation_history.append({
        "role":"user",
        "content":question
        }
    )
    
    response = client.responses.create(
    model = "gpt-5.6-luna",
    input = conversation_history
    )
    
    conversation_history.append({
            "role":"assistant",
            "content":response.output_text
    })

    print("AI: ",response.output_text)
    
print(conversation_history)
 