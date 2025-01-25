import random
import time
from datetime import datetime
from faker import Faker
from confluent_kafka import SerializingProducer
fake = Faker()
def generate_sales_transaction():
    user = fake.single_profile()
    return {
        "transactionId": fake.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),
        "productName": fake.choice(['laptop', 'mobile', 'tablet', 'watch', 'headpho','speaker']),
        "productCategory": fake.choice(['electronics', 'fashion', 'grocery', 'home', 'beauty', 'sports']),
        "productPrice": round(random.uniform(100, 1000), 2),
        "productQuantity": random.randint(1, 10),
        "productBrand": random.choice(['apple', 'samsung', 'sony', 'mi', 'oneplus', 'boat']),
        "currency": random.choice(['USD', 'MAD']),
        "customerId": user['username'],
        "transactionDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "paymentMethod": fake.choice(['credit_card', 'debit_card', 'online_payment'])
    }
def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))
def main():
    topic = 'sales'
    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092'
    })


if __name__ == '__main__':
    main()