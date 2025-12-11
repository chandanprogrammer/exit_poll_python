import pickle

model = pickle.load(open("exit_poll_model.pkl","rb"))

sample = [[30,0,2,1,1,3]]  
# age, gender, education, region, income, best_issue (encoded)

prediction = model.predict(sample)[0]
print("Predicted:", prediction)
