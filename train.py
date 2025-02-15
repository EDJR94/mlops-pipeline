import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

def train_and_save_model(model_path: str):
    # Load a simple dataset
    data = load_iris()
    X, y = data.data, data.target

    # Train a simple model
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    # Save the model
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model("/tmp/model.pkl")