# Credit Card Fraud Detection

This project utilizes a Machine Learning model to detect credit card fraud. The goal is to accurately identify fraudulent transactions from a dataset of credit card transactions.

## Project Structure

- **Dockerfile**: Used to containerize the application.
- **docker-compose.yml**: Defines the services, networks, and volumes for Docker.
- **k8s-deployment.yaml**: Kubernetes deployment configuration.
- **k8s-service.yaml**: Kubernetes service configuration.

## Getting Started

To get started with this project, you will need to have Docker and Kubernetes installed on your machine.

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Build the Docker image**
   ```bash
   docker build -t credit-card-fraud-detection .
   ```

3. **Run the application using Docker Compose**
   ```bash
   docker-compose up
   ```

4. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f k8s-deployment.yaml
   kubectl apply -f k8s-service.yaml
   ```

## Model Description

The Machine Learning model used in this project is designed to analyze transaction data and predict the likelihood of fraud. The model is trained on a labeled dataset of past transactions, with features such as transaction amount, location, and time.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.