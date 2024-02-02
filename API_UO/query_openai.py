import openai

def query_openai(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,  # Adjust as needed for creativity
            max_tokens=150,  # Adjust as needed for response length
            n=1,  # Number of completions to generate
            stop=None  # Stop sequence, if any
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return 'Error: ' + str(e)
