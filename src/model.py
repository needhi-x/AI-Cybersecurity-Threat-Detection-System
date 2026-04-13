import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    
    print("✅ Model Trained Successfully")
    return model

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    
    acc = accuracy_score(y, predictions)
    prec = precision_score(y, predictions)
    rec = recall_score(y, predictions)
    f1 = f1_score(y, predictions)
    
    print("\n📊 Model Evaluation:")
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 Score:", f1)
    
    return predictions
def plot_confusion_matrix(y, predictions):
    cm = confusion_matrix(y, predictions)
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    
    plt.title("Confusion Matrix")
    plt.savefig("outputs/confusion_matrix.png")
    plt.show()