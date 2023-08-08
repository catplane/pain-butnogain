import g4f

response = g4f.ChatCompletion.create(model=g4f.models.gpt_4, provider=g4f.Provider.ChatgptAi, messages=[
                                     {"role": "user", "content": "how to setup qos of one port on ovs"}], stream=False)

print(response)