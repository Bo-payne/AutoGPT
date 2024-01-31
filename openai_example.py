def query_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='text-davinci-003',
            messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return 'Error: ' + str(e)
