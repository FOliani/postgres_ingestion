def create_fake_data():

    from faker import Faker
    import pandas as pd

    fake = Faker('en_US')

    # Define the number of rows in the dataset
    num_rows = 2000

    data = []

    # Generate data for each row
    for _ in range(num_rows):
        name = fake.name()
        age = fake.random_int(min=18, max=65)
        city = fake.city()
        email = fake.email()
        phone_number = fake.phone_number()

        # Create a dictionary representing a row of data
        row = {
            'Name': name,
            'Age': age,
            'City': city,
            'Email': email,
            'Phone Number': phone_number
        }

        # Append the row to the data list
        data.append(row)

    # Create a Pandas Dataframe from the data list
    df = pd.DataFrame(data)

    # Print some rows of the data set
    print(df.head())
