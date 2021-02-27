import pickle
    
with open('model.pkl', 'rb') as handle:
    b = pickle.load(handle)

m_1 = b["m_1"]
m_2 = b["m_2"]
c   = b["c"]

x = 5

result = (m_1*x + m_2*(x**2) + c)

print(m_1)
print(m_2)
print(c)
print(result)