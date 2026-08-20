# Complete Project Guide: 03 Production Ml

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Production ML (Day 1)

**What is Production ML?**
ML systems that:
- Run 24/7
- Handle real users
- Scale automatically
- Monitor performance
- Update models

**Example:**
```
Development: Train model, test locally
Production: Serve 1M predictions/day, monitor, update
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
production_ml/
├── training/
│   ├── train.py
│   └── model.py
├── serving/
│   ├── api.py
│   └── predictor.py
├── monitoring/
│   └── monitor.py
├── data/
└── README.md
```

**Install:**
```bash
pip install flask scikit-learn pandas numpy joblib
```

---

### Step 3: Create Training Pipeline (Day 2-3)

**File: `training/train.py`**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import json
from datetime import datetime

class ModelTrainer:
    """Train and save ML models"""
    
    def __init__(self):
        self.model = None
        self.metrics = {}
    
    def load_data(self, filepath):
        """Load training data"""
        df = pd.read_csv(filepath)
        return df
    
    def prepare_data(self, df, target_column):
        """Prepare features and target"""
        X = df.drop(columns=[target_column])
        y = df[target_column]
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train(self, X_train, y_train):
        """Train model"""
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        print("✅ Model trained")
        return self.model
    
    def evaluate(self, X_test, y_test):
        """Evaluate model"""
        from sklearn.metrics import accuracy_score, classification_report
        
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        self.metrics = {
            'accuracy': accuracy,
            'report': classification_report(y_test, y_pred, output_dict=True),
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"✅ Model accuracy: {accuracy:.4f}")
        return self.metrics
    
    def save_model(self, filepath='models/model.pkl'):
        """Save trained model"""
        joblib.dump(self.model, filepath)
        print(f"✅ Model saved to {filepath}")
    
    def save_metrics(self, filepath='models/metrics.json'):
        """Save model metrics"""
        with open(filepath, 'w') as f:
            json.dump(self.metrics, f, indent=2)
        print(f"✅ Metrics saved to {filepath}")

def main():
    trainer = ModelTrainer()
    
    # Load and prepare data
    df = trainer.load_data('data/training_data.csv')
    X_train, X_test, y_train, y_test = trainer.prepare_data(df, 'target')
    
    # Train model
    trainer.train(X_train, y_train)
    
    # Evaluate
    trainer.evaluate(X_test, y_test)
    
    # Save
    trainer.save_model()
    trainer.save_metrics()

if __name__ == '__main__':
    main()
```

---

### Step 4: Create API Server (Day 4-5)

**File: `serving/api.py`**

```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('models/model.pkl')

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    try:
        # Get input data
        data = request.json
        features = data.get('features', [])
        
        # Convert to DataFrame
        df = pd.DataFrame([features])
        
        # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0].tolist()
        
        return jsonify({
            'prediction': int(prediction),
            'probability': probability,
            'status': 'success'
        }), 200
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """Batch prediction endpoint"""
    try:
        data = request.json
        features_list = data.get('features', [])
        
        # Convert to DataFrame
        df = pd.DataFrame(features_list)
        
        # Make predictions
        predictions = model.predict(df).tolist()
        probabilities = model.predict_proba(df).tolist()
        
        return jsonify({
            'predictions': predictions,
            'probabilities': probabilities,
            'status': 'success'
        }), 200
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

### Step 5: Add Monitoring (Day 6)

**File: `monitoring/monitor.py`**

```python
import time
import json
from datetime import datetime
import requests

class ModelMonitor:
    """Monitor model performance"""
    
    def __init__(self, api_url='http://localhost:5000'):
        self.api_url = api_url
        self.metrics = []
    
    def log_prediction(self, input_data, prediction, latency):
        """Log prediction"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'input': input_data,
            'prediction': prediction,
            'latency_ms': latency * 1000
        }
        self.metrics.append(log_entry)
    
    def check_health(self):
        """Check API health"""
        try:
            response = requests.get(f'{self.api_url}/health', timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def test_prediction(self, test_data):
        """Test prediction and measure latency"""
        start_time = time.time()
        try:
            response = requests.post(
                f'{self.api_url}/predict',
                json={'features': test_data},
                timeout=10
            )
            latency = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                self.log_prediction(test_data, result['prediction'], latency)
                return True, result
            else:
                return False, response.json()
        except Exception as e:
            return False, {'error': str(e)}
    
    def get_stats(self):
        """Get monitoring statistics"""
        if not self.metrics:
            return {}
        
        latencies = [m['latency_ms'] for m in self.metrics]
        
        return {
            'total_predictions': len(self.metrics),
            'avg_latency_ms': sum(latencies) / len(latencies),
            'min_latency_ms': min(latencies),
            'max_latency_ms': max(latencies)
        }
    
    def save_logs(self, filepath='monitoring/logs.json'):
        """Save monitoring logs"""
        with open(filepath, 'w') as f:
            json.dump(self.metrics, f, indent=2)
        print(f"✅ Logs saved to {filepath}")

# Usage example
if __name__ == '__main__':
    monitor = ModelMonitor()
    
    # Test health
    if monitor.check_health():
        print("✅ API is healthy")
        
        # Test prediction
        test_data = [1.0, 2.0, 3.0, 4.0]
        success, result = monitor.test_prediction(test_data)
        
        if success:
            print(f"✅ Prediction: {result}")
        else:
            print(f"❌ Error: {result}")
        
        # Get stats
        stats = monitor.get_stats()
        print(f"📊 Stats: {stats}")
    else:
        print("❌ API is not healthy")
```

---

### Step 6: Create Deployment Script (Day 7)

**File: `deploy.py`**

```python
import subprocess
import os
import time

def deploy():
    """Deploy production ML system"""
    print("=" * 60)
    print("Deploying Production ML System")
    print("=" * 60)
    
    # Step 1: Train model
    print("\n[Step 1] Training model...")
    subprocess.run(['python', 'training/train.py'])
    
    # Step 2: Start API server
    print("\n[Step 2] Starting API server...")
    api_process = subprocess.Popen(
        ['python', 'serving/api.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to start
    time.sleep(3)
    
    # Step 3: Test API
    print("\n[Step 3] Testing API...")
    from monitoring.monitor import ModelMonitor
    monitor = ModelMonitor()
    
    if monitor.check_health():
        print("✅ Deployment successful!")
        print("   API running on http://localhost:5000")
    else:
        print("❌ Deployment failed!")
    
    return api_process

if __name__ == '__main__':
    process = deploy()
    print("\nPress Ctrl+C to stop the server")
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        print("\n✅ Server stopped")
```

---

---